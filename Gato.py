from Mascota import Mascota

class Gato(Mascota):
#atributos
    raza = " "
    sonido =" "

#metodos
    def imprimirSaludo(self):
        print("Hola, soy un lindo gatito")

    def setRaza(self,raza):
        self.raza = raza

    def getRaza(self):
        return self.raza

    def setSonido(self,sonido):
        self.sonido = sonido

    def getSonido(self):
        return self.sonido
