from fastapi import APIRouter, HTTPException
# Para crear la estructura de los datos
from pydantic import BaseModel
from bson import ObjectId

from Schemas.Schemas import Clientes
from DB.db import db
clientes_collection = db["Clientes"]

# Objeto para interactuar con la API
router = APIRouter()

# Crear endpoint (ruta,url) para obtener los usuarios de la base de datos
@router.get("/clientes")
async def get_clientes():
    # Obtener de manera asincrona todos los usuarios
    resultados = dict() # todos los usuarios
    clientes = await clientes_collection.find().to_list(None)
    # Iterar todos los elementos de la lista clientes
    for i, cliente in enumerate(clientes):
        # Diccionario por cada usuario
        resultados[i] = dict()
        resultados[i]["nombre"] = cliente["nombre"]
        resultados[i]["apellido"] = cliente["apellido"]
        resultados[i]["correo_electronico"] = cliente["correo_electronico"]
    return resultados 

@router.post("/clientes")
async def create_clientes(clientes:Clientes):
    # Se agrega un usuario a la base de datos
    # Los datos del usuario deben estar en diccionario
    await clientes_collection.insert_one(clientes.dict())
    return{
        "message":  "El cliente se agrego correctamente"
    }
    
# Función para buscar usuarios por ID
@router.get("/clientes/{clientes_id}")
async def get_clientes_by_id(clientes_id: str):
    # Convertir el ID a ObjectId si es necesario
    clientes = await clientes_collection.find_one({"_id": ObjectId(clientes_id)})
    
    # Si el usuario no existe, lanzamos una excepción
    if not clientes:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    
    # Retornamos los datos del usuario encontrado
    return {
        "nombre": clientes["nombre"],
        "apellido": clientes["apellido"],
        "correo_electronico": clientes["correo_electronico"]
    }
    
# Función para eliminar usuarios por ID
@router.delete("/clientes/{clientes_id}")
async def delete_clientes_by_id(clientes_id: str):
    # Intentar eliminar el cliente
    try: 
        resultado = await clientes_collection.delete_one({"_id": ObjectId(clientes_id)})
    except Exception as e:
        raise HTTPException(status_code=404, detail="Formato invalido para el ID del cliente")
    # Si no se eliminó ningún documento, significa que no se encontró el usuario
    if resultado.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    
    return {"message": "Cliente eliminado correctamente"}

@router.put("/clientes/{clientes_id}")
async def update_clientes(clientes_id: str, clientes: Clientes):
    try: 
        clientes_object_id = ObjectId(clientes_id)
    except Exception as e:
        raise HTTPException(status_code=400, datail="Formato invalido para ID del cliente")
    
    db_clientes = await clientes_collection.find_one({"_id": clientes_object_id})
    
    if db_clientes:
        db_clientes["nombre"] = clientes.nombre
        db_clientes["apellido"] = clientes.apellido
        db_clientes["correo_electronico"] = clientes.correo_electronico
        
        await clientes_collection.update_one({"_id": clientes_object_id}, {"$set":db_clientes})
        
        return{
            "message": "Usuario actualizado con éxito"
        }
        
    raise HTTPException(status_code=404, detail="Cliente NO actualizado")