#Escribir un algoritmo que ingrese los siguientes datos:
#Nombre del aprendiz, asignatura, calificacion final (Tener en cuenta que las calificaciones seran del 1 al 10 y se debe mostrar en pantalla)
#Cuando la calificacion sea menir de 7 mostrar el mensaje "Reprobado", cuando la calificacion sea superior a 7 mostrar
#el mensaje "Aprobado"

def final():

    Nombre = input("Nombre del aprendiz: ")
    Asignatura = input("Ingrese la asignatura: ")

    while True:
        try:
            Calificacion = float(input("Ingrese la calificacion de 1-10: "))

            if 1 <= Calificacion <= 10:
                break
            else:
                print("La calificacion debe estar entre 1 y 10")
        except ValueError:
            print("La calificacion debe ser un numero")

    if Calificacion < 7:
                print(Nombre, "REPROBADO", Asignatura, "con", Calificacion)
    else:
                print(Nombre, "APROBADO", Asignatura, "con", Calificacion) 
final()
