# from sqlalchemy import Column, Integer, String
# from sqlalchemy.ext.declarative import declarative_base

# Base = declarative_base()

# class Todo(Base):
#     __tablename__ = "todo"

#     id = Column(Integer, primary_key=True)
#     name = Column(String)
#     description = Column(String)


# Import necessary components from SQLAlchemy
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Create a base class for SQLAlchemy models
Base = declarative_base()

# Define a class representing a table named "todo"
class Todo(Base):
    # Define the name of the table
    __tablename__ = "todo"

    # Define columns for the table
    id = Column(Integer, primary_key=True)  # Primary key column
    name = Column(String)  # Column for storing name data
    description = Column(String)  # Column for storing description data
