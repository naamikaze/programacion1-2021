import random
from dataclasses import dataclass

class Correcto(Exception):
    ...

@dataclass
class Productos:
    nombre_producto: str
    categoria: int 
    stock: int 
    precio: float 


class CadenaVacia(Exception):
    ...

def buscar_mayor_matriz(matriz):
    mayor = matriz[0][0]
    f = 0
    c = 0
    for fila in range(len(matriz)):
        for columna in range(len(matriz[fila])):
            if matriz[fila][columna] > mayor:
                mayor = matriz[fila][columna]
                f = fila
                c = columna
    return [f,c] 


def ejercicio4():
    matriz = [[230,45,53],[27,21,86],[54,82,2000]]
    mayor = buscar_mayor_matriz(matriz)
    print(f'Fila: {mayor[0]} Columna: {mayor[1]}')
    ...

def esvocal(letra):
    if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
        return True
    return False

def verificar_vocales(texto):
    cont = 0

    for letra in range(len(texto)):
        if esvocal(texto[letra]):
          cont += 1
    
    if cont > 0:
        print(f'Cantidad de vocales: {cont}')
    else:
        raise CadenaVacia

def ejercicio5():
    texto='hl'
    try:
        verificar_vocales(texto)
    except CadenaVacia:
        print('No se encontraron vocales :)()()()')

def generar_productos():
    lista = []
    for x in range(10):
        lista.append(Productos(
            "Producto nro "+str(x),
            random.randint(1,5),
            random.randint(1,50),
            random.uniform(1,300),
        ))
    return lista

def imprimir(productos):
    for linea in productos:
        if linea.categoria == 1:
            print(f'{linea.nombre_producto} | {linea.stock} | ${linea.precio}')

def ejercicio62(lista, buscar):
    mayor = -1
    mayornombre = ''
    mayorprecio = ''
    for linea in lista:
        if linea.categoria == buscar:
            if linea.stock > mayor:
                mayor = linea.stock
                mayornombre = linea.nombre_producto
                mayorprecio = linea.precio

    print(f'Nombre: {mayornombre} Precio: {mayorprecio} Stock: {mayor}')
    ...

def promedio(lista):
    promedio=0
    cont=0
    for linea in lista:
        if linea.categoria == 3:
            promedio+=linea.precio
            cont+=1

    promedio/=cont
    print(f'El promedio de precio de HDD es: {promedio}')


def ejercicio6():
    productos = generar_productos()
    imprimir(productos)
    try:
        buscar = int(input('Ingrese una opcion (1, 2, 3, 4 o 5): '))
        ejercicio62(productos,buscar)
        if buscar < 1 or buscar > 5:
            raise Correcto
    except Correcto:
        print('Ingrese una opcion valida')
    
    promedio(productos)
    
    ...

def main():
    #ejercicio4()
    #ejercicio5()
    ejercicio6()

    ...


if __name__ == '__main__':
    main()