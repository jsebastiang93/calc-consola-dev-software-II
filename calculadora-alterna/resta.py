# resta.py
from suma import sumar

def restar(a, b):
    if a < 0 or b < 0:
        return "Advertencia: Solo se permiten números positivos."
    
    if a >= b:
        c = 0
        while a != b:
            c += 1  
            a -= 1  
        return c
    else:
        return "Advertencia: La resta no es posible ya que el primer número es menor al segundo número."