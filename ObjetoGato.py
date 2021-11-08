from Gato import Gato

miMascota = Gato()

miMascota.imprimirSaludo()

miMascota.setNombre(input("Ingrese nombre del gatito: "))
miMascota.setColor(input("Color del gatito: "))
miMascota.setGenero(input("Genero del gatito: "))

miMascota.setRaza(input("Raza del gato: "))
miMascota.setSonido(input("El sonido que emite el gato: "))

print("Nombre: ",miMascota.getNombre())
print("Color: ",miMascota.getColor())
print("Genero: ",miMascota.getGenero())
print("Raza: ",miMascota.getRaza())
print("Sonido que emite: ",miMascota.getSonido())
