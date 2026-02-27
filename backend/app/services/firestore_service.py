from firebase_admin import firestore
import firebase_admin

db = firestore.client()

def add_vehicle(data):
    doc_ref = db.collection("vehicles").document()
    doc_ref.set(data)
    return doc_ref.id

def get_all_vehicles():
    docs = db.collection("vehicles").stream()
    return [{**doc.to_dict(), "id": doc.id} for doc in docs]

def delete_vehicle(vehicle_id):
    db.collection("vehicles").document(vehicle_id).delete()