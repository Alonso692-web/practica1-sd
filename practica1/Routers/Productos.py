from fastapi import APIRouter, HTTPException
from bson import ObjectId
from DB.db import db
from Schemas.Schemas import Producto

products_collection = db["Productos"]

router = APIRouter(prefix="/products")


@router.post("/")
async def create_product(producto: Producto):
    result = await products_collection.insert_one(producto.dict())
    if result.acknowledged:
        return {"Message": "Product created successfully"}
    raise HTTPException(status_code = 404, detail="There was a problem")
    


@router.get("/")
async def get_products():
    # Obtener de manera asincrona todos los usuarios
    products = await products_collection.find().to_list(None)
    
    # Convertir _id de ObjectId a str en cada usuario
    products_converted = []
    for product in products:
        product['id'] = str(product['_id'])  # Convertir _id a string y asignarlo a id
        del product['_id']  # Opcional: eliminar el campo original _id
        products_converted.append(product)
    return products_converted

@router.get("/{product_id}")
async def get_products_by_id(product_id:str):
    object_id = ObjectId(product_id)
    product = await products_collection.find_one({'_id': object_id})
    if product:
        resultado = dict()
        resultado["nombre"] = product['nombre']
        resultado["descripcion"] = product["descripcion"]
        resultado["precio"] = product["precio"]
        resultado["stock"] = product["stock"]
        return resultado
    return {"messaje": "User not found"}

@router.put("/{product_id}")
async def update_product(product_id: str, product: Producto):
    # Se actualiza un usuario por su id
    object_id = ObjectId(product_id)
    product_db = await products_collection.find_one({'_id': object_id})
    if product_db:
        product_db['nombre'] = product.nombre
        product_db['descripcion'] = product.descripcion
        product_db['precio'] = product.precio
        product_db['stock'] = product.stock
        await products_collection.update_one({'_id': object_id}, {'$set': product_db})
        return {"Message" : "El producto se actualizó"}
    raise HTTPException(status_code = 404, detail="product not found")

@router.delete("/{product_id}") 
async def delete_product(product_id: str):
    object_id = ObjectId(product_id)
    product = await products_collection.find_one({'_id': object_id})
    if product:
        await products_collection.delete_one({'_id': object_id})
        return {"Message" : "El producto se eliminó"}
    raise HTTPException(status_code = 404, detail="Product not found")
    
