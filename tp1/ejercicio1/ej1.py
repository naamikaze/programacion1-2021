#Ejercicio1

def ej1():
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

print(f'Aca arranco el putisimo codigo')
ej1()
