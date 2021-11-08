from Mascota import Mascota

class Conejo(Mascota):
#atributos
    raza= ""
    sonido=""
    comida=""

#metodos
    def imprimirSaludo(self):
        print("Hola, soy un lindo conejito")

    def setRaza(self, raza):
        self.raza = raza

    def getRaza(self):
        return self.raza

    def setSonido(self, sonido):
        self.sonido = sonido

    def getSonido(self):
        return self.sonido

    def setComida(self, comida):
        self.comida = comida

    def getComida(self):
        return self.comida
