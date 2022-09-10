'''Exercício Python 090: Faça um programa que leia nome e média de um aluno,
guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.'''
aluno = dict()
aluno["nome"] = str(input("nome: "))
aluno["media"]=float(input("media: "))
if aluno["media"] >=7:
    aluno["situação"] = "aprovado"
elif 5 <= aluno["media"] < 7:
    aluno["situação"] = "Recuperação"
else:
    aluno["situação"] = "reprovado"
print("=-"*20)
for k, v in aluno.items():
    print(f"-{k} é igual a {v}")
print("=-"*20)