import pila

#Definir un diccionario de las funciones del archivo para que pueda invocarlas

def main():
    logica_pila = {
        "crear_pila" : pila.crear_pila,
        "apilar" : pila.apilar,
        "desapilar" : pila.desapilar,
        "cima" : pila.cima,
        "esta_vacia" : pila.esta_vacia,
        "tamano" : pila.tamano,
        "mostrar_pila" : pila.mostrar_pila
    }

#Crear la interfaz a invocarla
vista.crear_interfaz(logica_pila)

main()