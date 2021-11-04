
# 2) Dado el siguiente vector [1, 5, 3, 9, 10, 8], informar el número mayor.


vector = [1, 5, 3, 9, 10, 8,222]
# vector =[54,5,48,45,32,16,15,14,12,10]
for i in range(len(vector)):
    for j in range(len(vector)):
        temp=None
        if vector[i] > vector[j]:
            temp = vector[j]
            vector[j]= vector[i]
            vector[i] = temp

print(vector)
print("El número mayor es " , vector[0])