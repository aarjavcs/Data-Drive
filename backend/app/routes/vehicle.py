from fastapi import APIRouter
from app.services.firestore_service import add_vehicle, get_all_vehicles, delete_vehicle

router = APIRouter()

@router.post("/")
def create_vehicle(vehicle: dict):
    vehicle_id = add_vehicle(vehicle)
    return {"message": "Vehicle added", "id": vehicle_id}

@router.get("/")
def fetch_vehicles():
    return get_all_vehicles()

@router.delete("/{vehicle_id}")
def remove_vehicle(vehicle_id: str):
    delete_vehicle(vehicle_id)
    return {"message": "Vehicle deleted"}