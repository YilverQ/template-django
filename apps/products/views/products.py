from ninja_extra import api_controller, NinjaExtraAPI 
from ninja_extra import http_get, http_post, http_put, http_delete
from typing import List
from django.shortcuts import get_object_or_404
from apps.products.models import Product
from apps.products.schemas.ProductSchema import ProductSchema, CreateProductSchema


@api_controller("/products", tags=["Products"])
class ProductController:
    
    @http_get("", response=List[ProductSchema])
    def list_products(self):
        return Product.objects.all()
    
    @http_get("/{id}", response=ProductSchema)
    def retrieve_product(self, id: int):
        return get_object_or_404(Product, id=id)
    
    @http_post("", response=ProductSchema)
    def create_product(self, payload: CreateProductSchema):
        return Product.objects.create(**payload.dict())
    
    @http_put("/{id}", response=ProductSchema)
    def update_product(self, id: int, payload: CreateProductSchema):
        product = get_object_or_404(Product, id=id)
        for attr, value in payload.dict().items():
            setattr(product, attr, value)
        product.save()
        return product
    
    @http_delete("/{id}")
    def delete_product(self, id: int):
        product = get_object_or_404(Product, id=id)
        product.delete()
        return {"message": "Deleted successfully"}