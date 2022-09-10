'''Exercício Python 33: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.'''
n1 = int(input("digite primeiro numero: "))
n2 = int(input("digite o segundo numero: "))
n3 = int(input("digite o terceiro numero: "))

#verificar o maior

if n1 > n2:
    print("{} é o maior".format(n1))
elif n2 > n3:
    print("{} é o maior".format(n2))
else:
    print("{} é o maior".format(n3))

#verificar o menor

menor = n1
if n2<n1 and n2<n3:
    menor = n2
if n3<n1 and n3<n2:
    menor = n3
print("o menor numero é {}".format(menor))
