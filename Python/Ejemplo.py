import tkinter as tk
from tkinter import *

#Botón para una función de saludar
def mostrar_saludo():
    nombre = entrada_nombre.get()
    saludo = f"Hola {nombre}"
    etiqueta_saludo.config(text = saludo)

#Función para mostrar el estado de la casilla de verificación
def mostrar_estado_casilla():
    estado = "Seleccionado" if casilla_var.get() else "No seleccionado"
    etiqueta_casilla.config(text = f"Estado de la casilla: {estado}")

#Función para un radio button
def mostrar_opción():
    etiqueta_opción.config(text = f"Opción seleccionada: {opcion_var.get()}")

#Una barra de progreso
def incrementar_progreso():
    progreso.step(10)

#Vamos a crear la ventana
ventana = tk.Tk()
ventana.title("Ejemplo de Interfaz en Python")
ventana.geometry("800x600")

entrada_nombre = tk.Entry(ventana)
entrada_nombre.pack()

#Etiquetas
etiqueta_bienvenida = tk.Label(ventana, text = "Ingresa tu nombre", font = ("Arial", 16))
etiqueta_bienvenida.pack(pady = 10)

#Botón para mostrar el saludo
button_saludo = tk.Button(ventana, text = "Saludar ", command = mostrar_saludo)
button_saludo.pack(pady = 5)

#Etiqueta del saludo
etiqueta_saludo = tk.Label(ventana, text = "")
etiqueta_saludo.pack()

ventana.mainloop()