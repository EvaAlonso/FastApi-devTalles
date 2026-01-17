# AND necesita que todo sea True
age = 25
license = True

if age >= 18 and license:
    print("Puedes conducir")

# OR funciona con que una de las condiciones sea verdadera
is_student = False
membership = True

if is_student or membership:
    print("Obtiene precio especial")

# NOT es una negación
is_admin = False
if not is_admin:
    print("Acceso denegado")

# Short Circuiting si no le mando algún nombre me puede dar un error, hay que evaluar que el nombre exista
name = False
print(name and name.upper())

# -----------------------------
# Explicación de operadores lógicos en Python
# -----------------------------
# Los operadores lógicos permiten combinar condiciones:
#
# 1. and: Devuelve True si ambas condiciones son verdaderas.
#    Ejemplo:
#    a = True
#    b = False
#    print(a and b)  # False
#
# 2. or: Devuelve True si al menos una condición es verdadera.
#    Ejemplo:
#    a = True
#    b = False
#    print(a or b)  # True
#
# 3. not: Niega el valor de una condición (True -> False, False -> True).
#    Ejemplo:
#    a = True
#    print(not a)  # False
#
# Ejemplo encadenando varios operadores:
# edad = 20
# tiene_licencia = True
# es_estudiante = False
#
# if (edad >= 18 and tiene_licencia) or es_estudiante:
#     print("Puedes conducir o eres estudiante")
#
# if not (edad < 18 or not tiene_licencia):
#     print("Eres mayor de edad y tienes licencia")
#
# Puedes usar paréntesis para agrupar condiciones y controlar la prioridad.

# -----------------------------------
# Short Circuiting (Evaluación corta)
# -----------------------------------
# En Python, los operadores lógicos 'and' y 'or' realizan "short circuiting":
#
# - Con 'and', si la primera condición es False, no evalúa la segunda.
# - Con 'or', si la primera condición es True, no evalúa la segunda.
#
# Esto es útil para evitar errores o ahorrar recursos.
#
# Ejemplo con 'and':
#
# nombre = None
# resultado = nombre and nombre.upper()  # No da error, porque si nombre es None o False, no se ejecuta .upper()
# print(resultado)  # Imprime None
#
# Ejemplo con 'or':
#
# usuario = "Eva"
# print(usuario or "Invitado")  # Imprime 'Eva' porque usuario es True
#
# usuario = ""
# print(usuario or "Invitado")  # Imprime 'Invitado' porque usuario es cadena vacía (False)
#
# Short circuiting permite escribir código más seguro y eficiente, evitando llamadas innecesarias o errores por valores nulos.
