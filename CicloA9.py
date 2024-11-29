#Un aprendiz desea saber cuál será su calificación final en cierta asignatura.
#Las notas que se manejan son de 0 a 5.


def calcular_calificacion_final():

    nombre = input("Ingrese su nombre: ")
    asignatura = input("Ingrese el nombre de la asignatura: ")

    nota1 = float(input("Ingrese la nota del primer examen (0-5): "))
    while nota1 < 0 or nota1 > 5:
        print("La nota debe estar entre 0 y 5.")
        nota1 = float(input("Ingrese la nota del primer examen (0-5): "))

    nota2 = float(input("Ingrese la nota del segundo examen (0-5): "))
    while nota2 < 0 or nota2 > 5:
        print("La nota debe estar entre 0 y 5.")
        nota2 = float(input("Ingrese la nota del segundo examen (0-5): "))

    nota3 = float(input("Ingrese la nota del tercer examen (0-5): "))
    while nota3 < 0 or nota3 > 5:
        print("La nota debe estar entre 0 y 5.")
        nota3 = float(input("Ingrese la nota del tercer examen (0-5): "))

    calificacion_final = (nota1 * 0.3) + (nota2 * 0.3) + (nota3 * 0.4)


    if calificacion_final >= 4.0:
        aprobado = "APROBADO"
    else:
        aprobado = "REPROBADO"

    # Mostrar resultados
    print(f"\nResultados para {nombre} en la asignatura {asignatura}:")
    print(f"Calificación final: {calificacion_final:.2f}")
    print(f"Estado: {aprobado}")

calcular_calificacion_final()