# Diccionarios son también estructuras de datos que nos ayudan a guardar información
# pero en el caso de los diccionarios no lo hace de forma ordenada sino con un formato clave valor


user = {
    "nombre": "Eva",
    "edad": 50,
    "email": "eva@email.com",
    "active": True,
    (19.12, -98.32): "Cancún México" #Tupla
}

print(user)

#si quiero cambiar una llave, podemos hacerlo porque es mutable
user["nombre"] = "Sonia"

# Para imprimir cada una de las llaves
print(user[(19.12, -98.32)])

# -------------------------------------------------
# ¿Qué es un diccionario en Python?
# -------------------------------------------------
# Un diccionario es una colección de pares clave-valor, donde cada clave es única.
# Características:
# - No ordenado (en versiones modernas sí mantiene orden de inserción, pero no se debe depender de ello para lógica).
# - Mutable: se puede modificar, agregar o eliminar elementos.
# - Las claves deben ser inmutables (str, int, tuple, etc.).
# - Se define con llaves: { }
#
# -------------------------------------------------
# Métodos principales de los diccionarios
# -------------------------------------------------
# keys(): Devuelve una vista de todas las claves
#   ejemplo: user.keys()
#
# values(): Devuelve una vista de todos los valores
#   ejemplo: user.values()
#
# items(): Devuelve una vista de pares (clave, valor)
#   ejemplo: user.items()
#
# get(clave, valor_por_defecto): Devuelve el valor de la clave o el valor por defecto si no existe
#   ejemplo: user.get("edad", 0)
#
# pop(clave): Elimina la clave y devuelve su valor
#   ejemplo: user.pop("email")
#
# popitem(): Elimina y devuelve el último par insertado
#   ejemplo: user.popitem()
#
# update(otro_diccionario): Actualiza el diccionario con otro
#   ejemplo: user.update({"ciudad": "Madrid"})
#
# clear(): Elimina todos los elementos
#   ejemplo: user.clear()
#
# setdefault(clave, valor): Devuelve el valor de la clave, si no existe la crea con ese valor
#   ejemplo: user.setdefault("pais", "España")
#
# fromkeys(iterable, valor): Crea un nuevo diccionario con claves de un iterable y el mismo valor
#   ejemplo: dict.fromkeys(["a", "b"], 0)
#
# copy(): Devuelve una copia superficial del diccionario
#   ejemplo: copia = user.copy()
#
# -------------------------------------------------
# Ejemplos de uso en la vida real
# -------------------------------------------------
# 1. Almacenar información de un usuario:
# usuario = {"nombre": "Ana", "edad": 30, "email": "ana@email.com"}
#
# 2. Contar ocurrencias de palabras:
# texto = "hola mundo hola"
# contador = {}
# for palabra in texto.split():
#     contador[palabra] = contador.get(palabra, 0) + 1
# print(contador)  # {'hola': 2, 'mundo': 1}
#
# 3. Relacionar claves con listas u otros diccionarios:
# agenda = {"Eva": ["1234", "5678"], "Luis": ["9999"]}
#
# 4. Iterar sobre claves y valores:
# for clave, valor in usuario.items():
#     print(clave, valor)
#
# 5. Diccionarios anidados:
# alumnos = {"Eva": {"edad": 25, "notas": [9, 8, 10]}, "Luis": {"edad": 22, "notas": [7, 6, 8]}}

# -------------------------------------------------
# Acceso seguro a claves
# -------------------------------------------------
# Usar get() para evitar errores si la clave no existe:
# usuario = {"nombre": "Ana"}
# print(usuario.get("edad", "No especificada"))  # 'No especificada'
#
# Comprobar si una clave existe:
# if "email" in usuario:
#     print(usuario["email"])
# else:
#     print("No hay email")
#
# -------------------------------------------------
# Combinar diccionarios
# -------------------------------------------------
# Usando update():
#
# d1 = {"a": 1, "b": 2}
# d2 = {"b": 3, "c": 4}
# d1.update(d2)
# print(d1)  # {'a': 1, 'b': 3, 'c': 4}
#
# Usando el operador | (Python 3.9+):
#
# d3 = {"x": 10}
# d4 = {"y": 20}
# combinado = d3 | d4
# print(combinado)  # {'x': 10, 'y': 20}

