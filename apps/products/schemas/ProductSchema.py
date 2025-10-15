from datetime import datetime
from ninja import Schema
from typing import Optional
from apps.products.models import Product

class ProductSchema(Schema):
    id: int
    name: str
    stocks: int
    price: float
    created_at: datetime
    updated_at: datetime
    status: bool
    bar_code: Optional[str] = None

class CreateProductSchema(Schema):
    name: str
    stocks: int
    price: float
    bar_code: Optional[str] = None
    status: Optional[bool] = True