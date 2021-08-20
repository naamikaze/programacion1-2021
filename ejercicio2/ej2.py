#Ejercicio 2
def gregoriano():
    from numeros import num1, num2, num3
    if num1 >= 1 and num1 <= 31 and num2 >= 1 and num2 <= 12:
        print(f'La fecha ingresada corresponde a una fecha ({num1}/{num2}/{num3}')
    else:
        print(f'La fecha ingresada no corresponde a una fecha ({num1}/{num2}/{num3}')

from numeros import nums
nums()
gregoriano()