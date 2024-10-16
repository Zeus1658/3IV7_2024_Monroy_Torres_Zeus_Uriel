Algoritmo sin_titulo
	pos = 0
	neg = 0
	Escribir "Ingresa la cantidad de números a leer"
	Leer n
	Escribir "Ingrese los valores"
	Repetir
		Leer m
		Si m > 0 Entonces
			pos = pos + 1
		SiNo
			neg = neg + 1
		Fin Si
		n = n - 1
	Hasta Que n = 0
	Escribir "La cantidad de números positivos es de: ", pos
	Escribir "La cantidad de números negativos es de: ", neg
FinAlgoritmo
