import tkinter as tk
from tkinter import messagebox, ttk
import time

#metodo burbuja
def burbuja(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if (lista[j] > lista[j+1]):
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

#metodo sort
def seleccion_sort(lista):
    n = len(lista)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if lista[j] < lista[min_idx]:
                min_idx = j
        lista[i], lista[min_idx] = lista[min_idx], lista[i]
    return lista

#metodo de insercion
def insercion(lista):
    for i in range(1, len(lista)):
        key = lista[i]
        j = i - 1
        while j >= 0 and key < lista[j]:
            lista[j+1] = lista[j]
            j -= 1
        lista[j+1] = key
    return lista

#merge
def merge(lista):
    if len(lista) > 1:
        mid = len(lista)//2
        izquierda = lista[:mid]
        derecha = lista[mid:]

        # Recursión
        merge(izquierda)
        merge(derecha)

        i = j = k = 0

        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] < derecha[j]:
                lista[k] = izquierda[i]
                i += 1
            else:
                lista[k] = derecha[j]
                j += 1
            k += 1

        while i < len(izquierda):
            lista[k] = izquierda[i]
            i += 1
            k += 1

        while j < len(derecha):
            lista[k] = derecha[j]
            j += 1
            k += 1
    return lista

#quick sort
def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    pivote = lista[len(lista)//2]
    izquierda = [x for x in lista if x < pivote]
    medio = [x for x in lista if x == pivote]
    derecha = [x for x in lista if x > pivote]
    return quick_sort(izquierda) + medio + quick_sort(derecha)

def menu():
    ventana = tk.Tk()
    ventana.geometry("400x400")
    ventana.configure(bg="gray30")
    ventana.resizable(False, False)

    texto_config = ('Arial', 10, 'bold')
    texto = tk.Text(ventana, height=5, width=60)
    texto.insert(tk.END, "Ingresa hasta 40 números enteros separados por espacios:")
    texto.config(state=tk.DISABLED, bg="gray30", font=texto_config, fg='white', borderwidth=0)
    texto.pack(padx=10, pady=20)

    texto_config1 = ('Arial', 15, 'bold')
    numeros = tk.Entry(ventana, bg='white', fg='black', borderwidth=0, width=30, font=texto_config1)
    numeros.pack()

    metodo_seleccionado = tk.StringVar(value="Seleccione un método")
    metodos = ["Burbuja", "Selección", "Inserción", "Merge Sort", "Quick Sort"]
    dropdown = ttk.OptionMenu(ventana, metodo_seleccionado, *metodos)
    dropdown.pack(pady=20)

    def procesar_datos():
        entrada = numeros.get()
        try:
            lista = list(map(int, entrada.split()))
            if len(lista) > 40:
                messagebox.showerror("Error", "Por favor, ingresa un máximo de 40 números.")
                return

            start_time = time.time()
            metodo = metodo_seleccionado.get()
            if metodo == "Burbuja":
                resultado = burbuja(lista)
            elif metodo == "Selección":
                resultado = seleccion_sort(lista)
            elif metodo == "Inserción":
                resultado = insercion(lista)
            elif metodo == "Merge Sort":
                resultado = merge(lista)
            elif metodo == "Quick Sort":
                resultado = quick_sort(lista)
            else:
                messagebox.showerror("Error", "Selecciona un método de ordenamiento.")
                return
            end_time = time.time()
            elapsed_time = end_time - start_time

            messagebox.showinfo("Resultado", f"Lista ordenada: {resultado}\n Tiempo de ejecución: {elapsed_time:.6f} segundos")
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingresa solo números enteros separados por espacios.")

    boton_procesar = tk.Button(ventana, text="Ordenar", command=procesar_datos, bg="white", font=texto_config)
    boton_procesar.pack(pady=20)

    ventana.mainloop()

menu()