def restar(a, b):
    """Resta dos números usando el complemento a dos."""
    while b != 0:
        borrow = (~a) & b
        a = a ^ b
        b = borrow << 1
    return a