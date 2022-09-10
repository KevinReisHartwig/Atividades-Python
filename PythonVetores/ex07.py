'''7. Faça um programa de consulta de telefones a partir de um nome informado por uma chave de dados:
leia nomes de pessoas com seus respectivos telefones, sendo a quantidade determinada pelo usuário.
Em seguida pergunte ao usuário qual o nome que ele deseja consultar o telefone. Após sua resposta,
exiba o telefone da pessoa procurada.'''

quantidades = []
nomes = []
telefones = []

quantidade = int(input("digite a quantidade de pessoas: "))

for i in range(quantidade):
    nome = input("digite seu nome: ")
    nomes.append(nome)
    telefone = int(input("digite seu telefone: "))
    telefones.append(telefone)

consulta = input("qual nome você deseja consultar o numero: ")

for i in range(quantidade):
    if consulta == nomes[i]:

        print("o numero pedido é {}".format(telefones[i]))
