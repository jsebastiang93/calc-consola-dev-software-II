import suma.py
import resta.py

def dividir(a, b):
    
    if b == 0:
        raise ValueError("No se puede dividir por cero")
    
    negativo = (a < 0) ^ (b < 0)  # Determina si el resultado será negativo
    cociente = 0

    # Ajusta los operandos para trabajar con sus magnitudes sin usar abs()
    while (a > 0 and b > 0 and a >= b) or (a < 0 and b < 0 and a <= b):
        a = restar(a, b)
        cociente = sumar(cociente, 1)

    return -cociente if negativo else cociente