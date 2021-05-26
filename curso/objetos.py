import unittest

class animal:
    def __init__(self, vivo):
        self.vivo = vivo

    def esta_vivo(self):
        print("Esta vivo: " + self.vivo)


class gato(animal):
    def correr(self):
        print("El gato esta corriendo")

    def dormir(self):
        print("ZZZZzzzzz ZZZZZZzzzzz")

    def ronronear(self):
        print("RRRR RRRRR RRRRR RRRRR")


garfield = gato("si")

garfield.esta_vivo()
garfield.ronronear()
garfield.dormir()
garfield.correr()

class TestResult(unittest.TestCase):
    
    def test_vivo(self):
        self.assertEqual(garfield.vivo,"si")
        