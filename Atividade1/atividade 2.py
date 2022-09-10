"""2. Faça um algoritmo que leia um número inteiro e verifique se ele é par ou ímpar. Imprima uma mensagem
correspondente ao resultado. Se o número for zero, imprima: “o valor é zero”."""

numero_inteiro = int(input("digite um numero inteiro: "))

if numero_inteiro % 2 == 0:
    print("o numero é par")
else:
    print("é impar")
