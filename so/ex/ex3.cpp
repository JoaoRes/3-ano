#include  <stdio.h>
#include  <stdlib.h>
#include  <unistd.h>
#include  <sys/wait.h>
#include  <sys/types.h>
#include  <pthread.h>
#include  <math.h>

//#include  "fifo.h"
#include  "delays.h"
#include  "thread.h"

#define  FIFOSZ         10
#define  N              10

typedef struct ServiceRequest 
{
    unsigned int client_id;
    char const* str;

} ServiceRequest;

typedef struct ServiceResponse
{
    unsigned int server_id;
    unsigned int nchar = 0;
    unsigned int ndig = 0;
    unsigned int nlet = 0;
} ServiceResponse;

typedef struct FIFO
{ 
    unsigned int ii;   ///< point of insertion
    unsigned int ri;   ///< point of retrieval
    unsigned int cnt;  ///< number of items stored
    unsigned int slot[FIFOSZ];  ///< storage memory

    pthread_cond_t fifoNotFull = PTHREAD_COND_INITIALIZER;
    pthread_cond_t fifoNotEmpty = PTHREAD_COND_INITIALIZER;
    pthread_mutex_t accessCR = PTHREAD_MUTEX_INITIALIZER;

} FIFO;

typedef struct BUFFER
{
    unsigned int id;
    ServiceRequest req;
    ServiceResponse res;
    bool resAvailable = false;

    pthread_cond_t responseAvailable = PTHREAD_COND_INITIALIZER;
    pthread_mutex_t accessCR = PTHREAD_MUTEX_INITIALIZER;
} BUFFER;


BUFFER pool[N];
static FIFO freeBuffers;
static FIFO pendingRequests;

/* Initialization of the FIFO */
void freeBuffersInit(void)
{
    mutex_lock(&freeBuffers.accessCR);

    unsigned int i;
    for (i = 0; i < FIFOSZ; i++)
    {
        freeBuffers.slot[i] = i;
    }
    freeBuffers.ii = freeBuffers.ri = 0;
    freeBuffers.cnt = FIFOSZ;

    cond_broadcast(&freeBuffers.fifoNotEmpty);

    mutex_unlock(&freeBuffers.accessCR);
}

/* Initialization of the FIFO */
void pendingRequestsInit(void)
{
    mutex_lock(&pendingRequests.accessCR);

    unsigned int i;
    for (i = 0; i < FIFOSZ; i++)
    {
        pendingRequests.slot[i] = 99999999;
    }
    pendingRequests.ii = pendingRequests.ri = 0;
    pendingRequests.cnt = 0;

    cond_broadcast(&pendingRequests.fifoNotFull);

    mutex_unlock(&pendingRequests.accessCR);
}

/* Check if FIFO is full */
static bool fifoFull(FIFO* fifo)
{
    return fifo->cnt == FIFOSZ;
}

/* ************************************************* */

/* Check if FIFO is empty */
static bool fifoEmpty(FIFO* fifo)
{
    return fifo->cnt == 0;
}

/* ************************************************* */

/* Insertion of an id into the FIFO  */
void fifoIn(FIFO* fifo, unsigned int buf_id)
{
    mutex_lock(&fifo->accessCR);

    /* wait while fifo is full */
    while (fifoFull(fifo))
    {
        cond_wait(&fifo->fifoNotFull, &fifo->accessCR); 
    }

    fifo->slot[fifo->ii] = buf_id;
    fifo->ii = (fifo->ii + 1) % FIFOSZ;
    fifo->cnt++;

    cond_broadcast(&fifo->fifoNotEmpty);

    mutex_unlock(&fifo->accessCR);
}

/* ************************************************* */

/* Retrieval of an id from the FIFO */

void fifoOut (FIFO* fifo, unsigned int * idp)
{
    mutex_lock(&fifo->accessCR);

    /* wait while fifo is empty */
    while (fifoEmpty(fifo))
    {
        cond_wait(&fifo->fifoNotEmpty, &fifo->accessCR); 
    }

    *idp = fifo->slot[fifo->ri];
    fifo->slot[fifo->ri] = 99999999;
    fifo->ri = (fifo->ri + 1) % FIFOSZ;
    fifo->cnt--;

    cond_broadcast(&fifo->fifoNotFull);

    mutex_unlock(&fifo->accessCR);
}

/* ******************************************************* */

/* CLIENT SIDE */

unsigned int getFreeBuffer(void) 
{
    unsigned int id;
    fifoOut(&freeBuffers, &id);
    return id;
}

/* ******************************************************* */

void putRequestData(char const* str, unsigned int buf_id) 
{
    pool[buf_id].req.str = str;
}

/* ******************************************************* */

void addNewPendingRequest(unsigned int buf_id)
{
    fifoIn(&pendingRequests, buf_id);
}

