Algoritmo Reserva_hotel
	Definir h, me, ms, d_e, ds , n, oc, cr Como Entero
	
	//menú de selección
	Escribir "Ingrese el número de la opción que desea emplear"
	Mientras opcion <> 5 Hacer
		Escribir "1.- Reservar una habitación"
		Escribir "2.- Cancelar una reservación"
		Escribir "3.- Consultar disponibilidad"
		Escribir "4.- Gestionar la ocupación del hotel"
		Escribir "5.- Salir"
		Leer opcion
		
		Segun opcion Hacer
			caso 1:
				Escribir "Ingrese el número de habitación que desea reservar"
				Leer h
				Si h > 20 Entonces
					Repetir
						Escribir "Solo hay habitaciones de la 1 a la 20"
						Escribir "Ingrese el número de habitación que desea reservar"
						Leer h
					Hasta Que h <= 20
				Fin Si
				Escribir "Ingrese el mes de entrada"
				Leer me
				Escribir "Ingrese el día de entrada"
				Leer d_e
				Escribir "Ingrese el mes de salida"
				Leer ms
				Escribir "Ingrese el día de salida"
				Leer ds
				num = h*me*d_e*ms*ds
				Escribir "Se ha confirmado su reserva, su número de reserva es: ", num
			caso 2:
				Escribir "Para cancelar su reserva, ingrese su número de reserva"
				Leer cr
				Si cr = num Entonces
					Escribir "Su reserva ha sido cancelada"
				SiNo
					Escribir "El número de reserva no coincide o no existe"
				Fin Si
			caso 3:
				Escribir "Ingrese las fechas en las que se desea quedar"
				Escribir "Ingrese el mes de entrada"
				Leer me
				Escribir "Ingrese el día de entrada"
				Leer d_e
				Escribir "Ingrese el mes de salida"
				Leer ms
				Escribir "Ingrese el día de salida"
				Leer ds
				Escribir "Habitaciones libres: "
				Escribir "Todas las habitaciones de la 1 a la 20"
				Escribir "Habitaciones ocupadas: "
				Escribir "0"
			caso 4:
				Escribir "La gestión del hotel por el momento es del 35%"
		Fin Segun
	Fin Mientras
	
FinAlgoritmo
