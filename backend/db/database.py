from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from core.config import settings

engine = create_engine(settings.DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_database():
    db = SessionLocal()
    try: #gives access to the database session
        yield db
    finally:
        db.close()

def create_tables():
    Base.metadata.create_all(bind=engine) #creates tables based on models