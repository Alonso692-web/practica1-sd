from fastapi import APIRouter, HTTPException
from bson import ObjectId, errors as bson_errors
from pymongo.errors import DuplicateKeyError
from DB.db import db
from Schemas.Schemas import Pedidos

pedidos_collection = db["Pedidos"]

router = APIRouter(prefix="/Pedidos")


# Obtener todos los pedidos
@router.get("/")
async def get_pedidos():
    resultados = []
    pedidos = await pedidos_collection.find().to_list(None)
    for pedido in pedidos:
        pedido["id"] = str(pedido["_id"])
        del pedido["_id"]
        resultados.append(pedido)
    return resultados

# Obtener pedido por ID
@router.get("/{pedido_id}")
async def get_pedido(pedido_id: str):
    try:
        pedido_object_id = ObjectId(pedido_id)
    except bson_errors.InvalidId:
        raise HTTPException(status_code=400, detail="Formato inválido para ID del pedido")

    pedido = await pedidos_collection.find_one({"_id": pedido_object_id})
    
    if pedido is None:
        raise HTTPException(status_code=404, detail="Pedido no encontrado")

    resultado = {
        "fecha": pedido["fecha"],
        "total": pedido["total"],
        "productos": pedido["productos"],
    }
    
    return resultado

# Actualizar pedido
@router.put("/{pedido_id}")
async def put_pedido(pedido_id: str, pedido: Pedidos):
    try:
        pedido_object_id = ObjectId(pedido_id)
    except bson_errors.InvalidId:
        raise HTTPException(status_code=400, detail="Formato inválido para ID del pedido")

    pedido_existente = await pedidos_collection.find_one({"_id": pedido_object_id})
    
    if pedido_existente is None:
        raise HTTPException(status_code=404, detail="Pedido no encontrado")

    pedido_actualizado = pedido.dict(exclude_unset=True)
    pedido_actualizado["_id"] = pedido_object_id

    resultado = await pedidos_collection.update_one({"_id": pedido_object_id}, {"$set": pedido_actualizado})
    
    if resultado.modified_count == 1:
        return {"mensaje": "Pedido actualizado correctamente"}
    else:
        raise HTTPException(status_code=404, detail="Pedido no modificado")
    
# Agregar un nuevo pedido
@router.post("/")
async def create_pedido(pedido: Pedidos):
    
    try:
        resultado = await pedidos_collection.insert_one(pedido.dict())
    except DuplicateKeyError:
        raise HTTPException(status_code=400, detail="El ID del pedido ya existe. No se puede duplicar.")

    if resultado.acknowledged:
        return {"mensaje": "Pedido agregado correctamente"}
    raise HTTPException(status_code=500, detail="Error al insertar el pedido")

# Eliminar pedido
@router.delete("/{pedido_id}")
async def delete_pedido(pedido_id: str):
    try:
        pedido_object_id = ObjectId(pedido_id)
    except bson_errors.InvalidId:
        raise HTTPException(status_code=400, detail="Formato inválido para ID del pedido")

    pedido_existente = await pedidos_collection.find_one({"_id": pedido_object_id})
    
    if pedido_existente is None:
        raise HTTPException(status_code=404, detail="Pedido no encontrado")

    resultado = await pedidos_collection.delete_one({"_id": pedido_object_id})
    
    if resultado.deleted_count == 1:
        return {"mensaje": "Pedido eliminado correctamente"}
    else:
        raise HTTPException(status_code=304, detail="Pedido no eliminado")