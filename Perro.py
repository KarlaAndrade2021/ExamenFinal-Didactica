from Mascota import Mascota

class Perro(Mascota):
#atributo
    raza = ""

#metodo
    def imprimirSaludo(self):
        print("Hola, soy un lindo perrito")
        
    def setRaza(self,raza):
        self.raza = raza

    def getRaza(self):
        return self.raza
