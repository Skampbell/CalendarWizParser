
# Import database module.
import firebase_admin
from firebase_admin import db
from firebase_admin import credentials

def postToFirebase(events, date):
    cred = credentials.Certificate("serviceAccountKey.json")
    # Initialize the app with a service account, granting admin privileges
    firebase_admin.initialize_app(cred, {'databaseURL': 'https://tstreetapp-skyler.firebaseio.com'})


    # Get a database reference to our blog.
    print(str(date["year"]) + '/' + str(date["month"]))
    ref = db.reference(str(date["year"]) + '/' + str(date["month"]) +'/')

    ref.set(events)
