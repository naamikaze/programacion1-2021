def control():
    cant = int(input('Ingrese la cantidad de viajes realizados: '))
    #El valor de la tarifa de subte según internet es de 30$ así que le puse ese valor.
    total = cant*30
    if cant >= 1 and cant <= 20:
        total = total
    elif cant >= 21 and cant <= 30:
        porcentaje=total*0.20
        total -= porcentaje
    elif cant >= 30 and cant <= 40:
        porcentaje=total*0.30
        total -= porcentaje
    elif cant > 40:
        porcentaje = total*0.40
        total -= porcentaje
    print(f'Usted debe pagar: {total}$')
    ...

def main():
    print('Trabajo Practico nro1 - Ejercicio 4')
    control()
    ...

if __name__ == '__main__':
    main()

