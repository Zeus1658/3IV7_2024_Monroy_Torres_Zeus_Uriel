import tkinter as tk
from tkinter import messagebox

#Vamos a crear la interfaz
def crear_interfaz(logica_pila):
    #Creamos la ventana
    ventana = tk.Tk()
    ventana.title("Manejo de pila")
    ventana.geometry("400x400")

#Necesitamos a una pila para realizar las invocaciones
pila = logica_pila["Crear pila"]()

#Funciones de la interfaz
def manejar_apilar():
    elemento = entrada.elemento.get()
    if elemento:
        logica_pila["apilar"](pila, elemento)
        actualizar_pila()
        entrada_elemento.delete(0, tk.END)
    else:
        messagebox.showwarning("Entrada Vacía", "Por favor ingresa un elemento")

def manejar_desapilar():
    try:
        elemento = logica_pila["cima"](pila)
        messagebox.showinfo("Cima", f"Elemento de la cima: {elemento}")
    except IndexError as e:
        messagebox.showerror("Error", str(e))

def manejar_tamano():
    tam = logica_pila["tamano"](pila)
    messagebox.showinfo("Tamaño", f"El tamaño de la pila: {tam}")

def manejar_mostrar():
    pila_actual = logica_pila["mostrar_pila"](pila)

def actualizar_pila():
    pila_actual = logica_pila["mostrar_pila"](pila)
    etiqueta_pila.config(text = pila_actual)

#Componentes de la interfaz
tk.Label(ventana, text = "Manejo de una pila", font = ("Arial", 16)).pack(pady = 10)}

entrada_elemento = tk.Entry(ventana, width = 30)
entrada_elemento.pack(pady = 5)
tk.Button(ventana, texto = "Apilar", comando = manejar_apilar).pack(pady = 5)
tk.Button(ventana, texto = "Desapilar", comando = manejar_desapilar).pack(pady = 5)
tk.Button(ventana, texto = "Ver cima", comando = manejar_cima).pack(pady = 5)
tk.Button(ventana, texto = "Ver tamañp", comando = manejar_tamano).pack(pady = 5)
tk.Button(ventana, texto = "Mosttrar Pila", comando = manejar_mostrar).pack(pady = 5)

etiqueta_pila = tk.Label(ventana, text = "pila actual:[]", font = ("Arial", 12)).pack(pady = 20)

ventana.mainloop()

