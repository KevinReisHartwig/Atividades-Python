'''6. Faça um programa de consulta pela posição numérica da pessoa: leia nomes de pessoas, sendo a
quantidade determinada pelo usuário. Logo após a entrada pergunte ao usuário o número do nome
que ele gostaria de consultar. Após sua resposta, exiba o nome que fica na posição informada. '''

quantidades = []
nomes = []


quantidade = int(input("digite a quantidade de pessoas: "))


for i in range(quantidade):

    nome = input("digite o {}° nome: ".format(i+1))
    quantidades.append(i+1)


    nomes.append(nome)

consulta = int(input("qual o numero que voce quer consultar: "))



for i in range(quantidade):
    if consulta == quantidades[i]:
        print("a pessoa chamou {} e o nome é {}".format(quantidades[i], nomes[i]))

print(quantidades)







print(nomes)

