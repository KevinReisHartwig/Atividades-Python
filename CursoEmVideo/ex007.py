'''Exercício Python 7: Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.'''
n1 = float(input("digite a primeira nota:"))
n2 = float(input("digite a segunda nota: "))
media = (n1 + n2) / 2
print("a media de {:.1f} e {:.1f} é {:.1f}".format(n1,n2,media))