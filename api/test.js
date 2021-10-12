var data = "";
var xhr = new XMLHttpRequest();
xhr.withCredentials = true;
xhr.addEventListener("readystatechange", function() {
  if(this.readyState === 4) {
    console.log(this.responseText);
  }
});
xhr.open("GET", "https://wso2-gw.ua.pt/primecore_primecore-ws/1.0.0/AccessPoint?maxResults=100&firstResult=0");
xhr.setRequestHeader("Authorization", "Bearer b5e6719f-db4e-3bde-b6fd-c3027edb6968");
xhr.send(data);