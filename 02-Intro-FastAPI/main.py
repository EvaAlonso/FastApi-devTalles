from fastapi import Query
from fastapi import FastAPI, Query

app = FastAPI(title="Mini Blog")

# Creamos una constante con datos para simular BBDD con una lista para tener un endpoint con datos
BLOG_POST = [
    {"id": 1, "title": "Hola, desde FastAPI",
        "Content": "Mi Primer post con FastAPI"},
    {"id": 2, "title": "Mi Segundo post con FastAPI",
     "Content": "Mi Segundo post con FastAPI, blablabla"},
    {"id": 3, "title": "Mi Tercer post con FastAPI",
     "Content": "Mi Tercer post con FastAPI, blablabla"},

]


@app.get("/")
def home():
    return {"mensaje": "Bienvenidos a Mini Blog"}


# @app.get("/posts")  sin query params
# def list_post():
#     return {"data": BLOG_POST}
# PARA QUERYPARAMS
@app.get("/posts")
def list_post(query: str | None = Query(default=None, description="Texto para buscar por título")):
    # como tengo acceso al query agrego el filtro también puedo evaluar si se envía un query
    # creamos una lista, iterando por cada blogpost, leyendo cada uno y agarrando el queryparam lo
    # pasamos a minúscula y lo buscamos en cada título también pasado a minúscula, si encuentra el
    # valor, el queryparam en el título agrega el post en mi lista de resultados y devuelve toda
    # la data con el query. Ej http://127.0.0.1:8000/posts?query=Primer
    # if query:
    #   results = []
    #   for post in BLOG_POST:
    #     if query.lower() in post["title"].lower():
    #       results.append(post)
    #   return {"data": results, "query": query}
    #
    # return {"data": BLOG_POST}
    # Esta forma anterior se puede simplificar con un list comprehension
    if query:
        results = [post for post in BLOG_POST if query.lower()
                   in post["title"].lower()]

        return {"data": results, "query": query}

    return {"data": BLOG_POST}

# PARA PATH PARAMETERS


# @app.get("/posts/{post_id}")
# def get_post(post_id: int):# 
#     # vamos a pasar por todos los post y ver cuál tiene ese id
#     for post in BLOG_POST:
#         if post["id"] == post_id:  # comparo el id del post con el que se pasa por url
#             return {"data": post}
#     return {"error": "Post no encontrado"}

# Path parameters y query params
@app.get("/posts/{post_id}")
def get_post(post_id: int, include_content: bool = Query(default =True, description="Incluir o no el contenido")):
    # vamos a pasar por todos los post y ver cuál tiene ese id
    for post in BLOG_POST:
        if post["id"] == post_id:  # comparo el id del post con el que se pasa por url
          if not include_content: # debo evaluar si tengo ese query parameters
              return {"id": post["id"], "title": post["title"]}
          return {"data": post}
    return {"error": "Post no encontrado"}
