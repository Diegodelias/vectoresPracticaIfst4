# 5) Dado el siguiente vector [8, 10, 15, 2, 8, 6, 21, 5], informar los dos números mayores.

vector = [8, 10, 15, 2, 8, 6, 21, 5]
for i in range (len(vector)):
    for j in range(len(vector)):
        temp=None
        if vector[i] > vector[j]:
            temp = vector[j]
            vector[j]= vector[i]
            vector[i] = temp


print("El primer número mayor es " , vector[0])
print("El segundo número mayor es " , vector[1])