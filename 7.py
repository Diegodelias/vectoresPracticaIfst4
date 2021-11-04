# 7) Ingresar 10 números y guardarlos en un vector nuevo. Al finalizar informar el número mayor y el
# número menor.

resultado = []
menor = 9999999999
mayor = -9999999999
for i in range(10):
    numTemp= input("Ingresar número: ")
    resultado.append(numTemp)
print(resultado)
for j in range(len(resultado)):
    if  int(resultado[j]) < int(menor):
        menor = resultado[j]
    if int(resultado[j]) > int(mayor):
        mayor = resultado[j]


print('El numero menor es ' ,menor)
print('El numero mayor es ',mayor)
