
from fastapi import FastAPI
from models import Product
app=FastAPI()

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
   return products

greet()
get_products()