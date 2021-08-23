#Excepciones en Python

#Son la forma que tiene Python de comunicarnos por un lado a nosotros y otro internamente al programa, de que hubo algún problema.


#Basicamente son validaciones, el programa una vez que encuentra un error lo muestra y corta el programa y hace lo que diga el except correspondiente.

"""
a = 100

try: #Envuelvo el codigo en una estructura (?)
    b = int(input('Ingrese un nro: ')) 
    print("Ingresó: ", b)
    print(a/b)

except ZeroDivisionError: #Error por si divide por 0
    print("No se puede dividir por cero")

except ValueError: #Por si ingresa un valor incorrecto (ej: letras)
    print("Debe ingresar un nro")

except Exception: #EN el caso de que haya un error hace lo siguiente:
    print("Error desconocido")

except: #Este sirve para todo pero no es una buena práctica usarlo.
    print("Captura todo")

print('chau')
"""

#Otra prueba del profe

class FueraDeRango(Exception): #Genero mi propia excepción.
    pass

def ingreso(min, max):
    numero = int(input('Ingrese un nro: '))
    if numero < min or numero > max:
        raise FueraDeRango() #Levanto el error
    return numero
 
def ingresar_numero():
    numero=0
    while True:
        try:
            numero=ingreso(1,100)
        except ValueError:
            print('Debe ingresar un número.')
        except FueraDeRango: #Si ocurre lo del if de mi propia excepcion
            print('Ingrese un nro de 1 a 100')

def main():
    print(ingresar_numero())

if __name__ == '__main__':
    main()

