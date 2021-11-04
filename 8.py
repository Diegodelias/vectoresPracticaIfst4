# 8) Ingresar 10 números y guardarlos en un vector nuevo. Al finalizar informar el promedio.

resultado=[]
acumulador=0
for i in range(10):
     numTemp= input("Ingresar número: ")
     resultado.append(numTemp)


for j in range(len(resultado)):
    acumulador = acumulador + int(resultado[j])


print(len(resultado))
promedio = acumulador / len(resultado)
print("el promedio es", promedio)