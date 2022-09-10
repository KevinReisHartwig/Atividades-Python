"""3. Faça um algoritmo que leia dois números inteiros e mostre um menu com quatro operações (+, -, *, /) para o
usuário escolher. Imprima o resultado da opção escolhida. Caso o usuário digite uma opção inválida, mostrar
mensagem de erro. (utilize a estrutura ESCOLHA)"""

n1 = int(input("digite um numero inteiro: "))
n2 = int(input("digite outro numero inteiro: "))
print("( +, -, *, / )")
escolha = input("escolha um operador entre os 4 acima: ")

if escolha == "+":
    print(n1+n2)
elif escolha == "-":
    print(n1-n2)
elif escolha == "*":
    print(n1*n2)
elif escolha == "/":
    print(n1/n2)
else:
    print("operação invalida!")
