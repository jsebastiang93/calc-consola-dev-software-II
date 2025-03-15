def sumar(a, b):
    """Suma dos números usando incremento y decremento."""
    while b != 0:
        carry = a & b
        a = a ^ b
        b = carry << 1
    return a
