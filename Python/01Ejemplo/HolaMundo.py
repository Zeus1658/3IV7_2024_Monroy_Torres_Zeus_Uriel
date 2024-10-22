#esto es un comentario

#vamos a definir una variable
x = 17.89
print(x)

#Ejemplo de if una condición
valores = int(input("Ingrese un valor \n"))

if valores < 0 :
    #Cuando sea verdad
    print("Es menor que 0")
elif valores > 0 :
    print("Es mayor que 0")
else:
    print("Es 0")

#Bucles
numero = 0
print("Tabla del 2")
while numero <= 10 :
    print("Resultado :", 2*numero)
    print("Antes",numero)
    numero += 1
    print("Después",numero)

#Bucle for
numero = [3, 7, 5, 8]

for i in numero :
    print(i)
