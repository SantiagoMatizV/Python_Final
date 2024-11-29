#Realice el script en Python para una aplicación que permita Imprimir los números impares,
#según el rango de datos determinado por el usuario.

def imprimir_impares(inicio, fin):
    for numero in range(inicio, fin +1):
        if numero % 2 !=0:
            print(numero)

inicio = int(input("Desde donde comienza el conteo: "))       
fin = int(input("Hasta donde llegara el conteo: "))     

if inicio > fin :
    print("El numero incial debe ser mayor al numero final")
else:
    imprimir_impares(inicio, fin)