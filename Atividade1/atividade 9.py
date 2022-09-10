'''9. Faça um programa que leia o nome e idade de duas pessoas e imprima o nome da pessoa mais nova, e seu
ano de nascimento (o programa deve funcionar corretamente para qualquer que seja o ano atual).'''

from datetime import date

data_atual = date.today()
print(data_atual)

nome = input('Informe o nome da pessoa: ')
idade = int(input('Informe a idade da pessoa: '))

print("Ano de nascimento:",int(data_atual.year)-idade)

