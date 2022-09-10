'''Exercício Python 72: Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.'''

cont = ('zero', 'um', 'dois', 'treis', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove' , 'dez', 'onze',
        'doze', 'treze', 'cartoze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    num = int(input("digite um numero de 0 a 20: "))
    if 0 <= num <=20:
        break

    print("tende novamente numero invalido")

print(f"voçe digitou o numero {cont[num]}")




