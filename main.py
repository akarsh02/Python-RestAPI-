from fastapi import FastAPI
from src.routes.productRoute import productRouts

app = FastAPI() #creating an object/instacne of FastAPI class


@app.get("/")
def home():
    return { "Welcome to the FastAPI application!"}


app.include_router(productRouts,prefix = "/product") #adding the router to the main app