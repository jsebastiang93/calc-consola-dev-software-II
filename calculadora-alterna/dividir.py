# division.py
from suma import sumar
from resta import restar

def dividir(a, b):
    if a < 0 or b < 0:
        return "Advertencia: Solo se permiten números positivos."
    
    if b == 0:
        return "Advertencia: No es posible dividir por cero (0)."
    
    c = 0
    while a >= b:
        a = restar(a, b)
        c = sumar(c, 1)

    return c