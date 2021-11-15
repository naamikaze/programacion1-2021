from dataclasses import dataclass
import random

@dataclass
class Alumnos:
    apellido: str
    nombre: str
    edad: int 
    carrera: int
    aprobadas: int

@dataclass
class Elcapo:
    apellido: str
    nombre: str
    edad: int 

class CadenaVacia(Exception):
    ...

class Incorrecto(Exception):
    ...

class ValorNoEncontrado(Exception):
    ...

def verificar(texto):
    if texto == '0' or texto == '1' or texto == '2' or texto == '3' or texto == '4' or texto == '5' or texto == '6' or texto == '7' or texto == '8' or texto == '9':
        return True 
    else:
        return False

def contiene_numeros(texto):
    if len(texto) == 0:
        raise CadenaVacia
    cont=0
    for x in range(len(texto)):
        if verificar(texto[x]):
            cont+=1
    if cont > 0: 
        print('True')
    else:
        print('False')
    ...

def ejercicio1():
    texto = input('Ingrese sexo: ')
    try:
        contiene_numeros(texto)
    except CadenaVacia:
        print('La cadena está vacia')


def buscar_valor_matriz(buscar, matriz):
    for fila in range(len(matriz)):
        for columna in range (len(matriz[fila])):
            if buscar == matriz[fila][columna]:
                return fila, columna

    raise ValorNoEncontrado


def ejercicio2():
    try:
        matriz = [[0,8,9], [1,2,3], [4,5,7]]
        buscar = int(input('Que valor querés buscar: '))
        buscacoco = buscar_valor_matriz(buscar, matriz)
        print(f'Fila: {buscacoco[0]} Columna: {buscacoco[1]}')
    except ValorNoEncontrado:
        print('No se encuentra el valor, gil')
    ...

def crear_alumnos():
    lista=[]
    for x in range(10):

    #Esto andaria en un mundo alterno
        '''
        alumno = ['','',0,0,0]
        alumno.apellido = 'Apellido'+str(x)
        alumno.nombre = 'Nombre'+str(x)
        alumno.edad = random.randint(20, 40)
        alumno.carrera = random.randint(1,3)
        alumno.aprobadas = random.randint(1,5)
        '''

        lista.append(Alumnos(
            "Apellido"+str(x),
            "Nombre"+str(x),
            random.randint(20,50),
            random.randint(1,3),
            random.randint(0,30),
        ))
    return lista

def ej31(lista):
    listarda=[]
    for linea in lista:
        if linea.carrera == 1 and linea.edad >= 30:
            print(f'{linea.nombre} | {linea.apellido} | {linea.edad}')
    ...

def ej32(lista):
    promedio = 0
    cant = 0
    for alumno in lista:
        if alumno.carrera == 3:
            promedio+=alumno.edad
            cant +=1
    promedio = promedio / cant
    print(f'Promedio de programacion: {promedio}')


def ej33(lista, buscar):
    #alumnos=Elcapo('','', 0)
    alumno_mayor = None
    mayor = -1
    for alumno in lista:
        if alumno.carrera == buscar:
            if alumno.aprobadas > mayor:
                mayor = alumno.aprobadas
                alumno_mayor = alumno

                #datasclass
                #alumnos.apellido = alumno.apellido
                #alumnos.nombre = alumno.nombre
                #alumnos.edad = alumno.edad

    print(f'Nombre: {alumno_mayor.nombre}')
    print(f'Apellido: {alumno_mayor.apellido}')
    print(f'Edad: {alumno_mayor.edad}')

    


def ejercicio3():
    alumnos = crear_alumnos()
    ej31(alumnos)
    ej32(alumnos)
    try:
        buscar = int(input('Ingresa una carrera (1, 2 o 3): '))
        if buscar <= 3 and buscar > 0: #>:v
            ej33(alumnos, buscar)
        else:
            raise Incorrecto
    except Incorrecto:
        print('Ingrese una opción valida')

def main():
    #ejercicio1()
    #ejercicio2()
    ejercicio3()
    ...

if __name__ == '__main__':
    main()
    ...