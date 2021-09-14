from dataclasses import dataclass
from typing import List

@dataclass
class SolicitudesClass:
    "El contenido de las solicitud"
    NumSolicitud: int
    NomCliente: str
    Zona: int
    NroTecnicoAsignado: int

def cargar_solicitud(solicitudes):
    solicitud = SolicitudesClass(0,"",0,0)
    solicitud.NumSolicitud = len(solicitudes) + 1
    solicitud.NomCliente = input("Ingrese el nombre del cliente: ")
    solicitud.Zona = input("Ingrese la zona: ")


    return solicitud


def buscar_cliente_en_otra_solicitud(solicitudes, solicitud):
    for x in range(len(solicitudes)):
        if solicitud.NomCliente == solicitudes[x].NomCliente and solicitudes[x].NroTecnicoAsignado != 0:
            return solicitudes[x].NroTecnicoAsignado



def buscar_tecnico(x,solicitudes):
    NroTecnicoAsignado = buscar_cliente_en_otra_solicitud(solicitudes, solicitudes[x])
    if NroTecnicoAsignado != 0:

        if tecnico_disponible(NroTecnicoAsignado, solicitudes):







def asignar_tecnico(solicitudes):

    for x in range(len(solicitudes)):
        if solicitudes[x].NroTecnicoAsignado != 0:
            continue

        NroTecnicoAsignado = buscar_tecnico(x, solicitudes)





def main():
    x=0
    solicitudes = []
    while x <= 1:

        solicitud = cargar_solicitud(solicitudes)
        solicitudes.append(solicitud)

        x += 1
    print(solicitudes)
    print("---------------------------------------------------")
    asignar_tecnico(solicitudes)

    print(solicitudes)

if name == 'main':
    main()
