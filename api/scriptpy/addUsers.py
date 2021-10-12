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

firebase = firebase.FirebaseApplication("https://detiwall-pei-default-rtdb.firebaseio.com/", None)
firebase.post("/users","F6aM63ZSz6geukv3ulm1cCPNkgH3")