#def sumaAcumulada (lista): #<- Acá va los valores que asigno abajo, por eso puse lista
#    listaAcumulada=[]
#   contador = 0
#    for i in lista: #<- Hace un for recorriendo los valores que recibió de lista cuando hice el def
#        contador += i #<- Hago un acumulador con el valor que actualmente está recorriendo la lista 
#        listaAcumulada.append(contador) #<- Meto el valor del acumulador en la lista
#    return listaAcumulada  #<- Devuelvo los valores de la lista
#
#print(sumaAcumulada([1,2,3])) #<- Le asigno que valores quiero que se usen en la funcion de lista, por ende estála palabra lista en la linea 1 y en el for de la linea 4


#Mi versión sería así:

def funcion(nros):
    acum = 0
    lista = []
    for i in nros:
        acum+=i #<- La variable sin corchetes []
        lista.append(acum)

    print()
    print(f'Primera lista: {nros}')
    print()
    print(f'Segunda lista ya acumulada: {lista}')
    ...

def main():
    funcion([1,2,3])
    ...

main()



#La que hice originalmente

#def dou():
#    lista1=[]
#    lista2=[]
#    acumulador=0
#    cant = int(input('Ingrese la cantidad de nros que desea ingresar: '))
#    for x in range(len(cant)):
#        num = int(input('Ingrese el {x} numero: '))
#        lista1.append(num)
#        acumulador+=num
#        lista2.append(acumulador)
#    print()
#    print(f'Primera lista {lista1}')
#   print()
#    print(f'Segunda lista {lista2}')

        



    