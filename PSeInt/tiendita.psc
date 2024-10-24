Algoritmo tiendita
	
	Definir producto como Texto
	Definir codigoproducto, cantidad Como Entero
	Definir precio Como Real 
	
	//Tengo que crear un menú de selección
	Mientras opción <> 5  Hacer
		Escribir "1.- Ingresar un nuevo Producto"
		Escribir "2.- Actualizar un Producto"
		Escribir "3.- Consulta el Inventario"
		Escribir "4.- Generar Reporte"
		Escribir "5.- Salir"
		
		Leer opcion
		
		Segun opcion Hacer
			Caso 1:
				Escribir "Ingresa el nombre del producto"
				Leer producto
				Escribir "Ingresa el código del producto"
				Leer codigoproducto
				Escribir "Ingresa la cantidad"
				Leer cantidad
				Escribir "Ingresa el precio"
				Leer precio
			Caso 2:
				Escribir "Ingresa el código del producto a actualizar"
				Leer codigoproducto
				Escribir "Ingresa la nueva cantidad"
				Leer cantidad
			Caso 3:
				Escribir "Consultar inventario"
				Escribir "Nombre del producto ", producto
				Escribir "Código del producto ", codigoproducto
				Escribir "Precio del producto ", precio
				Escribir "Cantidad del producto ", cantidad
			Caso 4:
				Escribir "Generar reporte"
			Caso 5:
				Escribir "Salida con éxito"
		Fin Segun
	Fin Mientras
	
FinAlgoritmo
