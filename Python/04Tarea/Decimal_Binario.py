#Ejercicio deberan de realizar el programa de convertir un número decimal en binario y de binario a decimal
def decimal_binario(decimal):
    binario = ""  
    while decimal > 0:
        res = decimal % 2  
        nuevobinario = str(res)  
        binario = nuevobinario + binario
        decimal = decimal // 2  
    return binario

def binario_decimal(binario):
    decimal = 0
    binario = binario[::-1] 
    for i in range(len(binario)):
        decimal += int(binario[i]) * (2 ** i) 
    return decimal

def menu():
    print("Ingrese la opción a realizar:")
    print("A.- Decimal a Binario")
    print("B.- Binario a Decimal")

menu()
opcion = input("Introduce la opción a desear: \n").upper()

if opcion == "A":
    decimal = int(input("Ingrese el decimal:\n"))
    binario = decimal_binario(decimal)
    print("El número en binario es:", binario)
elif opcion == "B":
    binario = input("Ingrese el número binario:\n")
    decimal = binario_decimal(binario)
    print("El número en decimal es:", decimal)
else:
    print("Opción no válida.")