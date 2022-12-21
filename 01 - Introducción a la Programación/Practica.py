#Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no.

edad = int(input("Introduce tu edad: "))
if edad < 18:
  print("Eres menor de edad y no tributas")
elif edad >= 18:
  ingreso = int(input("Introduce tu ingreso mensual: "))
  if ingreso >= 1000:
    print("Tributas")
  elif ingreso < 1000:
    print("No tributas")