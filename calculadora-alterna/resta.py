from suma import sumar

def restar(a, b):
    if a >= b:
        c = 0
        while a != b:
            c += 1  # Incrementa el contador
            a -= 1  # Decrementa a hasta que sea igual a b
        return c
    else:
        return "La resta no es posible ya que el primer número es menor al segundo número."