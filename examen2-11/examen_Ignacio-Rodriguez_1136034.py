#Ignacio Rodriguez
#1136034

from dataclasses import dataclass
class Invalido(Exception):
    pass

@dataclass
class Videojuego:
    titulo: str
    plataforma: str
    anio: int
    genero: str
    ventas: int

def leer_archivo():
    lista = []
    with open('Videojuegos.csv', 'r' , encoding=('utf-8')) as arch:
        primera=True
        for linea in arch:
            if primera:
                primera=False
                continue
            else:
                campos = linea.split(';')
                juegos = Videojuego(
                    campos[0],
                    campos[1],
                    int(campos[2]),
                    campos[3],
                    int(campos[4]),
                )
                lista.append(juegos)
    return(lista)

def busqueda(lista, buscar):
    cont = 0
    for linea in lista:
        if linea.plataforma == buscar:
            cont +=1
    if cont > 1:
        print(f'Existe la plataforma {buscar} en la lista con {cont} juegos.')
    else:
        raise Invalido

def buscar_plataforma(lista):
    try:
        buscar = input('Ingrese una plataforma: ')
        busqueda(lista, buscar)
        return buscar 
    except Invalido:
        print('No existe esa plataforma.')

def mas_vendido(lista, buscar):
    mayor = -1
    mayornombre=''
    mayorgenero=''
    cont = 0
    for linea in lista:
        if linea.plataforma == buscar:
            cont +=1
            if linea.ventas > mayor:
                mayor = linea.ventas
                mayornombre = linea.titulo
                mayorgenero = linea.genero

    if cont > 0:
        titu = 'Titulo'
        gene = 'Género'
        ventas = 'Ventas'

        print(f'{titu:^20}|{gene:^20}|{ventas:^15}')
        print(f'{mayornombre:^20}|{mayorgenero:^20}|{mayor:15f}')

def exportar_plataforma(lista, buscar):
    with open('listajuegos.csv', 'w', encoding='utf-8') as arch:
        arch.write(f'Titulo;Plataforma;anio_lanzamiento;Genero;Unidades_Vendidas\n')
        for linea in lista:
            if linea.plataforma == buscar:
                arch.write(f'{linea.titulo};{linea.plataforma};{linea.anio};{linea.genero};{linea.ventas}\n')

def buscar_genero(lista, buscar):
    lista =[]
    matriz = []
    ...

def main():
    leer = leer_archivo()
    plataforma = buscar_plataforma(leer)
    masventas = mas_vendido(leer, plataforma)
    exportar = exportar_plataforma(leer, plataforma)
    vendidas_genero = buscar_genero(leer, plataforma)

if __name__ == '__main__':
    main()
