'''Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos
e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado.
No final, serão exibidos todos os valores únicos digitados, em ordem crescente.'''
lista = []
while True:
    n =int(input("digite o numero: "))
    if n not in lista:
        lista.append(n)
    else:

        print("esse numero já tem tente outro")
    parar = str(input("digite S/N para parar ou não: ")).strip().upper()[0]
    if parar in "Nn":
        break
lista.sort()
print(lista)

