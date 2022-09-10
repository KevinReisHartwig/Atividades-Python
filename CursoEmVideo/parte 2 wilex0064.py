'''Exercício Python 64: Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário
digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a
soma entre eles (desconsiderando o flag).'''
cont = soma = num = 0

num = int(input("digite um numero ate voçe digitar 999 para parar: "))
while num != 999:
    soma = soma + num
    cont = cont + 1
    num = int(input("digite um numero ate voçe digitar 999 para parar: "))
print("foi digitado {} numeros é a soma deles é {}".format(cont,soma))
