'''Exercício Python 56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.'''
somaidade = 0
mediaidade = 0
velho = ''
maioridade = 0
mulher20 = 0



for i in range(1,5):
    print("qual os dados da {}° pessoa".format(i))
    sexo = input("qual o sexo da pessoa: ").strip()
    idade = int(input("qual a idade da pessoa: "))
    nome = input("qual o nome da pessoa: ").strip()
    somaidade = somaidade + idade
    if i == 1 and sexo in 'Mm':
        maioridade = idade
        velho = nome
    if sexo in 'Mm' and idade > maioridade:
        maioridade = idade
        velho = nome
    if sexo in 'Fm' and idade > 20:
        mulher20 = mulher20 + 1


mediaidade = somaidade/4
print("o homem mais velho tem {} de idade e se chama {}.".format(maioridade,velho))
print("a media das idades é {}".format(mediaidade))
print("tem {} mulheres maiores de 20 anos".format(mulher20))
