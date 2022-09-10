'''Exercício Python 10: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar '''
real = float(input("quantos de dinheiro voce tem na certeira? R$: "))
dolar = real / 4.43
print('com R$ {:.2f} você tem US$ {:.2f}'.format(real, dolar))
