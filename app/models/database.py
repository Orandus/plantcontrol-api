from sqlalchemy import create_engine, Column, Integer, Float, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy import inspect
from datetime import datetime
from dotenv import load_dotenv
import os


dotenv_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env')
load_dotenv(dotenv_path)
# load_dotenv()

SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")

# Define the database URI
print("Database URI: ", SQLALCHEMY_DATABASE_URI)

# Create the engine
engine = create_engine(SQLALCHEMY_DATABASE_URI, echo=True)

# Use the inspector to get table names
inspector = inspect(engine)
print(inspector.get_table_names())  # Correct way to get table names

# Create a session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Define the base class for models
Base = declarative_base()

# Define the SensorData model
class SensorData(Base):
    __tablename__ = "temp_hum_sensor_data"

    id = Column(Integer, primary_key=True, index=True)
    temperature = Column(Float, nullable=False)
    humidity = Column(Float, nullable=False)
    macaddress = Column(String(50), nullable=False)
    datetime = Column(DateTime, default=datetime.utcnow)

# Define the get_db function
def get_db():
    db: Session = SessionLocal()
    try:
        yield db
    finally:
        db.close()