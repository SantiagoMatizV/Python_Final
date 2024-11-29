#Realice el seudocódigo y el script en Python para una aplicación que permita a partir de un número
#que digite el usuario por teclado (número entero n), calcular su factorial (n!).


def factorial(n):
    if n<0:
        print("El numero debe ser positivo")
        return None
    elif n == 0:
        return 1
    else:
        factorial = 1
        for i in range(1, n + 1):
            factorial *= i
        return factorial

Num = int(input("Digite el numero a calcular: "))


Resultado = factorial(Num)
if Resultado is not None:
    print("El factorial de", Num, "es", Resultado)

    factorial ()