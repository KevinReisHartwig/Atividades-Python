'''Exercício Python 52: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.'''
total = 0
n = int(input("digite um numero: "))

for i in range(1,n+1):
    if n % i == 0:
        print("\33[31m", end=" ")
        total = total + 1

    else:
        print("\33[34m", end=" ")

    print("{}".format(i),end=" ")
print("\n\033[mo numero {} foi divisivel {} vezes".format(n,total))
if total == 2:
    print("ele é primo")
else:
    print("não é primo")