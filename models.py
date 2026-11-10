from pydantic import BaseModel
class Product(BaseModel):
    id:int
    name:str
    description:str
    price:float
    quantity:int
#no need of initaialixzation of contsructor beacuse we are inheritinn from BaseModel it will add validation like which shoudl npt be null
    # def __init__(self,id,name,description,price,quantity):
    #     self.id=id
    #     self.name=name
    #     self.description=description
    #     self.price=price
    #     self.quantity=quantity