from dataclasses import dataclass

@dataclass
class ClassDepartamentos:
    NumUnidad: int
    Descripcion: str
    Metros2: int
    Estado: int
    PrecioVenta: float

class ValMinMaxError(Exception):
    pass

def validar_valor(numero, min=None, max=None):
    if min != None:
        if numero < min:
            raise ValMinMaxError
    if max != None:
        if numero > max:
            raise ValMinMaxError

def ingresar_numero(mensaje, min, max=None):
    while True:
        try:
            numero = int(input(mensaje))
            validar_valor(numero, min, max)
            return numero
        except ValueError:
            print("Debe ingresar un numero")
        except ValMinMaxError:
            print("Error")

def convertir_numero_a_string(mensaje, min, max):
    numero = int(input(mensaje))
    cadena = ""
    if numero < min:
        print("Ingresar numero valido")
    elif numero > max:
        print("Ingresar numero valido")

    if numero == 1:
        cadena = "Libre"
    elif numero == 2:
        cadena = "Reservado"
    elif numero == 3:
        cadena = "Vendido"

    return cadena

def cargar_departamento(departamentos):
    cargadepto = ClassDepartamentos(0,"",0,0,0.0)
    cargadepto.NumUnidad = len(departamentos)+1
    cargadepto.Descripcion = input("Ingrese una descripcion del departamento: ")
    cargadepto.Metros2 = ingresar_numero("Ingrese el tamaño del depto en metros cuadrados: ", 1)
    cargadepto.Estado = convertir_numero_a_string("Ingrese el estado del departamento: 1-Libre, 2-Reservado, 3-Vendido", 1, 3)
    cargadepto.PrecioVenta = float(input("Ingrese el precio de venta: "))

    return cargadepto

def ponderar_tamaño(departamentos,numero_reserva):
    if departamentos[numero_reserva-1].Metros2 < 100:
        return 10
    if departamentos[numero_reserva-1].Metros2 >= 100 and departamentos[numero_reserva-1].Metros2 <= 200:
        return 8
    if departamentos[numero_reserva-1].Metros2 > 200:
        return 5

def ponderar_disponibilidad(departamentos):
    contador_libres = 0
    for x in range(len(departamentos)):
        if departamentos[x].Estado == "Libre":
            contador_libres += 1
    if contador_libres > 5:
        return 0
    if contador_libres >= 2 and contador_libres <= 5:
        return 2
    if contador_libres == 1:
        return 5
    

def verificar_precio(precio_venta,departamentos,numero_reserva):
    ponderacion_tamaño = ponderar_tamaño(departamentos,numero_reserva)
    ponderacion_disponibilidad = ponderar_disponibilidad(departamentos)
    valor_minimo = 1500 + 100 * ponderacion_tamaño + 200 * ponderacion_disponibilidad
    if precio_venta < valor_minimo:
        return False
    if precio_venta > valor_minimo:
        return True




def verificar_disponibilidad(numero_reserva,departamentos):
    for x in range(len(departamentos)):
        if departamentos[numero_reserva-1].Estado in departamentos[x].Estado == "Reservado" or departamentos[numero_reserva-1].Estado in departamentos[x].Estado == "Vendido":
            print("El departamento no está disponible")
        elif departamentos[numero_reserva-1].Estado == "Libre":
            return 1


def hacer_reserva(numero_reserva,precio_venta,departamentos):

    
    disponible = verificar_disponibilidad(numero_reserva,departamentos)
    if disponible == 1:
        precio = verificar_precio(precio_venta,departamentos,numero_reserva)
        if precio == True:
            departamentos[numero_reserva-1].Estado == 2 and departamentos[numero_reserva-1].PrecioVenta == precio_venta
            print("Usted a reservado el siguiente departamento con éxito")
            print(departamentos[numero_reserva-1])
        if precio == False:
            print("El precio ingresado está por debajo del valor minimo")
    if disponible != 1:
        print("El departamento ingresado no se escuenta disponible")


def calcular_departamentos_libres(departamentos):
    lista_libres = []
    for x in range(len(departamentos)):
        if departamentos[x].Estado == "Libre":
            lista_libres.append(departamentos[x])
    return f"Los departamentos libres son: {lista_libres}"

def contar_departamentos_por_estado(departamentos):
    cant_libres = 0
    cant_reservados = 0
    cant_vendidos = 0
    for x in range(len(departamentos)):
        if departamentos[x].Estado == "Libre":
            cant_libres += 1
        if departamentos[x].Estado == "Reservado":
            cant_reservados += 1
        if departamentos[x].Estado == "Vendido":
            cant_vendidos  += 1
    return f"Cantidad de departamentos Libres: {cant_libres}\nCantidad de departamentos Reservados: {cant_reservados}\nCantidad de departamentos Vendidos: {cant_vendidos}"        
            

def menu():
    departamentos = []
   
    while True:

        
        print("0-Salir")
        print("1-Cargar departamentos")
        print("2-Mostrar departamentos libres")
        print("3-Mostrar cantidad de departamentos por estado")
        print("4-Reservar departamento")

        try:
            seleccion = int(input("Seleccione la opcion que desea: "))

            if seleccion == 0:
                print("Adiós")
                break
            if seleccion == 1:
                cargadepto = cargar_departamento(departamentos)
                departamentos.append(cargadepto)
                print(departamentos)
            if seleccion == 2:
            
                print(calcular_departamentos_libres(departamentos))
                
            if seleccion == 3:
                print(contar_departamentos_por_estado(departamentos))
                
            if seleccion == 4: 
                numero_reserva = int(input("Ingrese el departamento que desea reservar: "))
                precio_venta = float(input("Ingrese el precio de venta pactado pactado: "))

                hacer_reserva(numero_reserva,precio_venta,departamentos)
            if seleccion < 0 or seleccion > 4:
                print("Por favor ingrese una opcion valida")
        except ValueError:
            print("Por favor ingrese un numero")
def main():
    menu()

if __name__ == '__main__':
    main()