
import math

#Vamos a crear una función para calcular el área y perímetro

def rectangulo(base, altura) :
    area = base * altura
    perimetro = 2 * (base + altura)
    return area, perimetro

def triangulo(base, altura, lado1, lado2, lado3) :
    area = (base * altura)/2
    perimetro = lado1 + lado2 + lado3
    return area, perimetro

def esfera(radio) :
    volumen = (4/3)*math.pi*radio**3
    return volumen

def menu():
    print("Bienvenido a Python con funciones")
    print("Elige una opción: ")
    print("A.- Área y perímetro de un rectángulo")
    print("B.- Área y perímetro de un triángulo")
    print("C.- Volumen de una esfera")


#Programa
menu()
opcion = input("Introduce la opción a desear: ").upper()

if opcion == "A":
    base = float(input("Ingrese la base\n"))
    altura = float(input("Ingrese la atura\n"))
    area, perimetro = rectangulo(base, altura)
    print("El área es de:", area)
    print("El perimetro es de:", perimetro)

elif opcion == "B":
    base = float(input("Ingrese la base\n"))
    altura = float(input("Ingrese la atura\n"))
    lado1 = float(input("Ingrese el lado 1\n"))
    lado2 = float(input("Ingrese el lado 2\n"))
    lado3 = float(input("Ingrese el lado 3\n"))
    area, perimetro = triangulo(base, altura. lado1. lado2, lado3)
    print("El área es de:", area)
    print("El perimetro es de:", perimetro)

elif opcion == "C":
    radio = float(input("Ingrese el radio\n"))
    volumen = esfera(radio)
    print("El volumen es de:", volumen)

else :
    print("Opción no válida")


