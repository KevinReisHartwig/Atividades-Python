'''Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.'''

lista = []
maior = 0
menor = 0

for i in range(0,5):
    lista.append(int(input(f"digite o °{i} numero: ")))
    if i == 0:
        maior = menor = lista[i]
    else:
        if lista[i] > maior:
            maior = lista[i]
        if lista[i] < menor:
            menor = lista[i]
print(f"os valores são {lista}")
print(f"os maiores valores são {maior} e fica na posição: ",end="")
for i,v in enumerate(lista):
    if v == maior:
        print(f"{i}...",end="")
print()

print(f"os menores valores são {menor}e fica na posição: ",end="")
for i,v in enumerate(lista):
    if v == menor:
        print(f"{i}...",end="")
print()
