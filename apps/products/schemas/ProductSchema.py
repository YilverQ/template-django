from ninja import ModelSchema, Schema
from typing import Optional
from apps.products.models import Product

class ProductScheme(ModelSchema):
    class Config:
        model = Product
        fields = ['id', 'name', 'stocks', 'price', 'created_at', 'updated_at', 'status', 'bar_code']


class CreateProductScheme(Schema):
    name: str
    stocks: int
    price: float
    bar_code: Optional[str] = None
    status: Optional[bool] = True