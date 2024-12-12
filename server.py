from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from datetime import datetime

# Initialize the FastAPI app
app = FastAPI()

# In-memory storage for alerts
critical_alerts = []

# Pydantic model for alert items
class AlertItem(BaseModel):
    patient_id: str
    glucose_value: float
    alert_type: str
    origin: str
    timestamp: datetime = datetime.utcnow()

# Root endpoint
@app.get("/")
def read_root():
    """
    Root endpoint that returns a welcome message.
    """
    return {"message": "Welcome to the Alert Management System!"}

# GET endpoint to retrieve all alerts
@app.get("/alerts", response_model=List[AlertItem])
def get_alerts():
    """
    Endpoint to retrieve all the critical alerts.
    """
    return critical_alerts

# POST endpoint to add a new alert
@app.post("/alerts", status_code=201)
def post_alert(alert: AlertItem):
    """
    Endpoint to add a new critical alert.
    """
    critical_alerts.append(alert)
    return {"message": "Alert received"}
