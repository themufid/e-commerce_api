
from pydantic import BaseModel

class ProductSerializer(BaseModel):
    name: str
    description: str
    price: float
    image: str

class PurchaseSerializer(BaseModel):
    product_id: int
    quantity: int
    total_price: float
