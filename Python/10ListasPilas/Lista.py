#Una lista muy parecido a un arreglo solo que es una estructura más versátil la cual puede manejar enteros, flotantes, cadenas, caracteres, etc.

#Vamos a crear una lista de estudiantes

estudiantes = ["Ana", "Hugo", "Paco", "Luis"]

#Métodos propios append(x) = Agregar un elemento al final, insert(i, x) = Inserta un elemento en una posición específica, remove(x) = Remover un elemento en específico

#Agregar uno
estudiantes.append("Diana")
print("Lista de estudiantes ", estudiantes)

#Eliminar a uno
estudiantes.remove("Hugo")
print("Lista de Estudiantes: ", estudiantes)