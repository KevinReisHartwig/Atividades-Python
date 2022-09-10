'''Exercício Python 50: Desenvolva um programa que leia seis números inteiros e
mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.'''
soma = 0
cont = 0
for i in range(1,7):
    n = int(input(f"digite {i}° numero: "))
    if n % 2 == 0:
        cont = cont + 1
        soma = soma + n
print(soma,cont)