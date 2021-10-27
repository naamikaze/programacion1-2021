from dataclasses import dataclass

@dataclass
class Afiliadoss:
    nombre: int
    prestacion:int 
    reintegro:int 

def leer_lista():
    lista = []
    with open('obrasocial.csv', 'r', encoding='utf-8') as arch:

        for afiliado in arch:
            campos = afiliado.split(';')
            afiliad = Afiliadoss(float(campos[0]),float(campos[1]), '0')
            lista.append(afiliad)
    return lista


def generar_importe(lista):
    nuevalist=[]
    reintegro = 0
    descuento = 0
    for pacientes in lista:
        int(pacientes.nombre)
        int(pacientes.prestacion)
        if pacientes.nombre >= 30001 and pacientes.nombre <= 60000 and pacientes.prestacion >= 300:
            reintegro = pacientes.prestacion*10
            descuento = reintegro - (reintegro*0.40)
            reintegro -= descuento
            pacientex = Afiliadoss([pacientes.nombre],[pacientes.prestacion],[reintegro])
            nuevalist.append(pacientex)
        elif pacientes.nombre >= 60001 and pacientes.nombre <= 90000: 
            reintegro = pacientes.prestacion*10
            descuento = reintegro - (reintegro*0.80)
            reintegro -= descuento
            pacientex = Afiliadoss([pacientes.nombre],[pacientes.prestacion],[reintegro])
            nuevalist.append(pacientex)
        else:
            reintegro = pacientes.prestacion*10
            pacientex = Afiliadoss([pacientes.nombre],[pacientes.prestacion],[reintegro])
            nuevalist.append(pacientex)

    return(nuevalist)


def crear_archivo(lista):
    with open('archivo_creado.txt','w',encoding='utf-8') as arch:
        arch.write(f' NroAfil | Cod.Prest | Importe. r\n')
        for pacientes in lista:
            arch.write(f'{pacientes.nombre} | {pacientes.prestacion} | {pacientes.reintegro}\n')

def mostrar_pacientes(lista):
    print()
    print(f' NroAfil | Cod.Prest | Importe. r\n')
    for pacientes in lista:
        print(f'{pacientes.nombre} , {pacientes.prestacion} , {pacientes.reintegro}\n')

def main():
    listar = leer_lista()
    importe = generar_importe(listar)
    crear = crear_archivo(importe)
    mostrar = mostrar_pacientes(importe)
    ...

if __name__ == '__main__':
    main()
    ...