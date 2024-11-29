#Desarrolle un programa, que pida al usuario la edad y el sexo, para que la computadora le indique si ya puede jubilarse.
#Tenga en cuenta que un Hombre se puede jubilar cuando tenga 63 años en adelante,
#en cambio, una mujer mayor se jubilará si tiene más de 54 años.

def calcular_jubilacion():
  
  edad = int(input("Ingrese su edad: "))
  sexo = input("Ingrese su sexo (M/F): ").upper() #es un método de Python para convertir una cadena a mayúsculas.

  if sexo == 'M':
    if edad >= 63:
      print("¡Puede jubilarse!")
    else:
      print("Aún no cumple los requisitos para jubilarse.")
  elif sexo == 'F':
    if edad >= 54:
      print("¡Puede jubilarse!")
    else:
      print("Aún no cumple los requisitos para jubilarse.")
  else:
    print("Sexo no válido. Por favor, ingrese 'M' para masculino o 'F' para femenino.")

calcular_jubilacion()