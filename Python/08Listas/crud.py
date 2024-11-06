#derivado a que es necesario poder almacenar diferentes fuentes de datos
#en python se utiliza la variable diccionario
#Un diccionario es capas de poder almacenar diferentes tipos de datos en formato de lista
import tkinter as tk
from tkinter import messagebox, simpledialog


#Para poder guardar los datos correspondientes de la lista es necesario utilizar un archivo, para ello vamos a ocupar la libreria os
import os

#Vamos a declarar un archivo, tenemos dos opciones una ruta dinámica o una ruta estática, eso queda de tarea
archivo = "alumnos.txt"

#El examne debe tener al menos 8 elementos de la lista que deseen guardar
#El examen debe de poseer elementos de diálogo y mensajes de salida con tkinter
#La lista debe de implementar al menos 30 diferentes elementos y debe verse una interfaz mediante la cual los imprima en formato de lista


#Primero vamos a crear una lista de alumnos
alumnos = []

#Vamos a crear una función para cargar datos
def cargar_datos():
    #Verificar si existe el archivo
    if os.path.exists(archivo, "r"):
        with open(archivo, "r")as f:
            for linea in f:
                #Que voy a obtener por cada línea
                #Strip: Es un método de cadena que nos ayuda a eliminar espacios al inicio y al final de una cadena, ejemplo, "   había          " => "había"
                #Split: Sirve para separar elementos, e este caso con comas
                partes = linea.strip().split(",")
                if len(partes) >= 6:
                    boleta = partes[0]
                    nombre = partes[1]
                    appat = partes[2]
                    apmat = partes[3]
                    fecnac = partes[4]
                    calificaciones = list(map(float, partes[5:]))
                    alumno = {
                        "boleta" : boleta,
                        "nombre" : nombre,
                        "apellido_paterno" : appat,
                        "apellido_materno" : apmat,
                    "fecha_nacimiento" : fecnac,
                        "claificaciones" : calificaciones
                    }
                    alumnos.append(alumno)

#Vamos a crear la función para guardar los datos
def guardar_datos():
    with open(archivo, "w") as f:
        for alumno in alumnos:
            f.write(f"{alumno['boleta']}, {alumno['nombre']}, {alumno['apellido_paterno']}, {alumno['apellido_materno']}, {alumno['fecha_nacimiento']}, {','.join(map(str,alumno['calificaciones']))}\n")

#Vamos a crear una función que se encargue de registrar un alumno

def registrar_alumno():
    boleta = simpledialog.askstring("Entrada","Ingresa la boleta del alumno ")
    nombre = simpledialog.askstring("Nombre","Ingresa el nombre del alumno ")
    appat = simpledialog.askstring("Apellido Paterno","Ingresa el apellido paterno del alumno ")
    apmat = simpledialog.askstring("Apellido Materno","Ingresa el apellido materno del alumno ")
    fecnac = simpledialog.askstring("Fecha","Ingresa la fecha de nacimiento(dd/mm/aaaa) del alumno: ")
    

    calificaciones = []
    #Vamos a solicitar 3 califiaciones
    for i in range(1,4):
        califiacion_parcial = float(input("Ingrese la calificación del parcial: "))
        calificaciones.append(califiacion_parcial)

    #Defino al alumno
    alumno = {
        "boleta" : boleta,
        "nombre" : nombre,
        "apellido_paterno" : appat,
        "apellido_materno" : apmat,
        "fecha_nacimiento" : fecnac,
        "claificaciones" : calificaciones
    }
    alumnos.append(alumno)

    messagebox.showinfo("Éxito", "El alumno se registró exitosamente")

#Función para poder consultar los datos del arreglo de alumnos(lista)
def consultar_alumnos() :
    if not alumnos :
        print("No hay registros solo juguito contigo")
    else :
        print("Lista de alumnos\n")
        for alumno in alumnos :
            print(f"Boleta: {alumno['boleta']}, Nombre: {alumno['nombre']},{alumno['apellido_paterno']},{alumno['apellido_materno']}, {alumno['fecha_nacimiento']}, {alumno['calificaciones']}\n")

#Función para buscar y editar por la boleta
def editar_alumno():
    boleta = input("Ingrese la boleta del aumno que desea editar: ")
    for alumno in alumnos :
        if alumno['boleta'] == boleta :
            alumno['nombre'] = input("Ingresa el nuevo nombre o presiona Enter para manetner el actual: ") or alumno['nombre']
            alumno['apellido_paterno'] = input("Ingresa el nuevo apellido paterno o presiona Enter para manetner el actual: ") or alumno['apellido_paterno']
            alumno['apellido_materno'] = input("Ingresa el nuevo apellido materno o presiona Enter para manetner el actual: ") or alumno['apellido_materno']
            alumno['fecha_nacimiento'] = input("Ingresa la nueva fecha de nacimiento o presiona Enter para manetner el actual: ") or alumno['fecha_nacimiento']
            #Editamos las calificaciones
            for i in range(3) :
                nueva_calificacion = input("Ingresa la nueva calificación o presiona Enter para manetner el actual: ")
                if nueva_calificacion:
                    alumno['calificaciones'][i] = float(nueva_calificacion)
    return
    print("No hay más alumnos")

#eliminar alumno
def eliminar_alumno():
    print("Alumno eliminado")

def main() :
    while True :
        print("Menú de Gestión de Próximos Extras")
        print("1.- Registrar Alumno")
        print("2.- Consultar lista de Alumnos")
        print("3.- Editar Alumno")
        print("4.- Eliminar Alumno")
        print("5.- Salir")

        opcion = input("Seleccione una opción ")

        if opcion == "1" :
            registrar_alumno()
        elif opcion == "2" :
            consultar_alumnos()
        elif opcion == "3" :
            editar_alumno()
        elif opcion == "4" :
            eliminar_alumno()
        elif opcion == "5" :
            print("Ayos")
            break
        else:
            print("Opción no válida")

main()