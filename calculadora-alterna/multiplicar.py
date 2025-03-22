# multiplicacion.py
from suma import sumar

def multiplicar(a, b):
    if a < 0 or b < 0:
        print("Advertencia: Solo se permiten números positivos.")
        return 0
    
    c = 0
    while a > 0:
        c = sumar(c, b)
        a -= 1

    return c