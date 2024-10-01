Algoritmo Vida_de_personas
    Definir n, i, pv, pf, añoConsulta Como Entero
    Definir aNacimientos, aFallecimientos Como Enteros
    pv = 0
    pf = 0
	m = 1
    Escribir "Ingrese la cantidad de personas"
    Leer n
    
    Dimension aNacimientos[n]
    Dimension aFallecimientos[n]
    
    Para i Desde 1 Hasta n Con Paso 1 Hacer
        Escribir "Ingrese el año de nacimiento de la persona ", m
        Leer aNacimientos[i]
        Escribir "Ingrese el año de fallecimiento de la persona ", m
        Leer aFallecimientos[i]
		m <- m + 1
    Fin Para
    
    Escribir "Ingrese el año que desea consultar"
    Leer añoConsulta
	
    pv = 0
    pf = 0
    edadMaxima = -1
    edadMinima = -1
	
    Para i Desde 1 Hasta n - 1 Con Paso 1 Hacer
        Si añoConsulta >= aNacimientos[i] Y añoConsulta <= aFallecimientos[i] Entonces
            pv = pv + 1 
            edad <- añoConsulta - aNacimientos[i]
            
            Si edadMaxima = -1 O edad > edadMaxima Entonces
                edadMaxima = edad
            FinSi
			
            Si edadMinima = -1 O edad < edadMinima Entonces
                edadMinima = edad
            FinSi
        Sino
            pf = pf + 1 
        Fin Si
    Fin Para
	
    Escribir "Las personas vivas en el año ", añoConsulta, " son: ", pv
    Escribir "Las personas fallecidas en el año ", añoConsulta, " son: ", pf
	
    Si pv > 0 Entonces
        Escribir "La persona más joven tiene ", edadMinima, " años."
        Escribir "La persona más anciana tiene ", edadMaxima, " años."
    Sino
        Escribir "No había personas vivas en el año ", añoConsulta
    Fin Si

FinAlgoritmo
