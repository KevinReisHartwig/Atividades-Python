'''2. Leia um conjunto de alunos, cada uma com o nome e a nota. Em seguida exiba o nome dos alunos
que possuem a nota maior do que a média da turma.'''

quantidade = int(input("quantidade de notas: "))

notas = []
soma = 0
iguais = 0
nomes = []

for i in range(quantidade):
    nomes.append(input("digite o nome do aluno: "))

for i in range(quantidade):
    notas.append(float(input("digite a nota de {}: ".format(nomes[i]))))

for i in range(quantidade):
    soma = soma + notas[i]

medias = soma/quantidade

for i in range(quantidade):
    if notas[i] > medias:
        print("a nota acima da media é {} e é de {}".format(notas[i],nomes[i]))
    elif notas[i] == medias:
        iguais = iguais + 1
for i in range(quantidade):
    if notas[i] < medias:
        print("a nota menor que a media é {} é de {}".format(notas[i],nomes[i]))
print("quantidade de notas iguais a media: {}".format(iguais))