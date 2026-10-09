#Pydantic in Python is a library used for data validation, parsing, and defining structured data models using Python type hints.

from pydantic import BaseModel,EmailStr

class CreateProduct(BaseModel):
    name:str
    price:int
    description:str
    category:str
    stock:int =0


class OrderSchema(BaseModel):
    product_id:int  = None
    count:int = None
    customer_email:EmailStr = None