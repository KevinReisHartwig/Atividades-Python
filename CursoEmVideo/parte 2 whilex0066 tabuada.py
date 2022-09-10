'''Exercício Python 67: Faça um programa que mostre a tabuada de vários números, um de cada vez,
para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.'''

while True:
    n=int(input("digite um numero para fazer a tabuado e digite um numer negativo para parar: "))
    if n < 0:
        break
    for i in range(1,11):
        print(f"{n} * {i} = {n*i}")
print("tabuada encerrada")
