'''Exercício Python 086: Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores
lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.'''
matrix = [[0,0,0],[0,0,0],[0,0,0]]
par = maior = terc = 0
for l in range(0,3):
    for c in range(0,3):
        matrix[l][c]=int(input(f"digite um valor para {[l],[c]}"))
print("=-"*20)
for l in range(0,3):
    for c in range(0,3):
        print(f"[{matrix[l][c]:^5}]",end="")
        if matrix[l][c] % 2 ==0:
            par += matrix[l][c]
    print()

print(f"a soma dos numeros pares e {par}")
for l in range(0,3):
    terc = terc + matrix[l][2]
print(f"a soma da terceira coluna é {terc}")
for c in range(0,3):
    if c == 0:
        maior = matrix[1][c]
    elif matrix[1][c] > maior:
        maior = matrix[1][c]
print(f"o maior da segunda coluna é {maior}")