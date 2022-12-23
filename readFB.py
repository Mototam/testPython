import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use a service account.
cred = credentials.Certificate('path/to/demoapp01-d72ce-firebase-adminsdk-9i22i-baf50a6231.json')

app = firebase_admin.initialize_app(cred)

db = firestore.client()

users_ref = db.collection(u'users')
docs = users_ref.stream()

for doc in docs:
    print(f'{doc.id} => {doc.to_dict()}')

data = users_ref.get()
print(data)