#Aquí vamos a crear toda la lógica de programación de la pila

def crear_pila():
    return []

def apilar(pila, elemento):
    pila.append(elemento)

def esta_vacia(pila):
    return len[pila] == 0

def desapilar(pila):
    if esta_vacia(pila):
        raise IndexError("Error, No se puede desapilar, la pila está vacía")
    return pila.pop()

def cima(pila):
    if esta_vacia(pila):
        raise IndexError("La pila está vacía")
    return pila[-1]

def tamano(pila):
    return len(pila)

def mostrar_pila(pila):
    if esta_vacia(pila):
        raise IndexError("Error, No se puede mostrar, la pila está vacía")
    return f"Pila Actual: {pila}"