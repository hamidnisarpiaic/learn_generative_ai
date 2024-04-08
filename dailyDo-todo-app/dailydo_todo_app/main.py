from fastapi import FastAPI
from sqlmodel import SQLModel, Field, create_engine, Session
from dailydo_todo_app import settings  # Importing settings assuming it's defined elsewhere

app = FastAPI()

# Create Model (There are 2 types of Model: 1. Data Model, 2. Table Model)
# To make one for two, we will add table=True
class Todo(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    content: str = Field(index=True, min_length=3, max_length=54)
    is_completed: bool = Field(default=False)

# Engine is one for the whole application
connection_string: str = str(settings.DATABASE_URL).replace("postgresql", "postgresql+asyncpg")
engine = create_engine(connection_string, connect_args={"sslmode": "require"}, pool_recycle=300, pool_size=10, echo=True)

SQLModel.metadata.create_all(engine)

# In a typical FastAPI application, database operations are usually handled within the route handlers,
# in the context of a request-response cycle. So, consider moving the session usage inside the route handlers.

@app.get("/")
async def root():
    return {"message": "Welcome to dailyDo todo app"}

@app.get("/todo")
async def read_todos():
    # Sample code, replace with actual database query logic
    # Here you should use the session in the context of a request-response cycle
    with Session(engine) as session:
        todos = session.query(Todo).all()
    return {"content": todos}
