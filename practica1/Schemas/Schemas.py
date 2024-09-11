from pydantic import BaseModel
from datetime import datetime

class Producto(BaseModel):
    nombre: str
    descripcion: str
    precio: float
    stock: int

class Categorias(BaseModel):
    nombre: str
    descripcion: str

class Pedidos(BaseModel):
    fecha: datetime
    total: int
    productos: list = []

class Clientes(BaseModel):
    nombre: str
    apellido: str
    correo_electronico: str