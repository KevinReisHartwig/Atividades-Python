'''10. Leia um conjunto de números. Exiba-os em ordem numérica crescente.'''

numeros = []

for i in range(10):
    valores = int(input("digite um numero: "))

    numeros.append(valores)
numeros.sort()
print(numeros)