'''3) Faça um programa que vai pedindo números ao usuário até que este introduza o
número -1. O computador deve dizer a média dos números introduzidos (excluindo o-
1)'''

# somar os numeros escolhidos para o usuario e fazer a média deles usando o -1 para parar, tirando o -1 da soma e media.
n = 1
soma = quantidade = media = 0
while n != -1:
    n = int(input('digite um número para parar digite -1: '))
    if n != -1:
        soma = soma + n
        quantidade = quantidade + 1
        media = (soma)/(quantidade)
print("você digitou {} números e a média foi {}".format(quantidade, media))