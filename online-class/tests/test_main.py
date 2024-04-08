# import pytest
# from fastapi.testclient import TestClient
# from online_class import settings
# from sqlmodel import create_engine, Session, SQLModel
# from online_class.main import app, get_session

# # Connection string and engine creation
# connection_string = str(settings.TEST_DATABASE_URL).replace("postgresql", "postgresql+psycopg2")
# engine = create_engine(connection_string, connect_args={"sslmode": "require"}, pool_recycle=300, echo=True)

# # Fixture for handling sessions
# @pytest.fixture(scope="module", autouse=True)
# def get_db_session():
#     SQLModel.metadata.create_all(engine)
#     yield Session(engine)

# @pytest.fixture(scope='function')
# def test_app(get_db_session):
#     def test_session():
#         yield get_db_session
#     app.dependency_overrides[get_session] = test_session
#     with TestClient(app=app) as client:
#         yield client



# # ==================================================================================================


# # Test No.1: Root Test
# def test_root():
#     client = TestClient(app)
#     response = client.get('/')
#     assert response.status_code == 200
#     assert response.json() == {"Hello": "Welcome to online-class"}

# # Test No.2: Create todo Test
# def test_create_todo():
#     SQLModel.metadata.create_all(engine)
#     with Session(engine) as session:
#         def db_session_override():
#             return session
#         app.dependency_overrides[get_session] = db_session_override
#         client = TestClient(app)
#         test_todo = {"content": "create todo list", "is_completed": False}
#         response = client.post('/todos/', json=test_todo)  # Added '/' to '/todos'
#         data = response.json()
#         assert response.status_code == 200
#         assert data["content"] == test_todo["content"]

# # Test No.3: get_all Test
# def test_get_all():
#     # Create tables in the database
#     SQLModel.metadata.create_all(engine)
    
#     # Create a new session
#     with Session(engine) as session:
#         # Define a function to override the session dependency
#         def db_session_override():
#             return session
        
#         # Apply dependency override
#         app.dependency_overrides[get_session] = db_session_override
        
#         # Create a TestClient instance
#         client = TestClient(app)
        
#         # Define the test todo
#         test_todo = {"content": "get all todos test", "is_completed": False}
        
#         # Post a new todo
#         response = client.post('/todos/', json=test_todo)
#         assert response.status_code == 200
        
#     # Now that the session is out of scope, let's create a new session to retrieve the data
#     with Session(engine) as session:
#         # Apply dependency override
#         app.dependency_overrides[get_session] = db_session_override
        
#         # Create a TestClient instance
#         client = TestClient(app)
        
#         # Get all todos
#         response = client.get('/todos/')
#         assert response.status_code == 200
        
#         # Retrieve todos from the response
#         todos = response.json()
        
#         # Assert that the newly added todo is present
#         new_todo = todos[-1]
#         assert new_todo["content"] == test_todo["content"]



# # Test No.4: Single Todo Test
# def test_get_single_todo():
#     SQLModel.metadata.create_all(engine)
#     with Session(engine) as session:
#         def db_session_override():
#             return session
#         app.dependency_overrides[get_session] = db_session_override
#         client = TestClient(app)
#         test_todo = {"content": "get single todo test", "is_completed": False}
#         response = client.post('/todos/', json=test_todo)  # Added '/' to '/todos'
#         todo_id = response.json()["id"]
#         res = client.get(f'/todos/{todo_id}')
#         data = res.json()
#         assert res.status_code == 200
#         assert data["content"] == test_todo["content"]

# # Ensure that the correct syntax is used for the Session object from online_class.main

# # Test No.5: Edit todo
# def test_edit_todo():
#     SQLModel.metadata.create_all(engine)
#     with get_session() as session:  # Use get_session() function to get the session
#         def db_session_override():
#             return session
#         app.dependency_overrides[get_session] = db_session_override
#         client = TestClient(app)
#         test_todo = {"content": "edit todo test", "is_completed": False}
#         response = client.post('/todos/', json=test_todo)  # Added '/' to '/todos'
#         todo_id = response.json()["id"]
#         edited_todo = {"content": "we have edited this", "is_completed": False}
#         response = client.put(f'/todos/{todo_id}', json=edited_todo)  # corrected syntax here
#         data = response.json()
#         assert response.status_code == 200
#         assert data["content"] == edited_todo["content"]

