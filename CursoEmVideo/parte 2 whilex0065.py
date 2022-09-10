'''Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média
entre todos os valores e qual foi o maior e o menor valores lidos.
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.'''
soma = quant = media = soma = menor = 0
resp = "S"

while resp in "Ss":
    n = int(input("digite um numero: "))
    soma = soma + n
    quant = quant + 1

    if quant == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    resp = str(input("digite S/N S continua e N sai: "))
media = soma/quant

print("a media é {} e a quantidade de numeros é {} ".format(media,quant),end="")
print("o maior é {} e o menor é {}".format(maior,menor))




