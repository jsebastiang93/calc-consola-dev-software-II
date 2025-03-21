import unittest
# Importamos el módulo a probar
import suma
import resta
import multiplicar
import dividir

class TestOperaciones(unittest.TestCase):

    def test_sumar(self):
        self.assertEqual(suma.sumar(2, 3), 5)
        self.assertEqual(suma.sumar(-5, 3), "Advertencia: Solo se permiten números positivos.")

    def test_restar(self):
        self.assertEqual(resta.restar(7, 4), 3)
        self.assertEqual(resta.restar(-3, -6), "Advertencia: Solo se permiten números positivos.")

    def test_multiplicar(self):
        self.assertEqual(multiplicar.multiplicar(4, 3), 12)
        self.assertEqual(multiplicar.multiplicar(-4, 3), "Advertencia: Solo se permiten números positivos.")
        self.assertEqual(multiplicar.multiplicar(0, 7), 0)

    def test_dividir(self):
        self.assertEqual(dividir.dividir(10, 2), 5)
        self.assertEqual(dividir.dividir(7, 2), 3)  # División entera
        self.assertEqual(dividir.dividir(-10, 2), "Advertencia: Solo se permiten números positivos.")
        self.assertEqual(dividir.dividir(10, 0), "Advertencia: No es posible dividir por cero (0).")  # División por 0 ahora devuelve mensaje

if __name__ == '__main__':
    unittest.main()