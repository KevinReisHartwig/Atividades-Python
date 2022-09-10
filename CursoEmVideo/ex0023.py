'''Exercício Python 23: Faça um programa que leia um número de 0 a 9999 e
mostre na tela cada um dos dígitos separados.'''
num = int(input("digite um numero inteiro: "))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(num)
print("unicade",u)
print("dezena", d)
print("centena", c)
print("milhar",m)
