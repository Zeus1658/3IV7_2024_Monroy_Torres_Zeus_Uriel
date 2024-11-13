import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
import os

archivo = 'Componentes.txt'
componentes = []

def cargar_datos():
    componentes.clear()
    if os.path.exists(archivo): 
        try:
            with open(archivo, 'r') as a:
                for fila in a:
                    partes = fila.strip().split(',')
                    if len(partes) >= 8: 
                        Tipo = partes[0]
                        Nombre = partes[1]
                        Modelo = partes[2]
                        Rendimiento = partes[3]
                        Resistencia = partes[4]
                        Temperatura = partes[5]
                        Energía = partes[6]
                        Cache = partes[7]
                        componente = {
                            'Tipo': Tipo,
                            'Nombre': Nombre,
                            'Modelo': Modelo,
                            'Rendimiento': Rendimiento,
                            'Resistencia': Resistencia,
                            'Temperatura': Temperatura,
                            'Energía': Energía,
                            'Caché': Cache
                        }
                        componentes.append(componente)
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo cargar el archivo: {str(e)}")
    else:
        messagebox.showinfo("Archivo no encontrado", "El archivo 'Componentes.txt' no existe. No se pueden cargar los datos.")

def guardar_datos():
    try:
        with open(archivo, 'w') as a:
            for componente in componentes:
                a.write(f"{componente['Tipo']}, {componente['Nombre']}, {componente['Modelo']}, {componente['Rendimiento']}, {componente['Resistencia']}, {componente['Temperatura']}, {componente['Energía']}, {componente['Caché']}\n")
    except Exception as e:
        messagebox.showerror("Error al guardar", f"No se pudo guardar el archivo: {str(e)}")

def registrar_componente():
    registro = tk.Toplevel()
    registro.title = "Registrar Nuevo Componente"
    registro.geometry("700x650")
    registro.configure(bg = 'gray30')

    texto = tk.Text(registro,borderwidth=0, height = 1, width = 30)
    texto_config = ('Arial', 25, 'bold')
    texto.insert(tk.END,"REGISTRAR UN COMPONENTE")
    texto.config(state = tk.DISABLED)
    texto.configure(bg="gray30", font = texto_config, fg = 'orange2')
    texto.place(x = 100, y = 20)    

    img = tk.PhotoImage(file = 'Registro.png')
    tamaño_img = img.subsample(2,2)
    lbl_img = tk.Label(registro, image = tamaño_img, bg = 'gray30')
    lbl_img.place(x = 350, y = 150)
    lbl_img.image = tamaño_img
    
    casilla_config = ('Arial', 13, 'bold')
    entry_config = ('Arial', 12, 'bold')

    tk.Label(registro, text = "Tipo", bg = 'gray30', fg = 'white', font = casilla_config, pady = 5).place(x = 10, y = 75)
    tipo_entry = tk.Entry(registro, width = 30, bg = 'gray65', borderwidth = 0, font = entry_config)
    tipo_entry.place(x = 30, y = 105)

    tk.Label(registro, text = "Nombre", bg = 'gray30', fg = 'white', font = casilla_config, pady = 5).place(x = 10, y = 150)
    nombre_entry = tk.Entry(registro, width = 30, bg = 'gray65', borderwidth = 0, font = entry_config)
    nombre_entry.place(x = 30, y = 180)

    tk.Label(registro, text = "Modelo", bg = 'gray30', fg = 'white', font = casilla_config, pady = 5).place(x = 10, y = 215)
    modelo_entry = tk.Entry(registro, width = 30, bg = 'gray65', borderwidth = 0, font = entry_config)
    modelo_entry.place(x = 30, y = 245)

    tk.Label(registro, text = "Rendimiento", bg = 'gray30', fg = 'white', font = casilla_config, pady = 5).place(x = 10, y = 280)
    rend_entry = tk.Entry(registro, width = 30, bg = 'gray65', borderwidth = 0, font = entry_config)
    rend_entry.place(x = 30, y = 310)

    tk.Label(registro, text = "Resistencia", bg = 'gray30', fg = 'white', font = casilla_config, pady = 5).place(x = 10, y = 345)
    res_entry = tk.Entry(registro, width = 30, bg = 'gray65', borderwidth = 0, font = entry_config)
    res_entry.place(x = 30, y = 375)

    tk.Label(registro, text = "Temperatura", bg = 'gray30', fg = 'white', font = casilla_config, pady = 5).place(x = 10, y = 410)
    temp_entry = tk.Entry(registro, width = 30, bg = 'gray65', borderwidth = 0, font = entry_config)
    temp_entry.place(x = 30, y = 440)

    tk.Label(registro, text = "Energía", bg = 'gray30', fg = 'white', font = casilla_config, pady = 5).place(x = 10, y = 475)
    energ_entry = tk.Entry(registro, width = 30, bg = 'gray65', borderwidth = 0, font = entry_config)
    energ_entry.place(x = 30, y = 505)

    tk.Label(registro, text = "Caché", bg = 'gray30', fg = 'white', font = casilla_config, pady = 5).place(x = 10, y = 540)
    cache_entry = tk.Entry(registro, width = 30, bg = 'gray65', borderwidth = 0, font = entry_config)
    cache_entry.place(x = 30, y = 570)

    def guardar():
        Tipo = tipo_entry.get()
        Nombre = nombre_entry.get()
        Modelo = modelo_entry.get()
        Rendimiento = rend_entry.get()
        Resistencia = res_entry.get()
        Temperatura = temp_entry.get()
        Energia = energ_entry.get()
        Cache = cache_entry.get()

        if not Tipo or not Nombre or not Modelo or not Rendimiento or not Resistencia or not Temperatura or not Energia or not Cache:
            messagebox.showerror("Error", "Verifica que todas las casillas estén llenas")
            return
        
        componente = {
            'Tipo':Tipo,
            'Nombre':Nombre,
            'Modelo':Modelo,
            'Rendimiento':Rendimiento,
            'Resistencia':Resistencia,
            'Temperatura':Temperatura,
            'Energía':Energia,
            'Caché':Cache
        }
        componentes.append(componente)

        guardar_datos()

        messagebox.showinfo("Registrado","El componente se ha agregado correctamente")
        registro.destroy()

    boton_config = ('Arial', 15, 'bold')
    tk.Button(registro, text = "Guardar", command = guardar, bg = 'DarkOrchid3', borderwidth = 0, font = boton_config, padx = 5, pady = 5, width = 15).place(x = 400, y = 500)
    tk.Button(registro, text = "Cancelar", command = registro.destroy, bg = 'red2', borderwidth = 0, fg = 'white', font = boton_config).place(x = 445, y = 570)

