'''11. Leia um conjunto de nomes de pessoas. Exiba-os em ordem alfabética crescente.'''

nomes = []

for i in range(5):
    nome = (input("digite um nome: "))

    nomes.append(nome)
nomes.sort()
print(nomes)