import suma.py

def multiplicar(a, b):
    
    resultado = 0
    negativo = False  

    # Determina si el resultado será negativo basado en los signos de a y b
    if (a < 0) ^ (b < 0):  # XOR: True si uno es negativo y el otro positivo
        negativo = True

    # Ajusta los operandos para trabajar solo con sus magnitudes
    while b != 0:
        if b & 1:  # Si el bit menos significativo de b es 1, suma a al resultado
            resultado = sumar(resultado, a)
        a <<= 1  # Desplaza a a la izquierda (equivalente a multiplicar por 2)
        b >>= 1  # Desplaza b a la derecha (equivalente a dividir por 2)

    return -resultado if negativo else resultado