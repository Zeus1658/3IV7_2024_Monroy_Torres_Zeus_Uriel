Algoritmo Fórmula_General
	Definir a, b, c, resultado1, resultado2 Como Real
	
	Escribir "Ingrese el valor de A de la fórmula"
	Leer a
	Escribir "Ingrese el valor de B de la fórmula"
	Leer b
	Escribir "Ingrese el valor de C de la fórmula"
	Leer c
	ecuacion = b^2-4*a*c
	Si ecuacion < 0 Entonces
		Escribir "Ecuación sin solución"
	FinSi
	
	resultado1 = (-b+raiz(ecuacion))/2*a
	resultado2 = (-b-raiz(ecuacion))/2*a
	Si resultado1 = resultado2 Entonces
		Escribir "La única solución es: ", resultado1
	SiNo
		Escribir "Los resultados son: X1= ",resultado1, ", X2= ",resultado2
	FinSi
FinAlgoritmo
