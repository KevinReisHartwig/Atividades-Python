'''Exercício Python 101: Crie um programa que tenha uma função chamada voto()
que vai receber como parâmetro o ano de nascimento de uma pessoa,
retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.'''

def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'com {idade} não vota'
    elif 16 <= idade <= 18 or idade > 65:
        return f'com {idade} é opcional'
    else:
        return f'com {idade} é obrigatorio!'

nasc = int(input("qual ano de nascimento: "))
print(voto(nasc))
