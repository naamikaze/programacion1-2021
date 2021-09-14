from dataclasses import dataclass
from typing import List

@dataclass
class departamentos:
    nro_unidad: int
    desc: str
    mt_cuadrados: int
    estado: int 
    precio_venta: int

def listado():
    for x in departamentos:
        if departamentos.estado == '1':
            print(departamentos[x])
    ...

def carga_depto(deptos):

    for jskjsk in range():

        departamentos.nro_unidad() = len(deptos) + 1
        departamentos.desc(input('Ingrese una descripción: '))
        departamentos.mt_cuadrados(int(input('Ingrese los metros cuadrados: ')))
        departamentos.estado(input('Ingrese el estado (1-Libre 2-Reservado 3-Vendido): '))
        departamentos.precio_venta(int(input('Ingrese el precio de venta: ')))

def menu():
    ...

def main():
    deptos = []
    carga_depto(deptos)
    listado()
    ...

if __name__ == '__main__':
    main()
    ...