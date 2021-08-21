import random

def opcion1():
    list=[]
    sumatoria = 0
    for x in range(random.randint(10, 99)):
        num = random.randint(1000, 9999)
        list.append(num)
        sumatoria+= num
    print(list)
    print(f'La sumatoria de todos los nros es: {sumatoria}')
    ...

def opcion2():
    buscar = int(input('Ingese el valor a eliminar: '))
    for i in range(len(list)):
        if buscar == list[i]:
            list.remove[i]
    print(f'Lista con el elemento borrado: {list}')

def main():
    opcion1() 
    opcion2()
    ...

if __name__ == "__main__":
    main()
