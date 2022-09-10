'''Exercício Python 076: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
No final, mostre uma listagem de preços, organizando os dados em forma tabular.'''




listagem = ("lapis", 2.00, "caderno",3.00, "mochila", 20.00)
print("-"*40)
print(f'{"listagem":^40}')
print("-"*40)
for i in range(0,len(listagem)):
    if i % 2 == 0:
        print(f"{listagem[i]:.<30}",end='')
    else:
        print(f"{listagem[i]:>7.2f}")
print("-" * 40)