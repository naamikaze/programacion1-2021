#Ejercicio Ambulancias
INDICE_NUMERO_AMBULANCIA=0

#Total de km recorridos y servicios prestados durante todo el mes.
def cargar_totales_ambulancias(ambulancias, ambulancias_numeros, ambulancias_servicios, ambulancias_kilometros):

    for ambulancia in ambulancias:
        if ambulancia[INDICE_NUMERO_AMBULANCIA] not in ambulancias_numeros:
            ambulancias_numeros.append(ambulancia[INDICE_NUMERO_AMBULANCIA])
    print(ambulancias_numeros)

    ...

def principal():

    ambulancias=[[1000,2,5,9],[200,2,4,8],[303,4,6,5],[1000,4,4,9],[1000,6,5,8],[200,3,5,10],[3,5,5,7],[2,4,4,11],[3,6,4,10]] 

    ambulancias_numeros=[]
    ambulancias_servicios=[]
    ambulancias_kilometros=[]
    ambulancias_numeros=[]
    cargar_totales_ambulancias(ambulancias, ambulancias_numeros, ambulancias_servicios, ambulancias_kilometros)
    print('Ambulancias')
    ...

if __name__ == '__main__':
    principal()
    ...