/* ******************************************************* */

void waitForResponse(unsigned int buf_id)
{
    while(!pool[buf_id].resAvailable) {
        cond_wait(&pool[buf_id].responseAvailable, &pool[buf_id].accessCR);
    }
}

/* ******************************************************* */

ServiceResponse* getResponseData(unsigned int buf_id)
{
    return &pool[buf_id].res;
}

/* ******************************************************* */

void releaseBuffer(unsigned int buf_id) 
{
    fifoIn(&freeBuffers, buf_id);
}

/* ******************************************************* */

void callService(ServiceRequest &req, ServiceResponse &res) 
{
    
    unsigned int buf_id = getFreeBuffer();

    mutex_lock(&pool[buf_id].accessCR);

    putRequestData(req.str, buf_id);
    addNewPendingRequest(buf_id);
    
    waitForResponse(buf_id);
    res = *getResponseData(buf_id);

    mutex_unlock(&pool[buf_id].accessCR);

    releaseBuffer(buf_id);
    pool[buf_id].resAvailable = false;
    
}

/* ******************************************************* */

/* SERVER SIDE */

unsigned int getPendingRequest(void)
{
    unsigned int buf_id;
    fifoOut(&pendingRequests, &buf_id);
    return buf_id;
}

/* ******************************************************* */

ServiceRequest* getRequestData(unsigned int buf_id) 
{
    return &pool[buf_id].req;
}

/* ******************************************************* */

ServiceResponse* produceResponse(ServiceRequest* req)
{

    ServiceResponse* res = new ServiceResponse();
    unsigned int i;
    char c;
    for (i = 0; req->str[i] != '\0'; i++) {
        c = req->str[i]; 
        if ((c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z')) { res->nlet++; }
        else if (c >= '0' && c <= '9') { res->ndig++; }
        res->nchar++;
    }

    return res;
}

/* ******************************************************* */

void putResponseData(ServiceResponse* res, unsigned int buf_id)
{
    pool[buf_id].res = *res;
}

/* ******************************************************* */

void signalResponseIsAvailable(unsigned int buf_id) 
{
    cond_broadcast(&pool[buf_id].responseAvailable);
    pool[buf_id].resAvailable = true;
}

/* ******************************************************* */

void processService() 
{
    unsigned int buf_id = getPendingRequest();
    
    mutex_lock(&pool[buf_id].accessCR);

    ServiceRequest* req;
    ServiceResponse* res;

    req = getRequestData(buf_id);
    res = produceResponse(req);
    putResponseData(res, buf_id);
    signalResponseIsAvailable(buf_id);

    mutex_unlock(&pool[buf_id].accessCR);
}

/* ******************************************************* */

/* The Server thread */
void* server(void* argp)
{
    int id = *((int*) argp);
    printf("Server %d entered\n", id);

    while(1) {
        processService();
    }

    return NULL;
}

/* ******************************************************* */

/* The Client thread */
void* client(void* argp)
{
    int id = *((int*) argp);
    

    //int n = 60;
    // while(1) {
        ServiceRequest* req = new ServiceRequest();
        ServiceResponse* res = new ServiceResponse();

        req->client_id = id;
        req->str = "teste1111";

        callService(*req, *res);

        printf("\e[31;01mClient %d:\e[0m\nChars: %d Letters: %d Digits: %d\n", id, res->nchar, res->nlet, res->ndig);
    //  n--;
    //     if(n == 0) {
    //         return 0;
    //     }
    // }
    printf("Client %d is finished\n", id);

    return NULL;
}

/* ******************************************************* */

/*   main thread: it starts the simulation and generates the producer and consumer threads */
int main(int argc, char *argv[])
{

    freeBuffersInit();
    pendingRequestsInit();

    /* launching the clients */
    int nClients = 5;
    pthread_t cthr[nClients];   /* consumers' ids */
    printf("Launching Client threads\n");
    int i;
    for (i = 0; i < nClients; i++)
    {
        thread_create(&cthr[i], NULL, client, (void*) &i);
    }

    /* launching the server */
    int nServer = 1;
    pthread_t pthr[nServer];      /* producers' ids */
    printf("Launching Server threads\n");
    //unsigned int id;
    for (i = 0; i < nServer; i++)
    {
        thread_create(&pthr[i], NULL, server, (void*) &i);
    }
    
    /* wait for threads to conclude */
    for (i = 0; i < nClients; i++)
    {
        thread_join(cthr[i], NULL);
        printf("Consumer thread %d has terminated\n", i);
    }
    for (i = 0; i < nServer; i++)
    {
        thread_cancel(pthr[i]);
        printf("Producer thread %d has terminated\n", i);
    }

    return EXIT_SUCCESS;
}

