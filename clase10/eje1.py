def main_leer():
    lista=[]
    with open('archivo.py', 'r', encoding='utf-8') as archivo:
        for linea in archivo:
            lista.append(linea)
    return lista


def main_borrar(lista):
    for x in range(len(lista)):
        lista[x].replace("#", "")
    print(lista)
    return lista

def main_ingresar(lista):
    with open('archivo.py', 'w', encoding='utf-8') as archivo:
        for x in range(len(lista)):
            archivo.write(lista[x])
    print('Todo listo')


def main():
    print('Un ALGORITMO HECHO POR EL MEJOR')

    for x in range(3):
        print('IGNACIO RODRIGUEZ')

    print()
    print('COMENZEMOS B)')
    print()

    lista = main_leer()
    borrada = main_borrar(lista)
    main_ingresar(borrada)
    ...


if __name__ == '__main__':
    main()
    ...
        
