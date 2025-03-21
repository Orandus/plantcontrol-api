from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class SensorData(BaseModel):
    id: Optional[int]
    temperature: float
    humidity: float
    macaddress: str
    datetime: datetime

    class Config:
        orm_mode = True

# Schema for creating new sensor data
class SensorDataCreate(BaseModel):
    temperature: float
    humidity: float
    macaddress: str

# Schema for responding with sensor data
class SensorDataResponse(BaseModel):
    id: int
    temperature: float
    humidity: float
    macaddress: str
    datetime: datetime

    class Config:
        orm_mode = True