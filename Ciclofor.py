#Manejo del Ciclo For.
""" Frutas = ["manzanas","peras","bananas"]
for num in Frutas:
    print(num) """ 
#Con ALT + SHIFT + A, lo comentas

#Para imprimir los datos de un array
""" Variable = "Si no ven el error, rebovinan para verlo de nuevo."
for v in Variable:
    print(v) """

#Para imprimir una cantidad especifica dentro de la variable.

""" for num in range(12, 1, -1):
    print(num) """

#Primera tabla de multiplicar

Tabla = int(input("Digite el numero a multiplicar: "))
for num in range(1, Tabla+1): #Este rango va de 1 a 10
    for num2 in range (0, 11):
        print(f"{num} * {num2} = {num*num2}")