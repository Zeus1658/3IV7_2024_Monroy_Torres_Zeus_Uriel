Algoritmo Conversion_Unidades
	Definir m, resultado, c Como Real
	
	Escribir "Ingrese la medida en pies"
	Leer m
	Escribir "Ingrese el número de inciso del conversor"
	Escribir "1. Pulgadas"
	Escribir "2. Yardas"
	Escribir "3. Centímetros"
	Escribir "4. metros"
	Leer c
	Segun c Hacer
		Opcion 1:
			resultado = m * 12
			Escribir "Es igual a ", resultado, " pulgadas"
		Opcion 2:
			resultado = m * 3
			Escribir "Es igual a ", resultado, " yardas"
		Opcion 3:
			resultado = (m * 12) * 2.54
			Escribir "Es igual a ", resultado, " centímetros"
		Opcion 4:
			resultado = ((m * 12) * 2.54)/100
			Escribir "Es igual a ", resultado, " metros"
		De Otro Modo:
			Escribir "Ingrese una opción existente"
	Fin Segun
	
	
FinAlgoritmo

//1 pulgada = 2.54/100 cm
//1 pie = 12 pulgadas