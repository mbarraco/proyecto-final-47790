

# Ejemplo: [1, 2, 3, 4, 5] -> 5
# Ejemplo: [1, 2 , 25] -> 25

def encontrar_max(numeros):

    max = -1
    for numero in numeros:
        if numero > max:
            max = numero

    print(max)


encontrar_max([1,2,3,4,5])
encontrar_max([1, -2 , 25])
