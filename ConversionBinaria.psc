Algoritmo ConversionBinaria
	Definir num Como Entero
	Definir cociente, residuo Como Real
	Definir binario como texto
	
	binario = ""
	residuo = 0
	Escribir "Ingresa el número que deseas convertir a binario"
	Leer num
	Si num < 0 Entonces
		Repetir
			Escribir "Ingrese un número positivo"
			Leer num
		Hasta Que num >= 0
	FinSi
	Si num >= 0 Entonces
		Mientras num > 0 Hacer
			residuo = num % 2
			nuevobinario <- ConvertirATexto(residuo)
			binario = nuevobinario + binario
			num = Trunc(num/2)
		Fin Mientras
		
		Si binario = "" Entonces
			Escribir "0"
		FinSi
	FinSi
	Escribir "El número binario es: ",binario
FinAlgoritmo
