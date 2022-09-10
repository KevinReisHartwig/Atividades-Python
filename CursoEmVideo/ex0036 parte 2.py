'''Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor
da casa, o
salário do comprador e em
quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.'''
casa = float(input("digite o valor da casa : "))
salario = float(input("digite o seu salario: "))
anos = int(input("quantos anos de financiamento?  "))
prestações = casa / (anos * 12)
minimo = salario * 0.30
print("para pagar a casa de R$ {} em {} anos".format(casa,anos))
print("a prestação vai ser de R${:.2f}".format(prestações))
if prestações <= minimo:
    print("aprovado")
else:
    print("negado")
