from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS middleware setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this to the appropriate origin of your frontend
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/city")
def city():
    return {"city": "Lahore"}

@app.post("/city/{city_name}")
def create_city(city: str):
    return {"city": "Lahore"}
            
