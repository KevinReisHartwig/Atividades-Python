'''Exercício Python 31: Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem,
cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.'''
km = float(input("qual é  a distancia da sua viagem: "))
print("você esta preste para fazer uma viagem de {}km".format(km))
if km <= 200:
    preço = km * 0.50
else:
    preço = km * 0.45
print("voce vai pagar {}".format(preço))