def buscar_componente():
    if not componentes:
        messagebox.showinfo("Consulta", "No hay componentes por el momento")
        return

    buscar = tk.Toplevel()
    buscar.title("Buscar Componente")
    buscar.geometry("1600x500")
    buscar.resizable(False, False)
    buscar.configure(bg = 'gray30')

    style = ttk.Style()
    style.configure("Custom.Treeview", background="grey18", fieldbackground="grey18", foreground="white", rowheight=20)
    style.map("Custom.Treeview", background=[("selected", "purple4")])

    bloque = ttk.Treeview(buscar, columns=('Tipo', 'Nombre', 'Modelo', 'Rendimiento', 'Resistencia', 'Temperatura', 'Energía', 'Caché'), show='headings', style = "Custom.Treeview")
    bloque.tag_configure('oddrow', background="grey13")
    bloque.tag_configure('evenrow', background="grey18")
    bloque.heading('Tipo', text='Tipo')
    bloque.heading('Nombre', text='Nombre')
    bloque.heading('Modelo', text='Modelo')
    bloque.heading('Rendimiento', text='Rendimiento')
    bloque.heading('Resistencia', text='Resistencia')
    bloque.heading('Temperatura', text='Temperatura')   
    bloque.heading('Energía', text='Energía Necesaria')
    bloque.heading('Caché', text='Memoria Caché')
    bloque.pack()

    lbl_config = ('Arial', 25, 'bold')
    entry_config = ('Arial', 15, 'bold')
    tk.Label(buscar, text="Ingrese el tipo de componente", bg = 'gray30', fg = 'white', font = lbl_config).place(x = 570, y = 280)
    componente_entry = tk.Entry(buscar)
    componente_entry.configure(bg = 'gray55', fg = 'white', borderwidth = 0, width = 70, font = entry_config)
    componente_entry.place(x = 420, y = 350)

    def busqueda():
        for item in bloque.get_children():
            bloque.delete(item)

        tipo_buscado = componente_entry.get()
        hay_resultados = False

        for idx, componente in enumerate(componentes):
            if componente['Tipo'].lower() == tipo_buscado.lower():
                tag = 'oddrow' if idx % 2 == 0 else 'evenrow'
                bloque.insert("", tk.END, id = idx, values = (componente['Tipo'], componente['Nombre'], componente['Modelo'], componente['Rendimiento'], componente['Resistencia'], componente['Temperatura'], componente['Energía'], componente['Caché']), tags = (tag,))
                hay_resultados = True

        if not hay_resultados:
            messagebox.showinfo("Resultado de la búsqueda", "No se encontraron componentes con ese tipo.")

    boton_config = ('Arial', 20, 'bold')
    tk.Button(buscar, text = "Buscar", command = busqueda, bg = 'purple4', fg = 'white', borderwidth = 0, font = boton_config, width = 8).place(x = 600, y = 420)
    tk.Button(buscar, text = "Volver", command = buscar.destroy, bg = 'orange2', fg = 'white', borderwidth = 0, font = boton_config, width = 8).place(x = 900, y = 420)

