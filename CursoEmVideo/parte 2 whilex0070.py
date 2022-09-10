'''Exercício Python 70: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar
se o usuário vai continuar ou não. No final, mostre:

A) qual é o total gasto na compra.

B) quantos produtos custam mais de R$1000.

C) qual é o nome do produto mais barato.'''
total = totmil = menor = cont = 0
barato = ""
while True:
    produto = str(input("digite o nome do produto: "))
    preço = int(input("digite o preço do produto: "))
    cont = cont + 1
    total = total + preço
    if preço > 1000:
        totmil = totmil + 1
    if cont == 1:
        menor = preço
        barato = produto
    else:
        if preço < menor:
            menor = preço
            barato = produto

    resp = " "
    while resp not in "SN":
        resp = str(input("digite sim ou não para continuar: ")).strip().upper()[0]
    if resp == "N":
        break
print(f"o total de produtos foi {total} e a quantidade de produtos maiores de 1000 foi {totmil}")
print(f"o nome do produto mais barato é {barato}")
