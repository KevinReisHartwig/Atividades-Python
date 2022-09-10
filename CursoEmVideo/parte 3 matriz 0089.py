'''Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista
composta. No final, mostre um boletim contendo a
média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.'''
lista = []
while True:
    nome = str(input("nome: "))
    nota1 = float(input("nota1: "))
    nota2= float(input("nota2: "))
    media = (nota1 + nota2)/2
    lista.append([nome,[nota1,nota2],media])

    resp = str(input("quer continuar? S/N"))
    if resp in "Nn":
        break
print("=-"*20)
print(f'{"N°.":<4}{"NOME":<10}{"MEDIA":>8}')
print("=-"*20)
for i, a in enumerate(lista):
    print(f"{i:<4}{a[0]:<10}{a[2]:>8.1f}")
while True:
    opc = int(input("digite 999 para parar escolhe o aluno: "))
    if opc == 999:
        break
    if opc <= len(lista) -1:
        print(f"as notas do aluno {lista[opc][0]} é {lista[opc][1]}")

