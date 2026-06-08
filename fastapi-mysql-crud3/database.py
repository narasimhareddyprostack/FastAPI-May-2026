
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Local MySQL connection String
DATABASE_URL = "mysql+pymysql://root:root@localhost/db6"
# Establish the database connection 
engine = create_engine(DATABASE_URL)
# execute/perfrom CRUD Operations Database
SessionLocal = sessionmaker(
                            autocommit=False, 
                            autoflush=False, 
                            bind=engine
)
# Used to create database models (tables)
Base = declarative_base()


'''
create_engine → Creates a connection to the database.
sessionmaker → Creates database sessions to perform CRUD operations.
declarative_base → Used to create database models (tables).
'''