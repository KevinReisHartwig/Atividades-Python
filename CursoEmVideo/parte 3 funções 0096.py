'''Exercício Python 096: Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno
retangular (largura e comprimento) e mostre a área do terreno.'''
def area(comp,larg):
    a = comp * larg
    print(f"a área de um terreno é {comp} * {larg} é de {a}m²")

print("calculador de área")
print("=-"*20)
l = float(input("digite a largura: "))
c = float(input("digite o comprimento: "))
area(c,l)