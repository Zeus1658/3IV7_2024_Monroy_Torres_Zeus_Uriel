Algoritmo ConversionTemperatura
	Definir resultado, grados Como Real
	Escribir "Ingrese la tempertura en grados Farenheit"
	Leer grados
	Escribir "Ingrese el número de inciso del conversor"
	Escribir "1. Clesius"
	Escribir "2. Kelvin"
	Escribir "3. Rankine"
	Leer n
	Segun n Hacer
		Opcion 1:
			resultado = ((grados - 32) * (5 / 9))
			Escribir "El resultado es: ", resultado,"° C"
		Opcion 2:
			resultado = (grados - 32) * (5/9) + 273.15
			Escribir "El resultado es: ", resultado," K"
		Opcion 3:
			resultado = grados + 459.67
			Escribir "El resultado es: ", resultado, "° R"
	Fin Segun
	
FinAlgoritmo
