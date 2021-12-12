class valor_no_encontrado(Exception):
    ...

def verificar_txt(texto):
    cont = 0
    for i in range(len(texto)):
        if texto[i] == ' ':
            cont += 1
    return cont

def ejercicio1():
    texto = 'Hola que tal'
    verif = verificar_txt(texto)
    print(f'Cantidad de espacios en el texto: {verif}')

def ejer6a(matriz):
    acum = 0
    for fila in range(len(matriz)):
        for columna in range(len(matriz[fila])):
            if matriz[fila][columna] > 0:
                acum += matriz[fila][columna]
    return acum

def ejer6b(matriz, buscar):
    f=0
    c=0
    for fila in range(len(matriz)):
        for columna in range(len(matriz[fila])):
            if matriz[fila][columna] == buscar:
                f=fila
                c=columna
                return f,c
    raise valor_no_encontrado

def ejercicio2():
    matriz = [
        [-5,-40,-3,-2,-1],
        [1,2,3,4,5],
        [6,7,8,21,10],
        [11,12,13,14,15],
        [16,17,18,20,31]]
    ej6a = ejer6a(matriz)
    print(f'Suma de nros positivos: {ej6a}')
    buscar = 21
    try:
        eje6b = ejer6b(matriz, buscar)
        print(f'Valor encontrado en Fila: {eje6b[0]} Columna: {eje6b[1]}')
    except valor_no_encontrado:
        print(f'No se ha encontrado el valor.')

def buscar_mayor(lista):
    mayor = lista[0]
    posicion = 0
    vector = []
    for x in range(len(lista)):
        if lista[x] > mayor:
            mayor = lista[x]
            posicion = x

    vector.append(mayor)
    vector.append(posicion)
    return vector 

def ejercicio3():
    lista = [0,1,2,3,40,5,60,7,8,9]
    verif = buscar_mayor(lista)
    print(f'Se encontró el mayor en: {verif}')

def ejercicio4():
    x = 1
    acum = 0
    while x != 0:
        num = int(input('Ingrese nro: '))
        if num != -1:
            acum += num
        else:
            x=0

    print(f'Suma de todos los nros ingresados: {acum}')
           
def main():
    ejercicio1()
    ejercicio2()
    ejercicio3()
    ejercicio4()

if __name__ == '__main__':
    main()
