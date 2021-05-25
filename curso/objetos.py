class animal:
    def __init__(self, vivo):
        self.vivo = vivo

    def esta_vivo(self):
        print("Esta vivo: " + self.vivo)

class gato(animal):
    def correr(self):
        print("El gato esta corriendo")
    def dormir(self):
        print("El gato esta durmiendo")
    def ronronear(self):
        print("El gato esta ronroneando")
        
garfield = gato("si")

garfield.esta_vivo()
garfield.ronronear()
garfield.dormir()
garfield.correr()
