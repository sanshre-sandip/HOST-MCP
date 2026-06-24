from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

#database configuration
db = "postgresql://postgres:sandy1234@localhost:5432/test1"

engine = create_engine(db)
session = sessionmaker(autocommit=False, autoflush=False, bind=engine)