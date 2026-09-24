from fastapi import APIRouter
from src.utils.utils import get_all_products

productRouts = APIRouter() #creating an object/instacne of APIRouter class


@productRouts.get("/") #no routes will be repeated in entire project
def getAllProducts():
    return get_all_products()
@productRouts.post("/create") #no routes will be repeated in entire project
def createNewProduct():
    return { "message": "New product created successfully!"}