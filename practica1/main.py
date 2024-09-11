from fastapi import FastAPI
from Routers import Productos, Categorias, Pedidos, Clientes

app = FastAPI()

app.include_router(Productos.router)
app.include_router(Categorias.router)
app.include_router(Pedidos.router)
app.include_router(Clientes.router)