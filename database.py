
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

db_url = "postgresql+psycopg2://postgres:postgres123@localhost:5432/local_db"
engine=create_engine(db_url)
session=sessionmaker(autoflush=False,autocommit=False,bind=engine)