# 1) Corregir el código para cumplir con la consigna.
# Ingresar 5 números y guardarlos en un vector. Al finalizar informar el número menor.
# vector = []
# for n in range(5):
#  nuevo = float(input("Ingrese el siguiente número:"))
#  vector.append(nuevo)
# menor=0
# for elemento in vector:
#  if elemento < menor:
#  menor=elemento
# print ("El número menor es:", menor)

vector = []
for n in range(5):
 nuevo = int(input("Ingrese el siguiente número:"))
 vector.append(nuevo)
menor=99999
for elemento in vector:
 if elemento < menor:
    menor=elemento
print ("El número menor es:", menor)