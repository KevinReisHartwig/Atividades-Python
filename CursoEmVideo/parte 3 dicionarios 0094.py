'''Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa
em um dicionário e todos os dicionários em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média'''
pessoa = dict()
galera = list()
soma = media = 0
while True:
    pessoa.clear()
    pessoa["nome"]=str(input("nome: "))
    while True:
        pessoa["sexo"]=str(input("digite o sexo M/F: ")).upper()[0]
        if pessoa["sexo"] in "MF":
            break
        print("erro digite novamente! S/N: ")
    pessoa["idade"] = int(input("digite sua idade: "))
    soma += pessoa["idade"]
    galera.append(pessoa.copy())

    while True:
        resp = str(input("S/N para continuar: ")).upper()[0]
        if resp in "SN":
            break
        print("erro")
    if resp == "N":
        break
media = soma/ len(galera)
print("=-"*30)
print(f"tem no total {len(galera)} pessoas")
print(f"a media é {media} anos")
print("as mulheres cadastradas foram ", end="")
for p in galera:
    if p["sexo"] in "fF":
        print(f'{P["nome"]}',end="")
print()

print("lista de pessoas acima da media: ")
for p in galera:
    if p["idade"] >= media:
        print("     ",end="")
        for k,v in p.items():
            print(f"{k}={v}; ",end="")
        print()
print("encerrado")