# -------------------------------------------------
# Recorrer diccionarios anidados
# -------------------------------------------------
# alumnos = {
#     "Eva": {"edad": 25, "notas": [9, 8, 10]},
#     "Luis": {"edad": 22, "notas": [7, 6, 8]}
# }
# for nombre, datos in alumnos.items():
#     print(f"Alumno: {nombre}")
#     for clave, valor in datos.items():
#         print(f"  {clave}: {valor}")
#
# -------------------------------------------------
# Operaciones avanzadas
# -------------------------------------------------
# 1. Crear un diccionario a partir de dos listas:
#
# claves = ["a", "b", "c"]
# valores = [1, 2, 3]
# dicc = dict(zip(claves, valores))
# print(dicc)  # {'a': 1, 'b': 2, 'c': 3}
#
# 2. Diccionarios por comprensión:
#
# cuadrados = {x: x**2 for x in range(5)}
# print(cuadrados)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# -------------------------------------------------
# Buscar valores en diccionarios anidados
# -------------------------------------------------
# alumnos = {
#     "Eva": {"edad": 25, "notas": [9, 8, 10]},
#     "Luis": {"edad": 22, "notas": [7, 6, 8]}
# }
#
# # Buscar la nota máxima de cada alumno
# for nombre, datos in alumnos.items():
#     nota_max = max(datos["notas"])
#     print(f"Nota máxima de {nombre}: {nota_max}")
#
# # Buscar si algún alumno tiene una nota de 10
# for nombre, datos in alumnos.items():
#     if 10 in datos["notas"]:
#         print(f"{nombre} tiene al menos un 10")

# -------------------------------------------------
# Modificar valores en diccionarios anidados
# -------------------------------------------------
# alumnos = {
#     "Eva": {"edad": 25, "notas": [9, 8, 10]},
#     "Luis": {"edad": 22, "notas": [7, 6, 8]}
# }
#
# # Cambiar la edad de Eva
# alumnos["Eva"]["edad"] = 26
# print(alumnos["Eva"])
#
# # Agregar una nueva nota a Luis
# alumnos["Luis"]["notas"].append(9)
# print(alumnos["Luis"])

# -------------------------------------------------
# Eliminar elementos condicionalmente en diccionarios anidados
# -------------------------------------------------
# alumnos = {
#     "Eva": {"edad": 26, "notas": [9, 10]},
#     "Luis": {"edad": 22, "notas": []},
# }
#
# # Eliminar alumnos sin notas
# alumnos = {nombre: datos for nombre, datos in alumnos.items() if datos["notas"]}
# print(alumnos)  # Solo quedan los alumnos con lista de notas no vacía
#
# # Eliminar todas las notas menores de 9 de todos los alumnos
# for datos in alumnos.values():
#     datos["notas"] = [n for n in datos["notas"] if n >= 9]
# print(alumnos)

# -------------------------------------------------
# Convertir diccionarios a otros formatos
# -------------------------------------------------
# 1. A JSON (texto):
# import json
# usuario = {"nombre": "Ana", "edad": 30}
# usuario_json = json.dumps(usuario)
# print(usuario_json)  # '{"nombre": "Ana", "edad": 30}'
#
# 2. De JSON a diccionario:
# usuario_dict = json.loads(usuario_json)
# print(usuario_dict)  # {'nombre': 'Ana', 'edad': 30}
#
# 3. A listas de claves y valores:
# claves = list(usuario.keys())
# valores = list(usuario.values())
# print(claves)   # ['nombre', 'edad']
# print(valores)  # ['Ana', 30]
#
# 4. A lista de tuplas (pares clave-valor):
# items = list(usuario.items())
# print(items)  # [('nombre', 'Ana'), ('edad', 30)]
#
# # Añadir un nuevo alumno
# alumnos["Ana"] = {"edad": 20, "notas": [8, 9]}
# print(alumnos)

# -------------------------------------------------
# Eliminar claves o valores en diccionarios anidados
# -------------------------------------------------
# alumnos = {
#     "Eva": {"edad": 26, "notas": [9, 8, 10]},
#     "Luis": {"edad": 22, "notas": [7, 6, 8, 9]},
#     "Ana": {"edad": 20, "notas": [8, 9]}
# }
#
# # Eliminar una nota de Eva (por valor)
# alumnos["Eva"]["notas"].remove(8)
# print(alumnos["Eva"])
#
# # Eliminar la clave 'Ana' completamente
# alumnos.pop("Ana")
# print(alumnos)
#
# # Eliminar todas las notas de Luis
# alumnos["Luis"]["notas"].clear()
# print(alumnos["Luis"])
