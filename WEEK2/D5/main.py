from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8501"],  
    allow_methods=["*"],
    allow_headers=["*"],
)

# Sample student data 
students_db = [
    {"name": "Alice Wonderland", "class": "Mathematics"},
    {"name": "Bob Builder", "class": "Engineering"},
    {"name": "Charlie Brown", "class": "Arts"},
    {"name": "Diana Prince", "class": "History"},
    {"name": "Ethan Hunt", "class": "Physics"},
]

@app.get("/students")
async def get_students():
    return students_db


#numbers
@app.get("/numbers")
async def get_numbers():
    return list(range(1, 11))

# login user
@app.get("/user")
async def get_user():
        return {
        "name": "Cedric",
        "email": "cedric@gmail.com"
    }