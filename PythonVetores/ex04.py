'''4. Leia um conjunto de valores inteiros e em seguida exiba-os na ordem inversa do que foram digitados. '''

numeros = []

for i in range(10):
    valores = int(input("digite um numero: "))

    numeros.append(valores)
numeros.reverse()
print(numeros)