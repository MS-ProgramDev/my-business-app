from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASS}@localhost:5432/business_db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
