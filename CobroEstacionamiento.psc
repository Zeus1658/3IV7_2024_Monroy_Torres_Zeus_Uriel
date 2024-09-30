Algoritmo CobroEstacionamiento
	//Si se trabaja con módulos es importante colocar los valores como reales (No enteros), de lo contrario no agarrará
	Definir horaentrada, minutoentrada, horasalida, minutosalida Como Real
	Definir totalHoras, totalMinutos, minutostotalescuenta Como Real
	Definir totalcobro Como Real
	
	//entrada de datos
	Escribir "Ingrese la hora de entrada (formato de 24 horas)"
	Leer horaentrada
	Escribir "Ingrese los minutos de entrada (formato de 0 a 59)"
	Leer minutoentrada
	
	Escribir "Ingrese la hora de salida (formato de 24 horas)"
	Leer horasalida
	Escribir "Ingrese los minutos de salida (formato de 0 a 59)"
	Leer minutosalida
	
	//Proceso 
	//Calcular el tiempo total en minutos
	totalHoras = horasalida - horaentrada
	totalMinutos = minutosalida - minutoentrada
	
	//Tengo que empezar a evaluar los casos
	
	//Si los minutos de salida son menores a los de entrada
	//Hay que ajustar la hora y los minutosalida
	Si totalMinutos < 0 Entonces
		totalMinutos = totalMinutos + 60
		//totalMinutos += 60
		totalHoras = totalHoras - 1
	Fin Si
	
	//Convertir todo a minutos
	
	totalMinutos = (totalHoras*60) + totalMinutos
	
	//Calcular el cobro
	totalcobro = 0
	
	//Calcular el cobro por la hora completa
	Si totalMinutos >= 60 Entonces
		totalcobro = totalcobro + (totalMinutos/60)*15
	Fin Si
	
	//Calcular el cobre de cada fracción
	
	minutorestantes = totalMinutos%60
	Si minutorestantes > 0 Entonces
		fracciones15min = minutorestantes
		//Cobrar cada fracción
		totalcobro = totalcobro + fracciones15min * 6
	Fin Si
	
	//Mostrar el resultado
	Escribir "El total a pagar es de : ", totalcobro, " pesos"
	
FinAlgoritmo
