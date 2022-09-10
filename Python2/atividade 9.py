'''9) Construir um algoritmo para gerar a seguinte série:
s = 1 + 1 + 1 + ... + 1 para os 50 primeiros termos.'''


divisão = 0


numero = int(input("digite um numero inteiro para calcurar a soma da divisão dele: "))

for n in range(1, numero+1):
    divisão = divisão + (1 / n)
print("a soma da divisão do numero {} é {}".format(numero, divisão))