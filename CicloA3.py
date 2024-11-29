#Realice el script en Python para una aplicación que permita mostrar en pantalla los números del 1 al 30 
#escribiendo un salto de línea cada 7 números. Salto de Línea = \n

def salto():
    for i in range(1, 31):
        print(i, end=" ")
        if i % 7 == 0:
            print()
salto()

        