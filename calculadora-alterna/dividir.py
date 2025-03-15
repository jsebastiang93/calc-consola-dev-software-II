from suma import sumar
from resta import restar

def dividir (a,b):
    c = 0
    if b == 0:
        return "Advertencia: No es posible dividir por cero (0)."
    else:
        while a >= b:
            a = restar(a, b)
            c = sumar(c, 1)

        return c