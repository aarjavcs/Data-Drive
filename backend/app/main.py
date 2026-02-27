from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import vehicle
from app.config.firebase_config import db  # Only needed for test-db

app = FastAPI()

# Enable CORS (Hackathon mode)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Later restrict to Netlify URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Root endpoint
@app.get("/")
def root():
    return {"message": "Vehicle Intelligence Backend Running 🚗"}

# Health check
@app.get("/health")
def health():
    return {"status": "healthy"}

# Test Firestore
@app.get("/test-db")
def test_db():
    doc_ref = db.collection("test").document("hello")
    doc_ref.set({"message": "Firebase connected 🚀"})
    return {"status": "Firestore write successful"}

# Include vehicle routes
app.include_router(vehicle.router, prefix="/vehicle", tags=["Vehicle"])