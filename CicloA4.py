#Realice  el script en Python para una aplicación que permita preguntarle al usuario una cantidad de dinero a invertir,
#el interés anual y el sistema muestre por pantalla el capital obtenido en la inversión.

def calcular_inversion(capital_inicial, tasa_interes, num_años):
  
  capital_final = capital_inicial * (1 + tasa_interes) ** num_años
  return capital_final

if __name__ == "__main__":
  try:
    capital_inicial = float(input("Ingrese la cantidad a invertir: "))
    tasa_interes = float(input("Ingrese la tasa de interés anual (ejemplo: 5 para 5%): ")) / 100
    num_años = int(input("Ingrese el número de años de la inversión: "))

    capital_final = calcular_inversion(capital_inicial, tasa_interes, num_años)
    print(f"El capital obtenido después de {num_años} años es: {capital_final:.2f}") #.2f es para que sepa que el numero sera de dos digitos y que es un float
  except ValueError:
    print("Por favor, ingrese solo números.")

    calcular_inversion(capital_inicial, tasa_interes, num_años)