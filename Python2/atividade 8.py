'''8) Dados dois números inteiros A e B, construa um algoritmo para calcular a soma de
todos os inteiros existentes entre A e B.'''


soma1 = 0
soma2 = 0




numero = int(input("digite o primeiro numero: "))
numero2 = int(input('digite o segundo numero: '))
for n in range(0, numero+1):
    soma1 = soma1 + n

for n in range(0, numero2+1):
    soma2 = soma2 + n

soma3 = soma1 + soma2




print("a soma do primeiro numero é {}".format(soma1))
print("a soma do segundo numero é {}".format(soma2))
print("a soma do primeiro e segundo numero é {}".format(soma3))