def consultar_componentes():
    if not componentes:
        messagebox.showinfo("Consulta", "No hay componentes por el momento")
    else:
        consultar = tk.Toplevel()
        consultar.title("Consultar Componente")
        consultar.geometry("1600x700")
        consultar.resizable(False, False)
        consultar.configure(bg = 'gray15')

        style = ttk.Style()
        style.configure("Custom.Treeview", background = "purple4", fieldbackground = "purple4", foreground = "white", rowheight = 20)
        style.map("Custom.Treeview", background=[("selected", "purple4")])

        bloque = ttk.Treeview(consultar, columns = ('Tipo', 'Nombre', 'Modelo', 'Rendimiento', 'Resistencia', 'Temperatura', 'Energía', 'Caché'), show='headings', style="Custom.Treeview")
        bloque.tag_configure('oddrow', background = "grey13")
        bloque.tag_configure('evenrow', background = "grey18")
        bloque.heading('Tipo', text = 'Tipo')
        bloque.heading('Nombre', text = 'Nombre')
        bloque.heading('Modelo', text = 'Modelo')
        bloque.heading('Rendimiento', text = 'Rendimiento')
        bloque.heading('Resistencia', text = 'Resistencia')
        bloque.heading('Temperatura', text = 'Temperatura')   
        bloque.heading('Energía', text = 'Energía Necesaria')
        bloque.heading('Caché', text = 'Memoria Caché')

        bloque.column("#0", width=0, stretch=tk.NO)
        for col in ('Tipo', 'Nombre', 'Modelo', 'Rendimiento', 'Resistencia', 'Temperatura', 'Energía', 'Caché'):
            bloque.column(col, anchor='w')

        for idx, componente in enumerate(componentes):
            tag = 'oddrow' if idx % 2 == 0 else 'evenrow'
            bloque.insert("", tk.END, values=(componente['Tipo'], componente['Nombre'], componente['Modelo'], componente['Rendimiento'], componente['Resistencia'], componente['Temperatura'], componente['Energía'], componente['Caché']), tags=(tag,))

        bloque.pack(fill="both", expand=True)

    boton_config = ('Arial', 15, 'bold')
    tk.Button(consultar, text = "", bg = 'gray15', borderwidth = 0 ).pack(padx = 10,pady = 20)
    tk.Button(consultar, text="Salir", command = consultar.destroy, bg = 'red2', borderwidth = 0, fg = 'white', font = boton_config, width = 10).place(x = 750, y = 650)

