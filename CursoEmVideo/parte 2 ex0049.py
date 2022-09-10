'''Exercício Python 49: Refaça o DESAFIO 9, mostrando a tabuada de um número
que o usuário escolher, só que agora utilizando um laço for.'''

numero = int(input("digite o numero para ver a tabuada: "))
print("\33[34m=-\33[m"*15)
for i in range(1,11):
    print("\33[31m{} x {:2} = {}\33[m".format(numero,i, numero*i))
print("\33[34m=-\33[m"*15)