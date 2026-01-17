from fastapi import FastAPI, Query, Body, HTTPException

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

# MÉTODO POST
@app.post("/posts")
def create_post(post: dict = Body(...)): 
  # validemos si tenemos un título y contenido en el post
  if "title" not in post or "content" not in post:
    return {"error": "Title y Content son requeridos"}
  if not str(post["title"]).strip(): # mandar el título sin espacios y ver si el título tiene algo
    return {"error": "Title no puede estar vacío"}
  # como todavía no tenemos BBDD simulanos un aumento del id
  new_id = (BLOG_POST[-1]["id"]+1) if BLOG_POST else 1
  # creo nuevo post por el body de la petición y lo añando a laso post
  new_post = {"id": new_id, "title": post["title"], "content": post["content"]}
  BLOG_POST.append(new_post)
  return {"message": "Post creado", "data": new_post}
# pasamos parámetro para recibir información desde el body podemos poner Body(None) opcional
# o usar elipsis para especificar que aún no hay parámetros, contenido pero es obligatorio
# RESUMEN
# Definimos la ruta que en este caso es post y una vez llamada con el método post, se ejecuta la
# función create_post y le pasamos un diccionario en un Body en este caso obligatorio
# evaluamos si tenemos title y content en post, si no están mandamos error
# En caso title pero vacío también error avisando title no puede estar vacío
# aumento automáticon nuevo id y creamos un diccionario nuevo post y lo agregamos 
# a la lista blog post y añadimos mensaje de post creado

# MÉTODO PUT
@app.put("/posts/{post_id}") # como quiero actualizar un post le tengo que pasar el id de ese post
def update_post(post_id: int, data: dict = Body(...)): # recuerda elipsis obligatorio pasar body
  # lo primero que hago es buscar ese post, itero sobre todo los post
  for post in BLOG_POST:
    if post["id"] == post_id:
      if "title" in data: post["title"] = data["title"]
      if "content" in data: post["content"] = data["content"]
      return {"message": "Post actualizado", "data": post}
    
 # return {"error": "No se encontró el post"} si el error lo retorno así me da siempre un 200
 # pero debería ser un 401 si por ejemplo pido post que no existe para eso uso httpexception
 # ver más info en main.md
  raise HTTPException(status_code=404, detail="Post no encontrado")