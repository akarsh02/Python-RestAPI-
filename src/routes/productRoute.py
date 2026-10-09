from fastapi import APIRouter,HTTPException
from src.utils.utils import get_all_products,creat_product,simple_send
from src.dtos.productSchema import CreateProduct,OrderSchema


productRouts = APIRouter() #creating an object/instacne of APIRouter class


@productRouts.get("/") #no routes will be repeated in entire project
def getAllProducts():
    return get_all_products()


@productRouts.get('/check')
def getProductByQuery(id = None):
    allProducts = get_all_products()
    for oneProduct in allProducts:
           if (str(oneProduct['id']) == id):
                  return oneProduct
    raise HTTPException(status_code=404, detail={"error": "Product Not Found using query"})

@productRouts.get("/{id}")
def getOneProducebyId(id):
    allProducts = get_all_products()
    for oneProduct in allProducts:
        if (str(oneProduct['id']) == id):
               return oneProduct
    raise HTTPException(status_code=404, detail={"error": "Product Not Found"})




@productRouts.post("/create") #no routes will be repeated in entire project
def createNewProduct(product:CreateProduct):
    products = get_all_products()
    product = product.model_dump() #converts to dict formate
    next_id = max([p["id"] for p in products]) + 1 # for creating next id
    product['id'] = next_id
    products.append(product)
    creat_product(products)
    return {"message":"New Product Created "}

@productRouts.put("/update/{id}") #no routes will be repeated in entire project
def updateProduct(product: CreateProduct, id: int):
    allProducts = get_all_products()
    for index, existingProduct in enumerate(allProducts):
        if existingProduct["id"] == id:
            allProducts[index] = {"id": id, **product.model_dump()}
            creat_product(allProducts)
            return {"message": "Product Updated Successfully"}

    raise HTTPException(status_code=404, detail={"error": "Product Not Found"})

@productRouts.delete("/delete/{id}") #no routes will be repeated in entire project
def deleteProduct(id: int):
    allProducts = get_all_products()
    for p in allProducts:
        if p["id"] == id:
            allProducts.remove(p)
            creat_product(allProducts)
            return {"message": "Product Deleted Successfully"}

    raise HTTPException(status_code=404, detail={"error": "Product Not Found"})



## sending and email
## data -product-id,count,customer-email
@productRouts.post("/placeOrder") #no routes will be repeated in entire project
async def placeOrder(Order: OrderSchema):
    allProducts = get_all_products()
    count = Order.count
    product_id = Order.product_id
    customer_email = Order.customer_email
    print("customer_email",customer_email)
    oneProduct = None
    for p in allProducts:
        if p["id"] == product_id:
            oneProduct = p
            break
    if not oneProduct:
        raise HTTPException(status_code=404, detail={"error": "Product Not Found"})
    if oneProduct["stock"] < count:
        raise HTTPException(status_code=400, detail={"error": "Insufficient stock"})
    await simple_send(customer_email, count)
    return {"message": "Order Placed Successfully"}