def editar_componente():
    if not componentes:
        messagebox.showinfo("Editar", "No existen componentes para editar.")
        return
    
    editar = tk.Toplevel()
    editar.title("Edición de Componentes")
    editar.geometry("1650x800")
    editar.configure(bg="gray10")
    editar.resizable(False, False)

    editar_config = ('Arial', 16, 'bold')

    texto = tk.Text(editar, height = 1, width = 120, borderwidth = 0)
    texto.insert("1.0", 'PRIMERO SELECCIONA EL COMPONENTE ANTES DE PRESIONAR UN BOTÓN')
    texto.pack(pady = 20, padx = 400)
    texto.configure(bg = "gray10", fg = 'orange3', font = editar_config)
    texto.config(state = tk.DISABLED)

    def eliminar_componente():
        selected_item = bloque.selection()
        
        if not selected_item:
            messagebox.showwarning("Selección requerida", "Selecciona un componente para eliminar.")
            return
        else:
            respuesta = messagebox.askyesno("Pregunta", "¿Estás segura que deseas eliminar este componente?")
            if respuesta == True:
                idx = int(selected_item[0])
                bloque.delete(selected_item)
                
                del componentes[idx]
                guardar_datos()
                messagebox.showinfo("Eliminado", "El componente ha sido eliminado correctamente.")
                return

    style = ttk.Style()
    style.configure("Custom.Treeview", background="purple4", fieldbackground="white", foreground="white", rowheight=20)
    style.map("Custom.Treeview", background=[("selected", "purple4")])

    bloque = ttk.Treeview(editar, columns = ('Tipo', 'Nombre', 'Modelo', 'Rendimiento', 'Resistencia', 'Temperatura', 'Energía', 'Caché'), show='headings', style="Custom.Treeview")
    bloque.tag_configure('oddrow', background = "grey13")
    bloque.tag_configure('evenrow', background = "grey18")
    bloque.heading('Tipo', text = 'Tipo')
    bloque.heading('Nombre', text = 'Nombre')
    bloque.heading('Modelo', text = 'Modelo')
    bloque.heading('Rendimiento', text = 'Rendimiento')
    bloque.heading('Resistencia', text = 'Resistencia')
    bloque.heading('Temperatura', text = 'Temperatura')   
    bloque.heading('Energía', text = 'Energía Necesaria')
    bloque.heading('Caché', text = 'Memoria Caché')

    for col in ('Tipo', 'Nombre', 'Modelo', 'Rendimiento', 'Resistencia', 'Temperatura', 'Energía', 'Caché'):
        bloque.column(col, anchor = 'w')

    for idx, componente in enumerate(componentes):
        tag = 'oddrow' if idx % 2 == 0 else 'evenrow'
        bloque.insert("", tk.END, id = idx, values = (componente['Tipo'], componente['Nombre'], componente['Modelo'], componente['Rendimiento'], componente['Resistencia'], componente['Temperatura'], componente['Energía'], componente['Caché']), tags = (tag,))

    bloque.pack(fill = "both", expand = True)

    def editar_datos_componente():
        selected_item = bloque.selection()[0]
        componente = componentes[int(selected_item)]
        
        editar_ventana = tk.Toplevel()
        editar_ventana.title("Editar Componente")
        editar_ventana.geometry("500x500")
        editar_ventana.configure(bg = 'gray15')
        
        tipo_entry = tk.Entry(editar_ventana)
        tipo_entry.insert(0, componente['Tipo'])
        tipo_entry.configure(bg = 'gray40', fg = 'white', borderwidth = 0, width = 75)
        tipo_entry.place(x = 24, y = 45)
        
        nombre_entry = tk.Entry(editar_ventana)
        nombre_entry.insert(0, componente['Nombre'])
        nombre_entry.configure(bg = 'gray40', fg = 'white', borderwidth = 0, width = 75)
        nombre_entry.place(x = 24, y = 90)
        
        modelo_entry = tk.Entry(editar_ventana)
        modelo_entry.insert(0, componente['Modelo'])
        modelo_entry.configure(bg = 'gray40', fg = 'white', borderwidth = 0, width = 75)
        modelo_entry.place(x = 24, y = 135)
        
        rendimiento_entry = tk.Entry(editar_ventana)
        rendimiento_entry.insert(0, componente['Rendimiento'])
        rendimiento_entry.configure(bg = 'gray40', fg = 'white', borderwidth = 0, width = 75)
        rendimiento_entry.place(x = 24, y = 180)
        
        resistencia_entry = tk.Entry(editar_ventana)
        resistencia_entry.insert(0, componente['Resistencia'])
        resistencia_entry.configure(bg = 'gray40', fg = 'white', borderwidth = 0, width = 75)
        resistencia_entry.place(x = 24, y = 225)
        
        temperatura_entry = tk.Entry(editar_ventana)
        temperatura_entry.insert(0, componente['Temperatura'])
        temperatura_entry.configure(bg = 'gray40', fg = 'white', borderwidth = 0, width = 75)
        temperatura_entry.place(x = 24, y = 270)
        
        energia_entry = tk.Entry(editar_ventana)
        energia_entry.insert(0, componente['Energía'])
        energia_entry.configure(bg = 'gray40', fg = 'white', borderwidth = 0, width = 75)
        energia_entry.place(x = 24, y = 315)
        
        cache_entry = tk.Entry(editar_ventana)
        cache_entry.insert(0, componente['Caché'])
        cache_entry.configure(bg = 'gray40', fg = 'white', borderwidth = 0, width = 75)
        cache_entry.place(x = 24, y = 360)

        def guardar_cambios():
            componente['Tipo'] = tipo_entry.get()
            componente['Nombre'] = nombre_entry.get()
            componente['Modelo'] = modelo_entry.get()
            componente['Rendimiento'] = rendimiento_entry.get()
            componente['Resistencia'] = resistencia_entry.get()
            componente['Temperatura'] = temperatura_entry.get()
            componente['Energía'] = energia_entry.get()
            componente['Caché'] = cache_entry.get()

            guardar_datos()

            messagebox.showinfo("Componente Editado", "El componente ha sido actualizado.")
            editar_ventana.destroy()

        boton_config = ('Arial', 15, 'bold')
        tk.Button(editar_ventana, text = "Guardar", command = guardar_cambios, bg = 'orange2', borderwidth = 0, fg = 'white', width = 10, font = boton_config).place(x = 50, y = 410)
        tk.Button(editar_ventana, text = "Cancelar", command = editar_ventana.destroy, bg = 'red2', borderwidth = 0, fg = 'white', width = 10, font = boton_config).place(x = 320, y = 410)

    boton_config = ('Arial', 11, 'bold')

    tk.Button(editar, text = "Eliminar Componente Seleccionado", command = eliminar_componente, bg = 'red4', borderwidth = 0, fg = 'white', font = boton_config).place(x = 10, y = 755)
    tk.Button(editar, text = "Editar Componente Seleccionado", command = editar_datos_componente, bg = 'purple4', borderwidth = 0, fg = 'white', font = boton_config).place(x = 300, y = 755)
    tk.Button(editar, text = "", bg = 'gray10', borderwidth = 0 ).pack(pady = 20)
    tk.Button(editar, text = "Salir", command = editar.destroy, bg = 'red2', borderwidth = 0, fg = 'white', font = boton_config, width = 10).place(x = 1500, y = 755)

