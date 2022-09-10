from time import sleep
'''Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:

[ 1 ] somar

[ 2 ] multiplicar

[ 3 ] maior

[ 4 ] novos números

[ 5 ] sair do programa

Seu programa deverá realizar a operação solicitada em cada caso.'''
opção = 0

n1 = int(input("qual o primeiro numero: "))
n2 = int(input("qual o segundo numero: "))
while opção != 5:
    print("=-=" * 15)
    print('''   [ 1 ] somar
    
    [ 2 ] multiplicar
    
    [ 3 ] maior
    
    [ 4 ] novos números
    
    [ 5 ] sair do programa''')
    print("=-="*15)

    opção = int(input(">>>>>qual opção "))
    if opção ==1:
        soma = n1 + n2
        print("a soma de {} + {} é {}".format(n1,n2,soma))

    elif opção ==2:
        mult = n1 * n2
        print("a multiplicação de {} * {} é {}".format(n1,n2,mult))

    elif opção ==3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print("o maior numero é {}".format(maior))

    elif opção ==4:
        print("escreva os novos numeros")
        n1 = int(input("digite o primeiro numero novo: "))
        n2 = int(input("digite o segundo numero novo: "))

    elif opção ==5:
        print("finalizando...")
        sleep(2)
    else:
        print("numero invalido!")
print("programa finalizado!")