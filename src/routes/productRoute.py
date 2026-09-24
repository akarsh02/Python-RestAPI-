from fastapi import APIRouter,HTTPException
from src.utils.utils import get_all_products

productRouts = APIRouter() #creating an object/instacne of APIRouter class


@productRouts.get("/") #no routes will be repeated in entire project
def getAllProducts():
    return get_all_products()

@productRouts.get("/{id}")
def getProducebyId(id):
    allProducts = get_all_products()
    for oneProduct in allProducts:
        if (str(oneProduct['id']) == id):
               return oneProduct
    raise HTTPException(status_code=404, detail={"error": "Product Not Found"})


@productRouts.post("/create") #no routes will be repeated in entire project
def createNewProduct():
    return { "message": "New product created successfully!"}