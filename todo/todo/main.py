import os  
from typing import Optional  
from fastapi import Depends, FastAPI, HTTPException  
from sqlalchemy.orm import Session as SQLAlchemySession  # Renamed Session to avoid conflicts
from sqlmodel import Field, SQLModel, create_engine, Session, select

from dotenv import load_dotenv

load_dotenv()

class Todo(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)  
    name: str = Field(index=True)  
    description: str  

class TodoCreate(SQLModel):
    name: str  
    description: str  

class TodoResponse(SQLModel):
    id: int  
    name: str  
    description: str  

conn_str = os.getenv("DATABASE_URL")
engine = create_engine(conn_str)

def get_data() -> SQLAlchemySession:
    with SQLAlchemySession(engine) as session:
        yield session

app = FastAPI(
    title="Todo App",
    description="A simple todo app",
    version="0.1.0"
)

@app.get("/todo")
def get_todo(session: SQLAlchemySession = Depends(get_data)):  # Updated the type hint
    todo = session.exec(select(Todo)).all()
    return todo  

@app.post("/todo/add", response_model=TodoResponse)
def add_todo(todo: TodoCreate, session: SQLAlchemySession = Depends(get_data)):  # Updated the type hint
    todo_add = Todo(**todo.dict())  
    session.add(todo_add)  
    session.commit()  
    session.refresh(todo_add)  
    return todo_add  

@app.delete("/todo/delete/{id}", response_model=TodoResponse)
def delete_todo(id: int, session: SQLAlchemySession = Depends(get_data)):  # Updated the type hint
    todo_delete = session.get(Todo, id)
    session.delete(todo_delete)
    session.commit()
    return todo_delete

@app.put("/todo/update/{id}", response_model=TodoResponse)
def update_todo(id: int, todo_update: TodoCreate, session: SQLAlchemySession = Depends(get_data)):  # Updated the type hint
    todo_to_update = session.get(Todo, id)
    if not todo_to_update:
        raise HTTPException(status_code=404, detail="Todo item not found")

    todo_to_update.name = todo_update.name
    todo_to_update.description = todo_update.description

    session.commit()
    session.refresh(todo_to_update)

    return todo_to_update
