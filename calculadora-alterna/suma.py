def sumar(a, b):
    
    while b > 0:
        a += 1
        b -= 1
    while b < 0:
        a -= 1
        b += 1
    return a
