import tkinter as tk
from tkinter import messagebox

def crear_interfaz(grafo, aristas, nodos, logica):
    ventana = tk.Tk()
    ventana.title("Planificación de Rutas")
    ventana.geometry("800x600")

    def mostrar_caminos():
        inicio = entrada_inicio.get()
        if inicio in grafo:
            distancias = logica["dijkastra"](grafo, inicio)
            resultado = "\n" .join([f"{ciudad}, {distancia}" for ciudad, distancia in distancias.items()])
            messagebox.showinfo("Camino mas corto: ", resultado)
        else:
            messagebox.showerror("Error", "Ciudad de inicio no válida")

    def mostrar_arbol():
        mst = logica["kruskal"](aristas, nodos)
        resultado = "\n" .join([f"{u} --- {v} [peso: {peso}]" for u, v, peso in mst])
        messagebox.showinfo("Arbol de Expansión mínimal: ", resultado)

    tk.Label(ventana, text = "Planificación de rutas")

    tk.Label(ventana, text = "Ciudad de Inicio: ").pack(pady = 5)

    entrada_inicio = tk.Entry(ventana)
    entrada_inicio.pack(pady = 5)

    tk.Button(ventana, text = "Mostrar camino más corto")
    tk.Button(ventana, text = "Mostrar arbol de expansión mínima")

    ventana.mainloop()
crear_interfaz()
