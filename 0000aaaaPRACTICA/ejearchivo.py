from dataclasses import dataclass

class NoEncontrado(Exception):
    ...

@dataclass
class Videojuegos:
    titulo: str
    plataforma: str
    anio: int 
    genero: str
    ventas: int 

def importar():
    lista = []
    with open('Videojuegos.csv', 'r', encoding='utf-8') as arch:
        primeravez='True'
        for juego in arch:
            if primeravez:
                primeravez = False
                continue

            campos = juego.split(';')
            lista.append(Videojuegos(
                campos[0],
                campos[1],
                int(campos[2]),
                campos[3],
                int(campos[4]),
            ))
    return lista

def buscargenero(lista):
    cont = 0
    buscar = input('Ingrese un genero: ')
    for juego in lista:
        if juego.genero == buscar:
            cont += 1
    
    if cont > 0:
        print(f'Se han encontrado {cont} juegos con el genero {buscar}')
        return buscar
    else:
        raise NoEncontrado

def masreciente(lista, genero):
    reciente = -1
    for juego in lista:
        if juego.genero == genero:
            if juego.anio > reciente:
                reciente = juego.anio
    print(f'El lanzamiento mas reciente para el genero {genero} fue en {reciente} ')
    return reciente

def lanzados(lista,anio):
    for juego in lista:
        if juego.anio == anio:
            print(f'{juego.titulo}, {juego.genero}, {juego.ventas}')

def exportar(lista, genero):
    with open('videojuego.csv', 'w', encoding='utf-8') as arch:
        arch.write('Titulo;Plataforma;anio_lanzamiento;Genero;Unidades_Vendidas\n')
        for juego in lista:
            if juego.genero == genero:
                arch.write(f'{juego.titulo};{juego.plataforma};{juego.anio};{juego.genero};{juego.ventas}\n')
        print('Listo')

def main():
    lista = importar()
    try:
        genero = buscargenero(lista)
    except NoEncontrado:
        print('No se ha encontrado el genero especificado.')
    anio = masreciente(lista, genero)
    lanzados(lista,anio)
    exportar(lista, genero)


if __name__ == '__main__':
    main()