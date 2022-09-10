'''Exercício Python 12: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.'''

preço = float(input("digite o preço do produto para aplicar o desconto: "))
novo = preço-(preço * 10 / 100)
desconto = preço * 0.10
print("o preço {:.2f} com {:.2f}(5%)  de desconto é R${:.2f}".format(preço,desconto, novo))

