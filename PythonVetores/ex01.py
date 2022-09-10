'''1. Leia um conjunto de notas, cuja quantidade seja determinada pelo usuário. Calcule a média de todas
elas. Exiba o conjunto das notas maiores do que a média calculada. Após a exibição anterior, exiba o
outro conjunto de notas que são menores do que a média. Exiba, também, a quantidade de notas que
são exatamente iguais a média'''
'''2. Leia um conjunto de alunos, cada uma com o nome e a nota. Em seguida exiba o nome dos alunos
que possuem a nota maior do que a média da turma.'''

quantidade = int(input("quantidade de notas: "))

notas = []
soma = 0
iguais = 0
nomes = []

for i in range(quantidade):
    notas.append(float(input("digite a nota: "))

for i in range(quantidade):
    soma = soma + notas[i]

medias = soma/quantidade

for i in range(quantidade):
    if notas[i] > medias:
        print("a nota acima da media é {}".format(notas[i]))
    elif notas[i] == medias:
        iguais = iguais + 1
for i in range(quantidade):
    if notas[i] < medias:
        print("a nota menor que a media é {}".format(notas[i]))
print("quantidade de notas iguais a media: {}".format(iguais))