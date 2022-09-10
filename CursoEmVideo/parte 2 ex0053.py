'''Exercício Python 53: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:
APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.'''

nome = str(input("digite um nome: ")).strip().upper()   # tirar os espaços e colocar tudo em maisculo
palavras = nome.split() #transforma em lista
junto = ''.join(palavras) #juntar as palavras da lista
inverso = ''
#inverso= junto[::-1] outro metodo mais facil sem o for
for letra in range(len(junto)-1, -1, -1):
    inverso = inverso + junto[letra]
if inverso == junto:
    print("palindromo")
else:
    print("não é um palindromo")
print(junto, inverso)
