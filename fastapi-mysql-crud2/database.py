
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Local MySQL connection
DATABASE_URL = "mysql+pymysql://root:root@localhost/db6"

engine = create_engine(DATABASE_URL)

# execute/perfrom CRUD Operations Database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
