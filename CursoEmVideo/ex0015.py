'''Exercício Python 15: Escreva um programa que pergunte a quantidade de Km
percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o
preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.'''
dias = int(input("digite os dias que foi usado o carro: "))
km = float(input("digite os km rodados com o carro: "))
preço = (dias * 60) + (km * 0.15)
print("o preço do uso do carro foi de R${:.2f}".format(preço))