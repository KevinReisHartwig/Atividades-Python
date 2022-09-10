'''Exercício Python 26: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”,
em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.'''
nome = str(input("digite algo: ")).upper().strip()
print("quantas vezes aparece o A: {}".format(nome.count('A')))
print("aonde apare a primeira letra A: {}".format(nome.find('A')+1))
print("aonde apareceu a ultima letra A: {}".format(nome.rfind('A')+1))
