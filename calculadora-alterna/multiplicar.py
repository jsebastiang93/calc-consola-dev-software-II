from suma import sumar

def multiplicar(a, b):
    c = 0
    while a > 0:
        c = sumar(c, b)
        a = a-1

    return c