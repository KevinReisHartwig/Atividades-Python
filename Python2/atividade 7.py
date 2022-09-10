'''7) Apresentar todos os valores numéricos inteiros ímpares situados na faixa de 0 a n, onde
n é um número fornecido pelo usuário do programa. A verificação se o número é ímpar
será feita dentro do loop. Caso o número seja ímpar, mostre-o, não sendo, passe para
o próximo número.'''

numero = 0
numero = int(input("digite um numero para falar entre eles quem é par: "))

for n in range (0, numero):
    if n % 2 != 0:
        print('\033[36m', end='')
    else:
        print('\033[m', end='')
    print('{} '.format(n), end='')
print("/ azul é impar e branco é par!")

