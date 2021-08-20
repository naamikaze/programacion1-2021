from funcion1 import func1
from funcion2 import func2

def menu():
    while True:
        opcion = int(input('Ingrese una opción: '))
        if opcion != 1 and opcion != 2:
            print('Ingrese una opción valida')
        elif opcion == 1:
            func1()
            break
        elif opcion == 2:
            func2()
            break
       
def main():
    print('Ejercicio 6 - Ignacio Rodríguez')
    menu()

if __name__ == '__main__':
    main()
