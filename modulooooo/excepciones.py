#aaaaaa

class MayorA5(Exception):
    pass

def main():
    try:
        num = int(input('Ingrese un numero'))
        num2 = int(input('Ingrese un  nro mayor a 5: '))

        if num2 < 5:
            raise MayorA5

        suma = num + num2
        print(suma)

    except ValueError:
        print('sexo')
    except MayorA5:
        print('El nro no es mayor a 5')

main()

    