from pydantic import BaseModel

class CreateProduct(BaseModel):
    name:str
    price:int
    description:str
    category:str
    stock:int =0
