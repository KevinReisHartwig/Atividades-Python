'''Faça um programa que receba o valor do salário de uma pessoa e o valor de um financiamento pretendido.
Caso o financiamento seja menor ou igual a 5 vezes o salário da pessoa, o programa deverá escrever
"Financiamento Concedido"; senão, escreverá "Financiamento Negado". Independente de conceder ou não o
financiamento, o programa escreverá depois a frase "Obrigado por nos consultar."'''

salario = float(input("digite seu salario: "))
salario_f = float(input("digite o numero de financiamento pretendido: "))

if salario_f <= 5:
    print("Financiamento Concedido")
else:
    print("Financiamento Negado")
print("obrigado por nos consultar!")