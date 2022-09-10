'''Exercício Python 14: Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.'''
c = float(input("digite a temperatura em graus ceusius para converter em graus Fahrenheit: "))
f = 9 * c / 5 + 32
print("a temperatura  de {} °C corresponde {} °F".format(c,f))
