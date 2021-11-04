# 9) Ingresar números hasta que se ingrese un 0 (cero). Guardar los números ingresados en un vector,
# ignorar el 0 (cero). Al finalizar informar el número mayor, el número menor y el promedio.
vector=[]
numero= None

def mayorYmenor(vector):
    menor = 9999999999
    mayor = -9999999999
    for j in range(len(vector)):
        if  int(vector[j]) < int(menor):
            menor = vector[j]
        if int(vector[j]) > int(mayor):
            mayor = vector[j]

    return mayor , menor

def promedio(vector):
    acumulador=0
    for j in range(len(vector)):
        acumulador = acumulador + int(vector[j])
    return (acumulador // len(vector))


while numero != 0:
    numero=int(input("Ingresar número: "))
    
    if numero != 0:
        vector.append(numero)
 


mayorYmenorFinal = mayorYmenor(vector)
print('el numero mayor es ' , mayorYmenorFinal[0])
print('el numero menor es ' ,mayorYmenorFinal[1])
print('el promedio es ' , promedio(vector) )
