'''Exercício Python 43: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu
Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:

– IMC abaixo de 18,5: Abaixo do Peso

– Entre 18,5 e 25: Peso Ideal

– 25 até 30: Sobrepeso

– 30 até 40: Obesidade

– Acima de 40: Obesidade Mórbida'''

peso = float(input("digite seu peso: "))
altura = float(input("digite sua altura: "))
imc = peso / (altura**2)
print("o IMC dessa pessoa é {:.2f}".format(imc))
if imc < 18.5:
    print("peso abaixo do peso normal")
elif 18.5 <= imc < 25:
    print("peso ideal")
elif 25 <= imc < 30:
    print("sobrepeso")
elif imc >= 40:
    print("gordo demais para de comer")