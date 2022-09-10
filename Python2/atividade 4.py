'''4) Faça um algoritmo para somar os restos da divisão por 3 de 200 números inteiros (de
1 a 200).'''

# algoritimo que some os restos da divisão:
soma = 0
for num in range(200):
    resto = num % 3
    soma = soma + ((num + 1) % 3)

    print("0 resto é {} e a soma do resto é {}".format(resto, soma))







