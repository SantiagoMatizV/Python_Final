#En un almacén se descuenta 20% del precio al cliente si el valor a pagar es mayor a $20.000.
#Dado un valor de precio, muestre lo que debe pagar el cliente.


def calcular_precio_final(precio_inicial):
  
  if precio_inicial > 20000:
    descuento = precio_inicial * 0.2  # 20% de descuento
    precio_final = precio_inicial - descuento
  else:
    precio_final = precio_inicial

  return precio_final

precio = float(input("Ingrese el precio del producto: "))

precio_a_pagar = calcular_precio_final(precio)

print(f"El precio final a pagar es: ${precio_a_pagar:.2f}")