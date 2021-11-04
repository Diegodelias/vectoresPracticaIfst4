# 6) Dado el siguiente vector [5,-2, 8, 10, -4, 13, 21], a cada elemento, sumarle 2, y guardarlo en un
# nuevo vector

vector = [5,-2, 8, 10, -4, 13, 21];


# fucnio sumar
# if len(vector)>0
#  return resultado

# else:
#     resultado.push(vector[0])
#     vector = slice(vector[1])
    
#     sumar(vector)

resultado = []
def sumarDosAvector(vector):
    if len(vector) <= 0:
        return resultado
    else:
        resultado.append((vector[0]+2))
        vector = vector[1:len(vector)]
        print(vector)
   
        return sumarDosAvector(vector)


print(sumarDosAvector(vector))
