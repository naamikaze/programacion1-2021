from dataclasses import dataclass

@dataclass
class Turnos:
    turnos: str
    maquina: str
    prof: str
    deff: str

def leer_archivo():
    with open('turnos.csv', 'r', encoding='utf-8') as arch:
        lista = []
        for linea in arch:
            linea = linea[:-1].split(';')
            turnacos=Turnos(0,0,0,0)
            turnacos.turnos = int(linea[0])
            turnacos.maquina = int(linea[1])
            turnacos.prof = int(linea[2])
            turnacos.deff = int(linea[3])
            lista.append(turnacos)
    return lista

def crear_matriz():
    datos = [['A', 450, 1500],['B', 350, 1425],['C', 400, 1450],['D', 250, 1000] ,['E', 200, 900]]
    return datos

def calcular(leer):
    for linea in leer:
        total_diario=0
        total_diario = linea.prof - linea.deff
        valuacion = total_diario * 77
        print(f'Maquina {linea.maquina} Total: {total_diario} Valuacion: {valuacion}')



def main():
    leer = leer_archivo()
    matriz= crear_matriz()
    reporte = calcular(leer)
    ...

if __name__ == '__main__':
    main()