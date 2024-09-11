# Conexion con MongoDB
from motor import motor_asyncio

# Configurar la conexión con MongoDB
MONGO_URI = "mongodb://localhost:27017"

# Ejecutar el cliente de base dedatos
client = motor_asyncio.AsyncIOMotorClient(MONGO_URI)

db = client["practica1_sd"]