#TP 10
def diadelasemana(dia, mes, año):
    if mes < 3:
        mes += 10
        año -= -1 
    else: 
        mes = mes - 2
        siglo = año // 100
        año2 =  año % 100
        diasem = (((26*mes-2)//10)+dia+año2+(año2//4)+(siglo//4)-(2*siglo))%7
        if diasem < 0:
            diasem = diasem + 7
        return diasem

def cant_dias_mes(mes):
    meses=[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return meses[mes-1]

def imprimir_calendario(mes, año):
    print(' D  L  M  X  J  V  S ')
    dias_mes = cant_dias_mes(mes)
    ##print(dias_mes)
    primer_semana = True

    for dia in range(1, dias_mes + 1):
        dia_semana = diadelasemana(dia,mes,año)

        if primer_semana:
            print('   ' * dia_semana, end='')
            primer_semana = False

        if dia < 10:
            print(' ', end='')
        print(dia, end=' ')

        if dia_semana == 6:
            print()

def main():
    dia = 7
    mes = 8
    año = 2021
    #dia = int(input('Ingrese un dia: '))
    #mes = int(input('Ingrese un mes: '))
    #año = int(input('Ingrese un año: '))
    dia_semana = diadelasemana(dia,mes,año)
    print(dia_semana)
    imprimir_calendario(mes, año)
    ...

if __name__ == '__main__':
    main()



         