# 3) Dado el siguiente vector , informar el número mayor y el número menor.



vector =  [5, 9, 15, 2, -8, 3, -112]
for i in range (len(vector)):
    for j in range(len(vector)):
        temp=None
        if vector[i] < vector[j]:
            temp = vector[j]
            vector[j]= vector[i]
            vector[i] = temp


print("El número menor es " , vector[0])
print("El número mayor es " , vector[len(vector)-1])