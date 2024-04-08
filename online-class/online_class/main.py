from fastapi import FastAPI, Depends, HTTPException
from sqlmodel import SQLModel, Field, create_engine, Session, select
from online_class import settings
import psycopg2  # Import psycopg2
from typing import Annotated
from contextlib import asynccontextmanager

# Create Model
class Todo(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    content: str = Field(index=True, min_length=3, max_length=54)
    is_completed: bool = Field(default=False)

# connection string and engine creation
connection_string = str(settings.DATABASE_URL).replace("postgresql", "postgresql+psycopg2")  # Correct replacement
engine = create_engine(connection_string, connect_args={"sslmode": "require"}, pool_recycle=300, echo=True)

# Create tables
def create_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with session(engine) as session:
        yield session


@asynccontextmanager
async def lifespan(app:FastAPI):
    print('creating Tables')
    create_tables()
    print('Tables created')
    yield


app = FastAPI(lifespan=lifespan, title="Todo App", version="1.0.0" )

@app.get("/")
async def read_root():
    return {"Hello": "Welcome to online-class"}


@app.post('/todos', response_model=Todo)
async def create_todo(todo:Todo, session: Annotated[Session,Depends(get_session)]):
    session.add(todo)
    session.commit()
    session.refresh(todo)
    if todo:   
        return todo
    else:
        raise HTTPException (status_code=404, detail= "No Task found")

@app.get('/todos', response_model= list[Todo])
async def get_all(session: Annotated[Session,Depends(get_session)]):
    todos= Session.exec(select(Todo)).all() 
    if todos:   
        return todos
    else:
        raise HTTPException (status_code=404, detail= "No Task found")

@app.get('/todos/{id}', response_model=Todo)
async def get_single_todo(id:int,session: Annotated[Session,Depends(get_session)] ):
    todo = Session.exec(select(Todo)).where(Todo.id==id).first()
    return todo

@app.put('/todos/{id}')
async def edit_todo(todo:Todo, session: Annotated[Session,Depends(get_session)]):
    existing_todo = session.exec(select(Todo)).where (Todo.id==id).first()
    if existing_todo :
        existing_todo.content = todo.content
        existing_todo.is_completed = todo.is_completed 
        session.add(existing_todo)
        session.commit()
        session.refresh(existing_todo)
        return existing_todo
    else:
        raise HTTPException (status_code=404, detail= "No Task found")
        
@app.delete('/todos/{id}')
async def delete_todo(id: int, session: Annotated[Session,Depends(get_session)]): 
    todo = Session.exec(select(Todo)).where(Todo.id==id).first()
    if todo :
        session.delete(todo)
        session.commit()
        session.refresh(todo)
        return {"message": "Task successfuly deleted"}
    else:
        raise HTTPException (status_code=404, detail= "No Task found")