# # Test No.6: Delete todo
# def test_delete_todo():
#     SQLModel.metadata.create_all(engine)
#     with get_session() as session:  # Use get_session() function to get the session
#         def db_session_override():
#             return session
#         app.dependency_overrides[get_session] = db_session_override
#         client = TestClient(app)
#         test_todo = {"content": "delete todo test", "is_completed": False}
#         response = client.post('/todos/', json=test_todo)  # Added '/' to '/todos'
#         todo_id = response.json()["id"]
#         response = client.delete(f'/todos/{todo_id}')  # corrected syntax here
#         data = response.json()
#         assert response.status_code == 200
#         assert data["message"] == "Task successfully deleted"

import pytest
from fastapi.testclient import TestClient
from online_class import settings
from sqlmodel import create_engine, Session, SQLModel
from online_class.main import app, get_session

# Connection string and engine creation
connection_string = str(settings.TEST_DATABASE_URL).replace("postgresql", "postgresql+psycopg2")
engine = create_engine(connection_string, connect_args={"sslmode": "require"}, pool_recycle=300, echo=True)

# Fixture for handling sessions
@pytest.fixture(scope="module", autouse=True)
def get_db_session():
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        yield session

@pytest.fixture(scope='function')
def test_app(get_db_session):
    def test_session():
        with get_db_session as session:
            yield session
    app.dependency_overrides[get_session] = test_session
    with TestClient(app=app) as client:
        yield client


# Test No.1: Root Test
def test_root(test_app):
    client = test_app
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == {"Hello": "Welcome to online-class"}

# Test No.2: Create todo Test
def test_create_todo(test_app):
    client = test_app
    test_todo = {"content": "create todo list", "is_completed": False}
    response = client.post('/todos/', json=test_todo)  # Added '/' to '/todos'
    data = response.json()
    assert response.status_code == 200
    assert data["content"] == test_todo["content"]

## Test No.3: get_all Test
def test_get_all(test_app):
    client = test_app
    # Define the test todo
    test_todo = {"content": "get all todos test", "is_completed": False}
    # Post a new todo
    response = client.post('/todos/', json=test_todo)
    assert response.status_code == 200
    
    # Get all todos
    response = client.get('/todos/')
    assert response.status_code == 200
    
    # Retrieve todos from the response
    todos = response.json()
    
    # Find the newly added todo in the list of todos
    new_todo_found = False
    for todo in todos:
        if todo["content"] == test_todo["content"]:
            new_todo_found = True
            break
    
    # Assert that the newly added todo is present
    assert new_todo_found, "Newly added todo not found in the list of todos"

# Test No.4: Single Todo Test
def test_get_single_todo(test_app):
    client = test_app
    test_todo = {"content": "get single todo test", "is_completed": False}
    response = client.post('/todos/', json=test_todo)  # Added '/' to '/todos'
    todo_id = response.json()["id"]
    res = client.get(f'/todos/{todo_id}')
    data = res.json()
    assert res.status_code == 200
    assert data["content"] == test_todo["content"]

# Test No.5: Edit todo
def test_edit_todo(test_app):
    client = test_app
    test_todo = {"content": "edit todo test", "is_completed": False}
    response = client.post('/todos/', json=test_todo)  # Added '/' to '/todos'
    todo_id = response.json()["id"]
    edited_todo = {"content": "we have edited this", "is_completed": False}
    response = client.put(f'/todos/{todo_id}', json=edited_todo)  # Corrected syntax here
    data = response.json()
    assert response.status_code == 200
    assert data["content"] == edited_todo["content"]

# Test No.6: Delete todo
def test_delete_todo(test_app):
    client = test_app
    test_todo = {"content": "delete todo test", "is_completed": False}
    response = client.post('/todos/', json=test_todo)  # Added '/' to '/todos'
    todo_id = response.json()["id"]
    response = client.delete(f'/todos/{todo_id}')  # corrected syntax here
    data = response.json()
    assert response.status_code == 200
    assert data["message"] == "Task successfully deleted"
