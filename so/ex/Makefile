CXXFLAGS = -Wall -ggdb -pthread

LDFLAGS = -pthread -lm

TARGETS = bounded_buffer_safe

all:	$(TARGETS)

bounded_buffer_safe:	fifo_safe.o bounded_buffer.o delays.o thread.o utils.o
		g++ -o $@ $^ $(LDFLAGS)

ex3: ex3.o thread.o utils.o delays.o
	g++ -o $@ $^ $(LDFLAGS)

fifo_safe.o:	fifo.h

thread.o utils.o:	%.o:	%.h dbc.h

delays.o:	%.o:	%.h

clean:
		rm -f *.o *~

cleanall:	clean
		rm -f $(TARGETS)
