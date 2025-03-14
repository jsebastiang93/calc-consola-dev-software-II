import unittest
import operaciones  # Importamos el módulo a probar

class TestOperaciones(unittest.TestCase):

    def test_sumar(self):
        self.assertEqual(operaciones.sumar(2, 3), 5)
        self.assertEqual(operaciones.sumar(-5, 3), -2)

    def test_restar(self):
        self.assertEqual(operaciones.restar(7, 4), 3)
        self.assertEqual(operaciones.restar(-3, -6), 3)

    def test_multiplicar(self):
        self.assertEqual(operaciones.multiplicar(4, 3), 12)
        self.assertEqual(operaciones.multiplicar(-4, 3), -12)
        self.assertEqual(operaciones.multiplicar(0, 7), 0)

    def test_dividir(self):
        self.assertEqual(operaciones.dividir(10, 2), 5)
        self.assertEqual(operaciones.dividir(7, 2), 3)  # División entera
        with self.assertRaises(ValueError):
            operaciones.dividir(10, 0)  # División por cero debe lanzar error

if __name__ == '__main__':
    unittest.main()