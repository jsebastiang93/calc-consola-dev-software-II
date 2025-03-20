# operaciones.py

def sumar(a, b):
    """Suma dos números usando incremento y decremento."""
    while b != 0:
        carry = a & b
        a = a ^ b
        b = carry << 1
    return a

def restar(a, b):
    """Resta dos números usando el complemento a dos."""
    while b != 0:
        borrow = (~a) & b
        a = a ^ b
        b = borrow << 1
    return a

def multiplicar(a, b):
    """Multiplica dos números usando sumas repetitivas."""
    resultado = 0
    negativo = (a < 0) ^ (b < 0)  # Determina si el resultado será negativo
    a, b = abs(a), abs(b)
    
    for _ in range(b):
        resultado = sumar(resultado, a)
    
    return -resultado if negativo else resultado

def dividir(a, b):
    """Divide dos números usando restas sucesivas."""
    if b == 0:
        raise ValueError("No se puede dividir por cero")
    
    negativo = (a < 0) ^ (b < 0)  # Determina si el resultado será negativo
    a, b = abs(a), abs(b)
    cociente = 0

    while a >= b:
        a = restar(a, b)
        cociente = sumar(cociente, 1)
    
    return -cociente if negativo else cociente