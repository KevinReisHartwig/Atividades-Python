'''9. Leia dois conjuntos de números com a mesma quantidade. Exiba a intersecção dos conjuntos, ou
seja, os números que são repetidos nos dois conjuntos.'''
nu1 = []
nu2 = []
igual = []
for i in range(5):
    n1 = int(input("digite um numero: "))
    n2 = int(input("digite um numero: "))
    nu1.append(n1)
    nu2.append(n2)
if n1 == n2:
    igual.append(n1)

print(f"os numeros da lista {nu1} e {nu2} que são iguais nas duas listas são {igual}")



