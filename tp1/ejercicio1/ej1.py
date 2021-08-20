#Ejercicio1

def mayor():
    switch = 0
    mayor = -10
    while switch != 3:
        switch +=1
        num = int(input('Ingrese un nro: '))
        if num > mayor:
            mayor = num
        elif num == mayor:
            mayor = -1 
            break
    print(f'El nro mayor es: {mayor}')
    ...


def main():
    print('TRABAJO PRACTICO NRO 1')
    print('Ejercicio 1 - Ignacio Rodríguez')
    mayor()
    ...

if __name__ == '__main__':
    main()
