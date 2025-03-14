# calculadora.py
import operaciones

def mostrar_menu():
    print("\n--- Calculadora ---")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

def obtener_numero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Entrada no válida. Ingresa un número entero.")

def main():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "5":
            print("Saliendo de la calculadora...")
            break

        num1 = obtener_numero("Ingresa el primer número: ")
        num2 = obtener_numero("Ingresa el segundo número: ")

        if opcion == "1":
            print(f"Resultado: {operaciones.sumar(num1, num2)}")
        elif opcion == "2":
            print(f"Resultado: {operaciones.restar(num1, num2)}")
        elif opcion == "3":
            print(f"Resultado: {operaciones.multiplicar(num1, num2)}")
        elif opcion == "4":
            try:
                print(f"Resultado: {operaciones.dividir(num1, num2)}")
            except ValueError as e:
                print(e)
        else:
            print("Opción no válida, intenta de nuevo.")

if __name__ == "__main__":
    main()