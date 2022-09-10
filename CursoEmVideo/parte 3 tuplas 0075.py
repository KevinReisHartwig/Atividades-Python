'''Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.

B) Em que posição foi digitado o primeiro valor 3.

C) Quais foram os números pares.'''

num = (int(input("digite um numero: ")),
        int(input("digite outro numero: ")),
        int(input("digite mais um numero: ")),
        int(input("digite o ultimo numero: ")))
print(f"vocçe digitou os valores {num}")
print(f"o nove apareceu {num.count(9)} vezes")
if 3 in num:
    print(f"o numero 3 apareceu na posição {num.index(3)+1}°")
else:
    print("não tem o numero 3")
print("os numeros pares foram digitados: ",end='')
for n in num:

    if n % 2 == 0:
        print(f"{n}", end=' ')
