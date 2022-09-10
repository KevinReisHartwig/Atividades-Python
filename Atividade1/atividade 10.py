'''10. Leia três números e imprima o maior deles. Não é necessário verificar se os números são iguais.'''

n1 = float(input('Informe o primeiro numero: '))
n2 = float(input('Informe o primeiro numero: '))
n3 = float(input('Informe o primeiro numero: '))

if n1>n2 and n1>n3:
  maior = n1
elif n2 > n3:
  maior = n2
else:
  maior = n3

print("O maior número é:",maior)