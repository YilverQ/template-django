from ninja_extra import api_controller, NinjaExtraAPI






##########################
from ninja_extra import api_controller, NinjaExtraAPI
from ninja_extra.crud import NinjaExtraCRUD
from ninja import Router
from typing import List
from apps.products.models import Product
from apps.products.schemas import ProductSchema, CreateProductSchema

api = NinjaExtraAPI()

class ProductCRUD(NinjaExtraCRUD):
    model = Product
    schema = ProductSchema
    create_schema = CreateProductSchema

@api_controller("/products")
class ProductController(ProductCRUD):

    def list(self) -> List[Product]:
        return Product.objects.all()

    def retrieve(self, id: int) -> Product:
        return Product.objects.get(id=id)

    def create(self, payload: CreateProductSchema) -> Product:
        return Product.objects.create(**payload.dict())

    def update(self, id: int, payload: CreateProductSchema) -> Product:
        product = Product.objects.get(id=id)
        for key, value in payload.dict().items():
            setattr(product, key, value)
        product.save()
        return product

    def delete(self, id: int) -> dict:
        product = Product.objects.get(id=id)
        product.delete()
        return {"message": "Deleted successfully"}

    # Ruta personalizada para activar/desactivar producto
    @api.post("/products/{id}/toggle-status")
    def toggle_status(self, id: int) -> Product:
        product = Product.objects.get(id=id)
        product.status = not product.status
        product.save()
        return product

# Registrar controlador
api.add_controller(ProductController)