""" 
1. @app.get("/posts/{post_id}")

Este decorador indica que la función siguiente responderá a solicitudes GET en la ruta /posts/ seguido de un valor variable (post_id). Ese valor se captura como parámetro de la función.
2. def get_post(post_id: int, include_content: bool = Query(default=True, description="Incluir o no el contenido")):

Se define la función get_post.
post_id: int es un parámetro de tipo entero que se obtiene de la URL (path parameter).
include_content: bool es un parámetro de consulta (query param) que se obtiene de la URL después del signo de interrogación (?), por ejemplo: /posts/1?include_content=False. Por defecto es True.
Query() permite definir validaciones, valores por defecto y descripciones para el parámetro.
3. for post in BLOG_POST:

Se recorre la lista BLOG_POST, que simula una base de datos de posts.
4. if post["id"] == post_id:

Se compara el id de cada post con el valor recibido en la URL. Si coincide, se ejecuta el siguiente bloque.
5. if not include_content:

Si include_content es False, se retorna solo el id y el título del post (sin el contenido).
6. return {"data": post}

Si include_content es True (o no se especifica), se retorna todo el post (id, title y content).
7. return {"error": "Post no encontrado"}

Si no se encuentra ningún post con ese id, se retorna un mensaje de error.
En resumen: este endpoint permite obtener un post por su id y decidir, mediante un query param, si quieres ver solo el id y el título o toda la información del post.
"""
# -------------------------------------------------
# Explicación del código y teoría FastAPI
# -------------------------------------------------
# 1. ¿Qué has hecho en este archivo?
# - Has creado una aplicación web con FastAPI.
# - Definiste una instancia de FastAPI llamada 'app'.
# - Usaste un decorador (@app.get("/")) para crear una ruta que responde a solicitudes GET en '/home'.
# - La función home retorna un diccionario (que FastAPI convierte automáticamente a JSON).
#
# 2. ¿Qué es un decorador en FastAPI?
# - Un decorador es una función especial que "envuelve" otra función para modificar su comportamiento.
# - @app.get("/ruta") indica que la función siguiente responderá a peticiones GET en esa ruta.
#
# 3. ¿Cómo se hace un GET en FastAPI?
# - Usando el decorador @app.get("/ruta").
# - Cuando un usuario accede a esa ruta con el método GET, se ejecuta la función decorada.
#
# 4. ¿Cómo instalar FastAPI ?
# - Ejecuta en la terminal (con el entorno virtual activado):
#     pip install "fastapi[standard]"
#
# 5. ¿Cómo inicializar un proyecto FastAPI?
# - Crea un archivo Python (por ejemplo, main.py) y define la instancia de FastAPI y las rutas como en este archivo.
#
# 6. ¿Cómo levantar el servidor?
# - Ejecuta en la terminal:
#     fastapi dev main.py
# - Esto inicia el servidor en modo desarrollo, recargando cambios automáticamente.
# - Por defecto, estará disponible en http://localhost:8000
#
# 7. ¿Cómo parar el servidor?
# - Ve a la terminal donde está corriendo y presiona Ctrl+C.
#
# 8. Documentación automática:
# - FastAPI genera documentación interactiva en:
#     http://localhost:8000/docs (Swagger UI)
#     http://localhost:8000/redoc (ReDoc)

# -------------------------------------------------
# Sobre el endpoint GET simulando datos y posibilidades
# -------------------------------------------------
# En este archivo has creado un endpoint GET (/posts) que simula datos devolviendo una lista de posts.
# Esto es útil para pruebas, prototipos o cuando aún no tienes una base de datos real.
#
# ¿Qué más podrías hacer con este endpoint?
# - Devolver datos más complejos: listas, diccionarios, objetos, etc.
# - Recibir parámetros en la URL (query o path parameters) para filtrar, buscar o paginar resultados.
# - Validar y documentar los datos de entrada y salida usando Pydantic.
# - Proteger el endpoint con autenticación o permisos.
# - Registrar logs, manejar errores personalizados, etc.
#
# Ejemplo de endpoint GET con parámetros:
#
# @app.get("/posts/{post_id}")
# def get_post(post_id: int):
#     for post in BLOG_POST:
#         if post["id"] == post_id:
#             return {"data": post}
#     return {"error": "Post no encontrado"}
#
# Ejemplo de endpoint GET con parámetros de consulta:
#
# @app.get("/posts/search/")
# def search_posts(title: str = ""):
#     resultados = [p for p in BLOG_POST if title.lower() in p["title"].lower()]
#     return {"data": resultados}

# -------------------------------------------------
# Uso de Path Parameters y diferencia con Query Params
# -------------------------------------------------
# Path parameters (parámetros de ruta) permiten capturar valores directamente en la URL.
# Ejemplo de implementación en FastAPI:
#
# @app.get("/posts/{post_id}")
# def get_post(post_id: int):
#     for post in BLOG_POST:
#         if post["id"] == post_id:
#             return {"data": post}
#     return {"error": "Post no encontrado"}
#
# ¿Cómo se hace la petición en la URL?
# - http://127.0.0.1:8000/posts/1
#   Aquí 1 es el path parameter (post_id).
#
# Diferencia entre query params y path params:
# - Path params: parte de la ruta, obligatorios, identifican recursos concretos (/posts/1).
# - Query params: van después de ?, opcionales, modifican la consulta o el resultado (/posts?query=algo).
#
# -------------------------------------------------
# Ejemplo combinando path y query parameters
# -------------------------------------------------
# Ruta: /posts/{post_id}?include_content=False
# - Si include_content es False, solo muestra id y title.
# - Si no se pasa o es True, muestra todo el post.


