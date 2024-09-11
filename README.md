# API para Gestión de Tienda en Línea

Esta API RESTful permite gestionar los datos de una tienda en línea utilizando MongoDB. La API proporciona operaciones CRUD (Crear, Leer, Actualizar, Eliminar) para varias colecciones dentro de la base de datos, como productos, usuarios, pedidos y categorías.

## Tecnologías Utilizadas

- **Python**: Para la implementación la API RESTful.
- **MongoDB**: Base de datos NoSQL para el almacenamiento de datos.

## Estructura de las Colecciones en MongoDB

### 1. **Productos**

Almacena la información sobre los productos disponibles en la tienda.

```json
{
  "id (ObjectId)": "identificador único del producto",
  "nombre (String)": "nombre del producto",
  "descripción (String)": "descripción del producto",
  "precio (Number)": "precio del producto",
  "stock (Number)": "cantidad de unidades en stock"
}
```

### 2. **Usuarios**
Gestiona la información de los usuarios registrados en la tienda.

```json
{
  "_id": "ObjectId",
  "nombre": "Nombre del usuario",
  "email": "usuario@example.com",
  "password": "hashed_password",
  "direccion": "Dirección del usuario"
}
```

### **3. Pedidos**
Rastrea los pedidos realizados por los usuarios.

```json
{
  "id (ObjectId)": "identificador único del pedido"
  "fecha (Date)": "fecha en que se realizó el pedido",
  "total (Number)": "total del pedido",
  "productos (Array)": "arreglo de productos incluidos en el pedido"
}
```

### **4. Categorías**
Organiza los productos en diferentes categorías.

```json
{
  "id (ObjectId)": "identificador único de la categoría",
  "nombre (String)": "nombre de la categoría",
  "descripci´on (String)": "descripción de la categoría"

}
```

## Endpoints de la API

La API proporciona los siguientes endpoints para interactuar con cada colección:

### **Productos**

- **`GET /productos`**: Obtiene todos los productos.
- **`GET /productos/:id`**: Obtiene un producto por ID.
- **`POST /productos`**: Crea un nuevo producto.
- **`PUT /productos/:id`**: Actualiza un producto por ID.
- **`DELETE /productos/:id`**: Elimina un producto por ID.

### **Usuarios**

- **`GET /usuarios`**: Obtiene todos los usuarios.
- **`GET /usuarios/:id`**: Obtiene un usuario por ID.
- **`POST /usuarios`**: Crea un nuevo usuario.
- **`PUT /usuarios/:id`**: Actualiza un usuario por ID.
- **`DELETE /usuarios/:id`**: Elimina un usuario por ID.

### **Pedidos**

- **`GET /pedidos`**: Obtiene todos los pedidos.
- **`GET /pedidos/:id`**: Obtiene un pedido por ID.
- **`POST /pedidos`**: Crea un nuevo pedido.
- **`PUT /pedidos/:id`**: Actualiza un pedido por ID.
- **`DELETE /pedidos/:id`**: Elimina un pedido por ID.

### **Categorías**

- **`GET /categorias`**: Obtiene todas las categorías.
- **`GET /categorias/:id`**: Obtiene una categoría por ID.
- **`POST /categorias`**: Crea una nueva categoría.
- **`PUT /categorias/:id`**: Actualiza una categoría por ID.
- **`DELETE /categorias/:id`**: Elimina una categoría por ID.


## Instalación

Sigue estos pasos para configurar y ejecutar el proyecto localmente:
# Exportación de Base de Datos MongoDB

Este repositorio contiene una copia exportada de la base de datos `practica1_sd`. Sigue los pasos a continuación para importar y utilizar la base de datos en tu entorno local.

## Contenido del Repositorio

- `backup/`: Carpeta que contiene la base de datos exportada en formato BSON, generada con `mongodump`.

## Requisitos Previos

Asegúrate de tener los siguientes requisitos instalados:

- **MongoDB**: Asegúrate de tener MongoDB instalado en tu sistema. Puedes descargarlo desde [MongoDB Download Center](https://www.mongodb.com/try/download/community).
- **MongoDB Tools**: Las herramientas de MongoDB (como `mongorestore`) deben estar disponibles en tu PATH. Si no las tienes, instálalas desde [MongoDB Database Tools](https://www.mongodb.com/try/download/database-tools).

## Instrucciones para Importar la Base de Datos

1. **Clonar el Repositorio:**

   Clona este repositorio en tu máquina local:

   ```bash
   git clone https://github.com/usuario/nuevo-repositorio.git
   cd nuevo-repositorio
   ```
2. **Importar la Base de Datos:**

Usa `mongorestore` para importar la base de datos desde la carpeta `backup`:

```bash
mongorestore --db practica1_sd --drop ./backup/practica1_sd
```


## Contribuciones
Las contribuciones son bienvenidas. Por favor, crea un "issue" para reportar errores o sugerir mejoras, y envía un "pull request" con los cambios.

## Licencia
Este proyecto está bajo la licencia MIT. Consulta el archivo LICENSE para más detalles.

Este archivo `README.md` proporciona una descripción clara y detallada de la implementación de tu API y las colecciones en MongoDB. Puedes ajustarlo según la estructura y detalles específicos de tu implementación.


