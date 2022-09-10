'''Exercício Python 37: Escreva um programa em Python que leia um número inteiro qualquer e peça para o
usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.'''
numero = int(input("digite um numero inteiro qualquer: "))
print('''escolha  uma das bases para converção: 
[1] converter para binário
[2] converter para octal
[3] converter para hexadecimal''')
opção = int(input("digite a opção: "))
if opção == 1:
    print("o numero {} em binário é {}".format(numero, bin(numero)[2:]))
elif opção == 2:
    print("o numero {} em octal é {}".format(numero, oct(numero)[2:]))
elif opção == 3:
    print("o numero {} em hexadecimal é {}".format(numero, hex(numero)[2:]))
else:
    print("opção invalida")