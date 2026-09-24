import json
file_path = "src/data/products.json"

def get_all_products():
   with open(file_path, "r") as p:
    return json.load(p)



def creat_product(product):
  with open(file_path,"w") as p:
    return json.dump(product,p)