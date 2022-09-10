'''Exercício Python 13: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.'''
salario = float(input("digite o seu salario para aplicar o aumento: "))
novo = salario + (salario * 0.15)
print("o salario é R${:.2f} e o aumento foi de 15% que deu R${:.2f}".format(salario,novo))