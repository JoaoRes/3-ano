import pyrebase

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
# Initialize the app with a service account, granting admin privileges
firebase = pyrebase.initialize_app(firebaseConfig)

db = firebase.database()
data = db.child('data').remove()#shallow().get()



mydata = list(data.val())
mydata = sorted(mydata)
if len(mydata)>5:
        db.child("data").child(mydata[0]).remove()
