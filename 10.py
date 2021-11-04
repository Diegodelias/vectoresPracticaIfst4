# 10) Ingresar números hasta que se ingresa un número negativo. Guardar los números en un vector,
# ignorar el último número negativo. Al finalizar informar la diferencia entre el primer elemento y el
# segundo, entre el segundo elemento y el tercero… hasta informar la diferencia entre el anteúltimo
# elemento y el último.

vector=[]
numero= 0


while numero >= 0:
    numero=int(input("Ingresar número: "))
    
    if numero >= 0:
        vector.append(numero)

print(vector)
 

for i in range(len(vector)):
    # print(vector[i])
    # print(vector[i-1])
    if (i+1) < len(vector):
        print(vector[i]-(vector[i+1]))

