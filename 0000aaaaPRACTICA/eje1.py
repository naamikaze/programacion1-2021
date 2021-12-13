from dataclasses import dataclass
import random

@dataclass
class Alumnos:
    apellido: str
    nombre: str
    edad: str
    carrera: str
    aprobadas: str

class ValorNoEncontrado(Exception):
    ...

def verifnum(caracter):
    if caracter == '0' or caracter == '1' or caracter == '2' or caracter == '3' or caracter == '4' or caracter == '5' or caracter == '6' or caracter == '7' or caracter == '8' or caracter == '9':
        return True
    else:
        return False

def ejercicio1(cadena):
    cont = 0
    for l in range(len(cadena)):
        if verifnum(cadena[l]):
            cont+=1
    if cont > 0:
        print('True')
    else:
        print('False')

def buscar_valor_matriz(buscar, matriz):
        for fila in range(len(matriz)):
            for columna in range(len(matriz[fila])):
                if matriz[fila][columna] == buscar:
                    return fila, columna
        raise ValorNoEncontrado


def ejercicio2():
    buscar=10
    matriz = [[1,2,3],[4,5,6],[7,8,9]]
    try:
        pos = buscar_valor_matriz(buscar, matriz)
        print(f'Fila: {pos[0]} Columna: {pos[1]}')
    except ValorNoEncontrado:
        print('No se ha encontrado el valor en la matriz.')

def crearmatriz():
    lista = []
    for x in range(10):
        lista.append(Alumnos(
            'Apellido'+str(x),
            'Nombre'+str(x),
            random.randint(20, 50),
            random.randint(1, 3),
            random.randint(0,30),
        ))
    return lista

def ej31(lista):
    for alumno in lista:
        if alumno.edad >= 30:
            print(alumno.nombre, alumno.apellido, alumno.edad)

def ej32(lista):
    promedio=0
    cont = 0
    for alumno in lista:
        if alumno.carrera == 3:
            promedio += alumno.edad
            cont +=1
    promedio /= cont
    return promedio

def ej33(lista):
    mayor=-10
    nombremayor = ''
    apellidomayor = ''
    edadmayor=0

    for alumno in lista:
        if alumno.aprobadas > mayor:
            mayor = alumno.aprobadas
            nombremayor = alumno.nombre
            apellidomayor = alumno.apellido
            edadmayor = alumno.edad

    print(nombremayor, apellidomayor, edadmayor)


def ejercicio3():
    lista = crearmatriz()
    print(lista)

    ej31(lista)
    promedio = ej32(lista)
    print(f'El promedio de edad de alumnos es: {promedio}')
    ej33(lista)


def main():
    ejercicio1('hola que tal coo te va')
    ejercicio2()
    ejercicio3()
    ...

if __name__ == '__main__':
    main()