# @app.get("/posts/{post_id}")
# def get_post(post_id: int, include_content: bool = Query(True, description="¿Incluir el contenido # del post?")):
#     for post in BLOG_POST:
#         if post["id"] == post_id:
#             if not include_content:
#                 return {"data": {"id": post["id"], "title": post["title"]}}
#             return {"data": post}
#     return {"error": "Post no encontrado"}

# Ejemplo de uso en la URL:
# - http://127.0.0.1:8000/posts/1           # Devuelve id, title y content
# - http://127.0.0.1:8000/posts/1?include_content=False   # Devuelve solo id y title
#
# Más información sobre path y query params:
# https://fastapi.tiangolo.com/es/tutorial/path-params/

# -------------------------------------------------
# Ejemplos de otros tipos de parámetros en FastAPI
# -------------------------------------------------
# 1. Varios parámetros de consulta (query params):
#
# @app.get("/search/")
# def search_posts(query: str = None, author: str = None):
#     # Filtra por título y autor si se proporcionan
#     resultados = [p for p in BLOG_POST if (not query or query.lower() in p["title"].lower()) and (not author or author.lower() in p.get("author", "").lower())]
#     return {"data": resultados}
#
# 2. Parámetros con valores por defecto y validaciones:
#
# from fastapi import Query
#
# @app.get("/items/")
# def get_items(limit: int = Query(10, ge=1, le=100)):
#     # limit debe estar entre 1 y 100
#     return {"limit": limit}
#
# 3. Parámetros opcionales:
#
# from typing import Optional
#
# @app.get("/users/")
# def get_user(name: Optional[str] = None):
#     if name:
#         return {"message": f"Hola, {name}"}
#     return {"message": "Hola, usuario anónimo"}
#
# 4. Parámetros de cabecera (headers):
#
# from fastapi import Header
#
# @app.get("/headers/")
# def read_header(user_agent: str = Header(None)):
#     return {"User-Agent": user_agent}
#
# 5. Parámetros de cookie:
#
# from fastapi import Cookie
#
# @app.get("/cookies/")
# def read_cookie(session_id: str = Cookie(None)):
#     return {"session_id": session_id}
#
# Más información y ejemplos:
# https://fastapi.tiangolo.com/es/tutorial/query-params-str-validations/
# https://fastapi.tiangolo.com/es/tutorial/header-params/
# https://fastapi.tiangolo.com/es/tutorial/cookie-params/
#
# Más información y ejemplos en la documentación oficial:
# https://fastapi.tiangolo.com/es/tutorial/first-steps/

# -------------------------------------------------
# Uso de Query Params y Query() en FastAPI
# -------------------------------------------------
# Para filtrar resultados en un endpoint GET, puedes usar parámetros de consulta (query params).
# Ejemplo de endpoint con filtro por query param:
#
# from fastapi import Query
#
# @app.get("/posts/search")
# def search_posts(query: str = Query(None, min_length=2, max_length=50)):
#     """Filtra los posts cuyo título contenga el texto de 'query' (no sensible a mayúsculas/minúsculas)."""
#     resultados = [p for p in BLOG_POST if query and query.lower() in p["title"].lower()]
#     return {"data": resultados}
#
# ¿Para qué sirve Query()?
# - Permite definir validaciones y metadatos para los parámetros de consulta.
# - Puedes establecer valores por defecto, longitud mínima/máxima, descripciones, etc.
# - Ejemplo: Query(None, min_length=2, max_length=50, description="Texto a buscar en el título")
#
# ¿Cómo se construye la URL?
# - Para buscar posts cuyo título contenga "Primer":
#   http://127.0.0.1:8000/posts/search?query=Primer
# - El parámetro después de ? se llama query param y se pasa como clave=valor.
#
# ¿Por qué usamos list comprehension?
# - Es una forma compacta y eficiente de crear listas a partir de otra lista aplicando una condición o transformación.
# - En el ejemplo:
#   resultados = [p for p in BLOG_POST if query and query.lower() in p["title"].lower()]
#   Esto filtra todos los posts cuyo título contiene el texto buscado.
#
# ¿Qué es list comprehension?
# - Es una sintaxis de Python para crear listas de manera concisa.
# - Ejemplo básico:
#   cuadrados = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]
# - Se usa para filtrar, transformar o construir listas de forma eficiente y legible.
#
# Más información sobre query params y validaciones:
# https://fastapi.tiangolo.com/es/tutorial/query-params/
