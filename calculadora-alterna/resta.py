def restar(a, b):
    """Resta dos números usando suma y complemento a dos."""
    return a + (~b + 1)  # Equivalente a a - b