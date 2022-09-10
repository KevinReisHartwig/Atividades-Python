'''Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas
listas extras que vão conter apenas os valores pares e os valores ímpares
digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.'''
valores = []
par = []
impares = []
while True:
    valores.append(int(input("digite um numero: ")))


    teste = str(input("digite S/N para continuar ou nãp: "))
    if teste in "Nn":
        break
for i,v in enumerate(valores):
    if v %2==0:
        par.append(v)
    elif v %2==1:
        impares.append(v)
print(f"os valores impares é {impares}")
print(valores)
print(f"os numeros pares é {par}")