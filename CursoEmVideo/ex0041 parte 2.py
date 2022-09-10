'''Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia o ano de
nascimento de um atleta e mostre
sua categoria, de acordo com a idade:

– Até 9 anos: MIRIM

– Até 14 anos: INFANTIL

– Até 19 anos: JÚNIOR

– Até 25 anos: SÊNIOR

– Acima de 25 anos: MASTER'''

from datetime import date
ano = int(input("qual seu ano de nascimento: "))
atual = date.today().year
idade = atual - ano
print("o atleta tem {} de idade".format(idade))

if idade <= 9:
    print("atleta mirim")
elif idade <=14:
    print("atleta infantil")
elif idade <= 19:
    print("junior")
elif idade <= 25:
    print("senior")
elif idade >= 26:
    print("master")