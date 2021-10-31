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
            turno = Turnos([linea.turnos], [linea.maquina], [linea.prof], [linea.deff])
            lista.append(turno)

    return lista



        



def main():
    leer = leer_archivo()
    print(leer)
    ...

if __name__ == '__main__':
    main()