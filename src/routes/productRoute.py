from fastapi import APIRouter


productRouts = APIRouter() #creating an object/instacne of APIRouter class


@productRouts.get("/products") #no routes will be repeated in entire project
def getAllProducts():
    return []

