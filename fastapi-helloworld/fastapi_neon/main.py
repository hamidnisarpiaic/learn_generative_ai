from contextlib import contextmanager
from fastapi import FastAPI, Depends
from sqlmodel import Session, SQLModel, create_engine, select, Field  # Add Field to the import statement
from fastapi_neon.settings import settings  # Import settings from your settings file

class Todo(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    content: str = Field(index=True)

# Use the DATABASE_URL from settings
connection_string = str(settings.DATABASE_URL)

# Create the engine
engine = create_engine(connection_string)

# Function to create tables
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

# Context manager to create tables before app starts
@contextmanager
def lifespan(app: FastAPI):
    print("Creating tables..")
    create_db_and_tables()
    yield

app = FastAPI(
    lifespan=lifespan,
    title="Hello World API with DB",
    version="0.0.1",
    servers=[
        {
            "url": "http://0.0.0.0:8000",  # ADD NGROK URL Here Before Creating GPT Action
            "description": "Development Server",
        }
    ],
)

# Function to get session
def get_session():
    with Session(engine) as session:
        yield session

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/todos/", response_model=Todo)
def create_todo(todo: Todo, session: Session = Depends(get_session)):
    session.add(todo)
    session.commit()
    session.refresh(todo)
    return todo

# Corrected response_model usage
@app.get("/todos/", response_model=list[Optional[Todo]])  # Corrected usage
def read_todos(session: Session = Depends(get_session)):
    todos = session.exec(select(Todo)).all()
    return todos
