'''Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.'''

palavras = ("cachorro", "leão", "gabriela", "kevin", "nicole", "rodolfo", "bruno")
for i in palavras:
    print(f"\nas palavras são {i.upper()} e as vogais é: ",end="")
    for letra in i:
        if letra.lower() in "aeiou":
            print(f"{letra}",end=" ")