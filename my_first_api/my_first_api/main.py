# Import the FastAPI class from the fastapi module
from fastapi import FastAPI

# Create an instance of the FastAPI class
app = FastAPI()

# Define route handlers for various endpoints
@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/city")
def city():
    return {"city": "Islamabad"}

@app.get("/country")
def country():
    return {"country": "Pakistan"}
