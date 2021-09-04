#Ordenamiento

def ordenar_vector(vector):

    for j in range(len(vector)-1): #Repito todo así se acomoda la cantidad de veces que es debida, porque si no lo hago solo me acomoda un numero solo.

        for i in range(len(vector)-1): #Pongo el -1 para que no compare el ultimo nro y rompa todo 
            if vector[i] > vector[i+1]: #Si el numero en tal posicion es mayor al que le sigue...
                aux = vector[i] #Hago un auxiliar

                vector[i] = vector[i+1] #Lo cambio a la proxima posicion del vector.

                vector[i + 1] = aux 

    print(vector)
    ...

#Busqueda binaria (SOLO SIRVE EN VECTORES ORDENADOS) 
def busqueda_binaria(valorBuscado, vector):
    inicio = 0
    final = len(vector) - 1

    while final >= inicio:

        medio = (final+inicio) // 2 

        if vector[medio] == valorBuscado:
            return medio

        if vector[medio] > valorBuscado:
            final = medio - 1

        if vector[medio] < valorBuscado:
            inicio = medio + 1

    return -1


#General para todo

def main():
    arreglo_desordenado = [2, 9, 8, 3, 7, 1] #Numeros que voy a ordernar
    print('Principal')
    print(arreglo_desordenado)
    ordenar_vector(arreglo_desordenado)
    indice = busqueda_binaria(3, arreglo_desordenado)
    print(indice)

if __name__ == '__main__':
    main()
    ...





