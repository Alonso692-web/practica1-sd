from fastapi import HTTPException, APIRouter
from bson import ObjectId
from DB.db import db
from Schemas.Schemas import Categorias

categorias_collection = db["Categorias"]

router = APIRouter(prefix="/Categorias")

def categoria_helper(categorias) -> dict:
    return{
        "id": str(categorias["_id"]),
        "nombre": categorias["nombre"],
        "descripcion": categorias["descripcion"]
    }

@router.get("/")
async def get_categorias():
    resultados = dict()
    categoria = await categorias_collection.find().to_list(None)
    for i, categorias in enumerate(categoria):
        resultados[i] = dict()
        resultados[i]["nombre"] = categorias["nombre"]
        resultados[i]["descripcion"] = categorias["descripcion"] 
    return resultados

@router.get("/{categorias_id}")
async def get_categorias(categorias_id: str):
    categorias = await categorias_collection.find_one({"_id": ObjectId(categorias_id)})
    if categorias:
        return categoria_helper(categorias)
    raise HTTPException(status_code=404, detail="El id de la categoria no se encontró")

@router.post("/")
async def create_categoria(categorias: Categorias):
    try:
        categoria_dict = categorias.dict()
        resultado = await categorias_collection.insert_one(categoria_dict)
        return {"usuario_id": str(resultado.inserted_id)}
    except Exception as e:
        raise HTTPException(status_code=404, detail="Error al agregar el usuario {e}")

@router.put("/{categorias_id}")
async def update_categoria(categorias_id: str, categorias: Categorias):
    categoria = await categorias_collection.find_one({"_id": ObjectId(categorias_id)})
    if categoria:
        categoria["nombre"] = categorias.nombre
        categoria["descripcion"] = categorias.descripcion
        await categorias_collection.update_one({"_id": ObjectId(categorias_id)}, {"$set": categoria})
        return {"Message": "El usuario se actualizó con exito"}
    raise HTTPException(status_code=404, detail="El usuario no se encontró")

@router.delete("/{categorias_id}")
async def delete_user(categorias_id: str):
    try:
        resultado = await categorias_collection.delete_one({"_id": ObjectId(categorias_id)})
        if resultado.deleted_count == 0:
            return {"message": "Categoria eliminada exitosamente"}
        else:
            raise HTTPException(status_code=404, detail="El id del usuario no se encontró")
    except Exception as e:
        raise HTTPException(status_code=404, detail="id inválido o error en la base de datos")
    