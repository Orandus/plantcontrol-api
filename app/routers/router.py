from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.models.database import get_db
from app.schemas.schemas import SensorDataCreate, SensorDataResponse
from app.models.database import SensorData  # Assuming SensorData is defined in database.py

router = APIRouter()

@router.post("/sensor-data/", response_model=SensorDataResponse)
def create_sensor_data(sensor_data: SensorDataCreate, db: Session = Depends(get_db)):
    db_sensor_data = SensorData(**sensor_data.dict())
    db.add(db_sensor_data)
    db.commit()
    db.refresh(db_sensor_data)
    return db_sensor_data

@router.get("/sensor-data/{sensor_data_id}", response_model=SensorDataResponse)
def read_sensor_data(sensor_data_id: int, db: Session = Depends(get_db)):
    sensor_data = db.query(SensorData).filter(SensorData.id == sensor_data_id).first()
    if sensor_data is None:
        raise HTTPException(status_code=404, detail="Sensor data not found")
    return sensor_data

@router.put("/sensor-data/{sensor_data_id}", response_model=SensorDataResponse)
def update_sensor_data(sensor_data_id: int, sensor_data: SensorDataCreate, db: Session = Depends(get_db)):
    db_sensor_data = db.query(SensorData).filter(SensorData.id == sensor_data_id).first()
    if db_sensor_data is None:
        raise HTTPException(status_code=404, detail="Sensor data not found")
    for key, value in sensor_data.dict().items():
        setattr(db_sensor_data, key, value)
    db.commit()
    db.refresh(db_sensor_data)
    return db_sensor_data

@router.delete("/sensor-data/{sensor_data_id}")
def delete_sensor_data(sensor_data_id: int, db: Session = Depends(get_db)):
    db_sensor_data = db.query(SensorData).filter(SensorData.id == sensor_data_id).first()
    if db_sensor_data is None:
        raise HTTPException(status_code=404, detail="Sensor data not found")
    db.delete(db_sensor_data)
    db.commit()
    return {"detail": "Sensor data deleted successfully"}