def menu():
    ventana = tk.Tk()
    ventana.title("Componentes para PC's")
    ventana.wm_geometry("1500x800")
    ventana.resizable(False, False)
    ventana.configure(bg = "gray15")
    ventana.wm_attributes("-alpha", 1)

    texto = tk.Text(ventana, height = 4, width = 50, borderwidth = 0)
    texto_config = ('Arial', 50, 'bold')
    texto.insert(tk.END,"BIENVENIDO")
    texto.config(state = tk.DISABLED) 
    texto.configure(bg = "gray15", font = texto_config, fg = 'orange2')
    texto.place(x = 900, y = 100)

    img = tk.PhotoImage(file = 'Inicio.png')
    lbl_img = tk.Label(ventana, image = img, bg = 'gray15')
    lbl_img.place(x = 800, y = 200)

    font_config = ('georgia', 20, 'bold')

    tk.Button(ventana, text = "Registrar Componente", command = registrar_componente, fg = 'DarkOrchid4', bg = 'purple2', borderwidth = 0, font = font_config, width = 35, pady = 12).place(x = 80, y = 100)
    tk.Button(ventana, text = "Buscar Componente", command = buscar_componente, fg = 'DarkOrchid4', bg = 'purple2', borderwidth = 0, font = font_config, width = 35, pady = 12).place(x = 80, y = 240)
    tk.Button(ventana, text = "Consultar Componente", command = consultar_componentes, fg = 'DarkOrchid4', bg = 'purple2', borderwidth = 0, font = font_config, width = 35, pady = 12).place(x = 80, y = 380)
    tk.Button(ventana, text = "Editar Componente", command = editar_componente, fg = 'DarkOrchid4', bg = 'purple2', borderwidth = 0, font = font_config, width = 35, pady = 12).place(x = 80, y = 520)
    tk.Button(ventana, text = "Salir", command = ventana.destroy, fg = 'white', bg = 'red2', borderwidth = 0, font = font_config, width = 20, pady = 2).place(x = 200, y = 660)
    ventana.mainloop()

cargar_datos()
menu()