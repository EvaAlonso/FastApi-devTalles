# Una lista es una estructura de datos que me ayuda a almacenar más información en una variable
list_numbers = [1, 2, 3, 4, 5]

# Las listas son ordenadas, tienen su índicie (empieza de 0)
# Podemos guardar muchos tipos de datos, y mezclarlos
list_letters = ["a", "b", "c"]
list_mix = ["z", 2, True, [1, 2, 3], 5.5]

shopping_card = ["café", "leche", "pan"]

print(type(list_mix))

# TODO EN PYTHON ES UN OBJETO

# Métodos de las listas

# Append agrega un valor al final de la lista
print(list_numbers)
list_numbers.append(100)

print(list_numbers)

# Remove elimina el valor que le pasamos
list_numbers.remove(4)

# Count me cuenta cuántas veces aparece un valor
print(list_numbers.count(2))

# más métodos .copy copia el valor de una lista
# .sort ordena una lista

# -------------------------------------------------
# ¿Qué es una lista en Python?
# -------------------------------------------------
# Una lista es una colección ordenada y mutable de elementos. Puede contener cualquier tipo de dato y permite duplicados.
# Características:
# - Ordenada: cada elemento tiene un índice.
# - Mutable: se puede modificar (agregar, quitar, cambiar elementos).
# - Permite duplicados y mezcla de tipos de datos.
# - Se define con corchetes: [ ]
#
# -------------------------------------------------
# Métodos principales de las listas
# -------------------------------------------------
# append(x): Agrega un elemento al final
#   ejemplo: lista.append(10)
#
# extend(iterable): Agrega todos los elementos de un iterable al final
#   ejemplo: lista.extend([20, 30])
#
# insert(i, x): Inserta un elemento en la posición indicada
#   ejemplo: lista.insert(1, "a")
#
# remove(x): Elimina la primera aparición de x
#   ejemplo: lista.remove(10)
#
# pop([i]): Elimina y retorna el elemento en la posición i (por defecto el último)
#   ejemplo: lista.pop() o lista.pop(0)
#
# clear(): Elimina todos los elementos de la lista
#   ejemplo: lista.clear()
#
# index(x): Retorna el índice de la primera aparición de x
#   ejemplo: lista.index("a")
#
# count(x): Cuenta cuántas veces aparece x
#   ejemplo: lista.count(2)
#
# sort(): Ordena la lista (por defecto de menor a mayor)
#   ejemplo: lista.sort()
#
# reverse(): Invierte el orden de la lista
#   ejemplo: lista.reverse()
#
# copy(): Retorna una copia superficial de la lista
#   ejemplo: nueva_lista = lista.copy()
#
# Ejemplo usando varios métodos:
#
# numeros = [3, 1, 2]
# numeros.append(4)        # [3, 1, 2, 4]
# numeros.sort()           # [1, 2, 3, 4]
# numeros.reverse()        # [4, 3, 2, 1]
# print(numeros)

# -------------------------------------------------
# Métodos menos comunes de listas
# -------------------------------------------------
#
# del: Elimina uno o varios elementos por índice o por rango
#   ejemplo: del lista[0]  # elimina el primer elemento
#   ejemplo: del lista[1:3]  # elimina elementos en rango
#
# Slicing: Obtener sublistas usando índices
#   ejemplo: sublista = lista[1:4]
#
# List comprehension: Crear listas de forma compacta
#   ejemplo: cuadrados = [x**2 for x in range(5)]
#
# Enumerate: Obtener índice y valor al iterar
#   ejemplo:
#   for i, valor in enumerate(lista):
#       print(i, valor)
#
# -------------------------------------------------
# Casos de uso reales
# -------------------------------------------------
# 1. Filtrar elementos:
#
# edades = [15, 22, 18, 30]
# mayores = [e for e in edades if e >= 18]
# print(mayores)  # [22, 18, 30]
#
# 2. Buscar elementos:
#
# nombres = ["Ana", "Eva", "Luis"]
# if "Eva" in nombres:
#     print("Eva está en la lista")
#
# 3. Eliminar duplicados:
#
# lista = [1, 2, 2, 3]
# lista_sin_duplicados = list(set(lista))
# print(lista_sin_duplicados)  # [1, 2, 3]
#
# 4. Iterar y modificar:
#
# precios = [10, 20, 30]
# precios_con_iva = [p * 1.21 for p in precios]
# print(precios_con_iva)  # [12.1, 24.2, 36.3]
