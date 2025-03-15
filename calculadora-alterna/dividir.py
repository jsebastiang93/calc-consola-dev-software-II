from suma import sumar
from resta import restar

def dividir (a,b):
    while a > b:
        a = restar(a, b)
        c =+ 1