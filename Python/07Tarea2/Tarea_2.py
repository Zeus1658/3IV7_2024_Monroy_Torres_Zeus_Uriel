def ingresar_matriz():
    matriz = []
    print("Introduce los valores de la matriz de 3x3")
    for i in range(5):
        fila = []
        for j in range(5):
            valor = float(input(f"Elemento: [{i+1}][{j+1}] : "))
            fila.append(valor)
        matriz.append(fila)
    return matriz

def sumar_matriz(matriz1, matriz2):
    matriz_suma = []
    for i in range(5):
        fila = []
        for j in range(5):
            fila.append(matriz1[i][j] + matriz2[i][j])
        matriz_suma.append(fila)
    return matriz_suma

def imprimir_matriz(matriz):
    for fila in matriz:
        print(fila)

def matriz_transpuesta(matriz1, matriz2):
    matriz_transpuesta = []
    for j in range(5):
        fila = []
        for i in range(5):
            fila.append(matriz1[i][j] + matriz2[i][j])
        matriz_transpuesta.append(fila)
    return matriz_transpuesta

def imprimir_matriz_transpuesta(matriz):
    for fila in matriz:
        print(fila)
        
#Programa principal
print("matriz1: ")
matriz1 = ingresar_matriz()       

print("matriz2: ")
matriz2 = ingresar_matriz()

#La sumo
matriz_resultado = sumar_matriz(matriz1, matriz2)
matriz_res = matriz_transpuesta(matriz1, matriz2)

#Muestro el resultado
print("")
print("El resultado es: ") 
imprimir_matriz(matriz_resultado)
print(" ")
print("La matriz transpuesta es: ")
imprimir_matriz_transpuesta(matriz_res)
