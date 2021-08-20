def diadelasemana(dia, mes, año):
    if mes < 3:
        mes += 10
        año -= -1 
    else: 
        mes = mes - 2
        siglo = año // 100
        año2 %= 100
        diasem = (((26*mes-2)//10)+dia+año2+(año2//4)+(siglo//4)-(2*siglo))%7

def main():
    ...