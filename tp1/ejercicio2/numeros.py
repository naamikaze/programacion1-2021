def nums():
    while True:
        num1 = int(input('Ingrese el primero nro: '))
        num2 = int(input('Ingrese el segundo nro: '))
        num3 = int(input('Ingrese el tercer nro: '))
        if num1 > 0 and num2 > 0 and num3 > 0:
            break
        else:
            print(f'Un nro es invalido, intente otra vez por favor.')

