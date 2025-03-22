from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker

# MySQL Database Configuration
DB_USERNAME = "root"
DB_PASSWORD = ""  # Add your password if needed
DB_HOST = "127.0.0.1"
DB_PORT = "3306"
DB_NAME = "hackmit"

# Database URL
DATABASE_URL = f"mysql+mysqlconnector://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Create Database Engine
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
metadata = MetaData()

# Function to Get Database Session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
