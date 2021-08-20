#from ejex import NOMBRE_SISTEMA, IVA <- Para importar una/s variable/s en específico. Esta es una buena práctica, solo llamar lo que voy a utilizar.

#Los import no cuentan necesariamente como variables globales.

import ejex as c # <- Con esto importo todo el módulo. El 'c' es el alias. 
import funciones as f1
import funciones2 as f2

def mostrar_menu():
    print(c.NOMBRE_SISTEMA) #Llamo la variable con c. como especifiqué en la linea 3.
    print(c.IVA)
    op=int(input('Ingrese una opción: '))
    if op == 1:
        f1.opcion_1(4)
    elif op == 2:
        f2.opcion_2()

def main():
    print(f'Mostrar menu desde módulo menú')
    mostrar_menu()

if __name__ == '__main__':
    main()

