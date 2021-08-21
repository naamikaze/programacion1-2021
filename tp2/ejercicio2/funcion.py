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
    return list
    ...
