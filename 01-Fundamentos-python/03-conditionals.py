is_new_dev = False
interest_python = True
knows_python = False

if is_new_dev:
  print("Te recomiendo saber Python.")
elif interest_python:
  print("Aprende en mi curso de fundamentos de python")
else:
  print("Inicia en el mundo de la programación")
  

if knows_python:
  print("Te recomiendo aprender FastApi")

# -----------------------------
# Explicación del código y condicionales en Python
# -----------------------------
# Los condicionales permiten ejecutar diferentes bloques de código según si una condición es verdadera o falsa.
# Se usan las palabras clave: if, elif (else if) y else.
#
# Sintaxis básica:
# if condición:
#     # código si la condición es True
# elif otra_condición:
#     # código si la anterior es False y esta es True
# else:
#     # código si todas las condiciones anteriores son False
#
# En el código anterior:
# - Si is_new_dev es True, imprime una recomendación sobre Python.
# - Si no, pero interest_python es True, recomienda un curso de fundamentos.
# - Si ninguna de las anteriores es True, sugiere iniciar en programación.
# - Luego, si knows_python es True, recomienda aprender FastAPI.
#
# Ejemplo adicional:
#
# edad = 18
# if edad >= 18:
#     print("Eres mayor de edad")
# else:
#     print("Eres menor de edad")
#
# Puedes combinar condiciones con 'and', 'or', y 'not':
#
# if is_new_dev and interest_python:
#     print("¡Bienvenido al mundo Python!")
  