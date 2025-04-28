from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

database_url = "postgresql://postgres:root@localhost:5432/fastapi"

# Create the SQLAlchemy engine
engine = create_engine(database_url)

# Create a session local
SessionLocal = sessionmaker(bind=engine,autoflush=False)


# Create a Base class for models
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
