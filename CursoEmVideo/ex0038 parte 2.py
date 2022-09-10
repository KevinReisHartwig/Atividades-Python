'''Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:'''
numero1 = int(input("digite um numero: "))
numero2 = int(input("digite outro numero: "))

if numero1 > numero2:
    print("o primeiro numero é maior {}".format(numero1))
elif numero2 > numero1:
    print("o segundo numero é o maior {}".format(numero2))
else:
    print(" são iguais ")