Algoritmo Vida_de_personas
    Definir n, i, pv, pf, a�oConsulta Como Entero
    Definir aNacimientos, aFallecimientos Como Enteros
    pv = 0
    pf = 0
	m = 1
    Escribir "Ingrese la cantidad de personas"
    Leer n
    
    Dimension aNacimientos[n]
    Dimension aFallecimientos[n]
    
    Para i Desde 1 Hasta n Con Paso 1 Hacer
        Escribir "Ingrese el a�o de nacimiento de la persona ", m
        Leer aNacimientos[i]
        Escribir "Ingrese el a�o de fallecimiento de la persona ", m
        Leer aFallecimientos[i]
		m <- m + 1
    Fin Para
    
    Escribir "Ingrese el a�o que desea consultar"
    Leer a�oConsulta
	
    pv = 0
    pf = 0
    edadMaxima = -1
    edadMinima = -1
	
    Para i Desde 1 Hasta n - 1 Con Paso 1 Hacer
        Si a�oConsulta >= aNacimientos[i] Y a�oConsulta <= aFallecimientos[i] Entonces
            pv = pv + 1 
            edad <- a�oConsulta - aNacimientos[i]
            
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
	
    Escribir "Las personas vivas en el a�o ", a�oConsulta, " son: ", pv
    Escribir "Las personas fallecidas en el a�o ", a�oConsulta, " son: ", pf
	
    Si pv > 0 Entonces
        Escribir "La persona m�s joven tiene ", edadMinima, " a�os."
        Escribir "La persona m�s anciana tiene ", edadMaxima, " a�os."
    Sino
        Escribir "No hab�a personas vivas en el a�o ", a�oConsulta
    Fin Si

FinAlgoritmo
