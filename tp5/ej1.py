class FueraDeRango(Exception): #Genero mi propia excepción.
   ... 

class ValorMenorMin(Exception):
   ... 

class ValorMayorMax(Exception):
    ...

def ingresar_numero(mensaje, min, max):
    numero=0
    while True:
        try:
            texto=input(mensaje)
            numero = convertir_texto_numero(texto, min, max)
            return numero
        except ValueError:
            print('Debe ingresar un número.')
        #except FueraDeRango:
            #print('Ingrese un nro de 1 a 100')
        except ValorMayorMax:
            print('El valor ingresado es mayor a ', max)
        except ValorMenorMin:
            print('El valor ingresado es menor a ', min)

def convertir_texto_numero(texto, min, max):
    numero = int(texto)

    if numero < min:
        raise ValorMenorMin

    if numero > max:
        raise ValorMayorMax
    return numero


def main():

   # edad = ingresar_numero('Ingrese su edad: ', 0, 150)
   # print(edad)

    nota = ingresar_numero('Ingrese la nota: ', 1, 10)
    print(nota)
    ...


if __name__ == '__main__':
    main()
    ...


