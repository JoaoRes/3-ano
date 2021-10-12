from os import wait
from requests.models import Response
import schedule
import time
import requests
import json
from firebase import firebase 
import json 
from types import SimpleNamespace
import datetime
import pyrebase

firebase = firebase.FirebaseApplication("https://detiwall-pei-default-rtdb.firebaseio.com/", None)

firebaseConfig = {
        "apiKey": "AIzaSyAGlltLGv62NuK7A0Af1TUE2SrE2x1pW4A",
        "authDomain": "detiwall-pei.firebaseapp.com",
        "databaseURL": "https://detiwall-pei-default-rtdb.firebaseio.com",
        "projectId": "detiwall-pei",
        "storageBucket": "detiwall-pei.appspot.com",
        "messagingSenderId": "251921800960",
        "appId": "1:251921800960:web:ae6613c0a2c38220041de5",
        "measurementId": "G-K70JYWB1R3"
        };
#Initialize the app with a service account, granting admin privileges
firebase = pyrebase.initialize_app(firebaseConfig)

db = firebase.database()

count=0

def access_token():
    url = 'https://wso2-gw.ua.pt/token?grant_type=client_credentials&state=1234567890&scope=openid'

    x = requests.post(url, headers={"Content-Type":"application/x-www-form-urlencoded", "Authorization" : "Basic VlNPdUMzT0FoZDFscnVBdDdHNmNCU3dNOHprYTp1c2tOMnJhcnJIU090V2dhU2NyT01zU0ZoUklh"} )
    response= x.json()
    return response["access_token"]

token=access_token()

def access_points():
    
    url = 'https://wso2-gw.ua.pt/primecore_primecore-ws/1.0.0/AccessPoint?maxResults=1000'
    authorization = "Bearer " + token
    x= requests.get(url, headers={"Authorization" : authorization})
    response= x.json()
    results = db.child("data").child(count).set(response)
    
    

    #result= firebase.post( "/data" , response)

def deleting():
    data = db.child('data').shallow().get()
    mydata = list(data.val())
    mydata = [int(x) for x in mydata]
    mydata.sort()
    print(mydata)
    if len(mydata)>5:
        db.child("data").child(mydata[0]).remove()

def counter():
    global count
    count = count + 1
    
    
access_token()
access_points()


schedule.every(60).minutes.do(access_token)
time.sleep(30)
schedule.every(15).minutes.do(access_points)
time.sleep(2)
schedule.every(15).minutes.do(counter)
schedule.every(15).minutes.do(deleting)



while True:
    schedule.run_pending()
    time.sleep(1)
 	
    
