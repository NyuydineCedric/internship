from fastapi import FastAPI
import streamlit as st
app = FastAPI()

@app.get("/hello")
def hello():
    return "Welcome"

@app.get("/centiment-analysis/{text}")
def centiment_analysis(text):
    status = ["good","bad"]
    if text.lower in status:
        return{
            "Levi": "Good student",
            "Cedric": "Good student"
        }
    else:
        return ({
                "levi":"bad",
                "Cedric":"Not a christian"
                })
#print centiment_analysis("good")
