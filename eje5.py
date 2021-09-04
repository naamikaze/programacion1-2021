from dataclasses import dataclass
from typing import List

@dataclass
class Fecha:
    dia: int
    mes: int 
    anio: int

@dataclass
class Horario:
    horas: int
    minutos: int
    segundos: int

@dataclass
class Producto:
    nombre: str
    precio_u: int
    fecha_prod: Fecha

class HoraIncorrecta(Exception):
    pass

class MinutoIncorrecto(Exception):
    pass

class SegundoIncorrecto(Exception):
    pass

def validar_horario(hora, minuto, segundo):
    if hora < 0 or hora > 23:
        raise HoraIncorrecta()
    if minuto < 0 or minuto > 60:
        raise MinutoIncorrecto()
    if segundo < 0 or segundo > 60:
        raise SegundoIncorrecto()

def main():
    validar = 0
    while True:
        try:
            primeravez=True
            for x in range(2):
                hora=int(input('Ingrese una hora: '))
                minuto=int(input('Ingrese un minuto: '))
                segundos=int(input('Ingrese un segundo: '))
                validar = validar_horario(hora, minuto, segundos)
                if primeravez == True:
                    fecha=Fecha(hora,minuto,segundos)
                else:
                    fecha2=Fecha(hora,minuto,segundos)
                primeravez = False

            total = fecha - fecha2
            print('Hay una diferencia de ', total, 'horas')
            break

        except HoraIncorrecta:
            print('La hora ingresada no es correcta. ')
        except MinutoIncorrecto:
            print('Los minutos ingresados no son correctos. ')
        except SegundoIncorrecto:
            print('Los segundos ingresados no son correctos. ')
    ...

if __name__ == '__main__':
    main()
    ...

