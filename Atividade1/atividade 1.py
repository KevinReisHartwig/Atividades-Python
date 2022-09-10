'''1. Construa um algoritmo que leia dois números inteiros e verifique se a divisão seja indeterminada
(denominador igual a zero). Em caso afirmativo, imprima a seguinte mensagem: “Divisão indeterminada”, do
contrário, imprima o resultado da divisão. Considere a divisão do primeiro pelo segundo.'''

n1 = int(input("digite um numero inteiro: "))
n2 = int(input("digite outro numero inteiro: "))

if n2 == 0:
    print("divisão inderterminada")
else:
    print(n1/n2)

