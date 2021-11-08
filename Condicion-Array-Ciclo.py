#arreglos
carnet=[]
nombre=[]
apellido=[]
nota1=[]
nota2=[]
nota3=[]
nota4=[]
promedio=0
num=3
#almacenando datos en arreglos utilizando ciclo
for i in range(num):
    carnet.append(int(input("Ingrese numero de carnet del alumno: ")))
    nombre.append(input("Ingrese nombre del alumno: "))
    apellido.append(input("Ingrese apellido de alumno: "))
    nota1.append(float(input("Ingrese nota final del 1er.Bimestre: ")))
    nota2.append(float(input("Ingrese nota final del 2do.Bimestre: ")))
    nota3.append(float(input("Ingrese nota final del 3er.Bimestre: ")))
    nota4.append(float(input("Ingrese nota final del 4to.Bimestre: ")))
    print("__________________________________________________________")

#calculo de promedio
for x in range(3):
    promedio=(nota1[x] + nota2[x] + nota3[x] + nota4[x])/4
    print("Nombre alumno: ",nombre[x],"",apellido[x]," Promedio obtenido: ",promedio)
    if promedio>70:
        print("Felicidades, has ganado tu curso")
    else:
        print("Lo siento, has reprobado el curso, debes de estudiar mas.")
