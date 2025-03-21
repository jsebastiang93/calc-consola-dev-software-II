# suma.py
def sumar(a, b):
    if a < 0 or b < 0:
        return "Advertencia: Solo se permiten números positivos."
    
    c = b
    while a > 0:
        a -= 1
        c += 1
        
    return c
