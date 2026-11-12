
from fastapi import FastAPI
from models import Product
from database import session,engine
import database_models

app=FastAPI()

database_models.Base.metadata.create_all(bind=engine)

@app.get("/")
def greet():
   return "Welcome ......."

products = [
    Product(
        id=1,
        name="Phone",
        description="The iPhone",
        price=45678,
        quantity=34
    ),
    Product(
        id=2,
        name="Laptop",
        description="MacBook Air",
        price=85000,
        quantity=20
    ),
    Product(
        id=3,
        name="Headphones",
        description="Wireless headphones",
        price=2500,
        quantity=50
    ),
    Product(
        id=4,
        name="Keyboard",
        description="Mechanical keyboard",
        price=3500,
        quantity=15
    ),
    Product(
        id=5,
        name="Mouse",
        description="Wireless mouse",
        price=1200,
        quantity=40
    )
]
@app.get("/products")
def get_products():
   db=session()
   db.query()
   return products

@app.get("/product/{id}")
def get_product_by_id(id:int):
   for product in products:
      if product.id==id:
         return product
      
   
   return "prodcut Not FOund Please try Exisitng products"

@app.post("/product/create")
def add_product(product: Product):
   products.append(product)
   return "The Product is added sucessfully"

@app.put("/productUpdate")
def upadte_the_product(id:int,product:Product):
   for i in range(len(products)):
      if products[i].id==id:
         products[i]=product
      return "product is updated Successfully"
   return "product not found"

@app.delete("/product/delete/{id}")
def delete_the_product(id:int):
   for i in range(len(products)):
      del products[i]
      return "Product Is Deleted Succesfully"
   return "Product is not found"

      

