#Realice el script en python para una aplicacion que permita convertir de dolares a pesos, con una tasa de cambio de $3.934
#y mediante una estructura while preguntar si desea seguir realizando otras conversiones o no para que de esta manera 
#continue con la ejecucion o finalice la aplciacion.

def convertir_dolares_a_pesos(dolares):

  tasa_cambio = 3.934  # Tasa de cambio fija
  pesos = dolares * tasa_cambio
  return pesos

if __name__ == "__main__":
  while True:
    try:
      dolares = float(input("Ingrese la cantidad de dólares a convertir: "))
      pesos = convertir_dolares_a_pesos(dolares)
      print(f"{dolares} dólares equivalen a {pesos:.2f} pesos colombianos.")

      continuar = input("¿Desea realizar otra conversión? (si/no): ")
      if continuar.lower() != 'si':
        break
    except ValueError:
      print("Por favor, ingrese un valor numérico válido.")