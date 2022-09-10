'''Exercício Python 66: Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o
usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos
números foram digitados e qual foi a soma entre elas (desconsiderando o flag).'''
quant = soma = 0
while True:
    n=int(input("digite um numero para parar digite 999: "))
    if n == 999:
        break
    soma = soma + n
    quant = quant + 1
print(f"a soma é {soma} e a quantidade é {quant}")

