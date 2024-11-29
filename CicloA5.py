#Realice el script en Python para una aplicación que permita mediante una estructura while promediar el número
# de notas definidas por el profesor para un estudiante y determinar si aprueba o no la asignatura.
# Aprueba con 4,5 en un rango de 0 a 5.0

def calcular_promedio(notas):

  return sum(notas) / len(notas)

def determinar_aprobacion(promedio):

  if promedio >= 4.5:
    return "Aprobado"
  else:
    return "Reprobado"

if __name__ == "__main__": #Este bloque de código se ejecuta solo si el archivo se ejecuta directamente, no si se importa como módulo.
  cantidad_notas = int(input("Ingrese la cantidad de notas: "))
  notas = []

  i = 1
  while i <= cantidad_notas:
    nota = float(input(f"Ingrese la nota {i}: "))
    notas.append(nota) #Agrega la nota ingresada a la lista
    i += 1

  promedio = calcular_promedio(notas)
  resultado = determinar_aprobacion(promedio)

  print(f"El promedio del estudiante es: {promedio:.2f}")
  print(f"El estudiante está: {resultado}")