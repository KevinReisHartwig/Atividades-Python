'''13. Faça um software configurável para calcular a distribuição de freqüência de valores sorteados. Por
exemplo, suponha a faixa de 20 a 25 para os números sorteados e uma quantidade de 10, então se os
números sorteados forem 20, 24, 25, 23, 24, 25, 23, 23, 21,25 o resultado do programa deverá ser:
Distribuição de 10 números sorteados de 20 a 25:
Número 20: 1 vez (10%)
Número 21: 1 vez (10%)
Numero 22: zero vezes (0%)
Número 23: 2 vezes (20%)
Número 24: 2 vezes (20%)
Número 25: 4 vezes (40%)
Em seguida exiba a distribuição de freqüência ordenada:
Distribuição de 10 números sorteados de 20 a 25 (em ordem decrescente):
Número 25: 4 vezes (40%)
Número 23: 2 vezes (20%)
Número 24: 2 vezes (20%)
Número 20: 1 vez (10%)
Número 21: 1 vez (10%)
Numero 22: zero vezes (0%)'''
#Faça um software configurável para calcular a distribuição de freqüência de valores sorteados. Suponha uma faixa para os números sorteados, por exemplo, de 20 a 25,  e uma quantidade, por exemplo, 10 números, então os números sorteados poderão ser: 20, 24, 25, 23, 24, 25, 23, 23, 21,25.
import random
import numpy as np


#define a faixa
valor_inf=int(input("Informe o valor numérico inferior da faixa: "))
valor_sup=int(input("Informe o valor numérico superior da faixa: "))

#define a quantidade de números a serem sorteados dentro da faixa
qtde=int(input("Informe a quantidade de números que serão sorteados: "))

#cria uma lista vazia de números
numeros=[]
frequencia=[]
#faz a leitura dos dados dos alunos: nome e nota
for i in range(0,qtde):
  numeros.append(random.randint(valor_inf,valor_sup))
  frequencia.append(0)

print(numeros)

#Ordena em ordem crescente pela valor dos números sorteados (Bubble Sort)
for i in range(0,qtde):
  for j in range(i + 1, qtde):
      if (numeros[i] > numeros[j]):
        aux = numeros[i];
        numeros[i] = numeros[j];
        numeros[j] = aux;

#mostra o resultado na tela

def frequency(my_list):
    for item in my_list:
      if (item in frequencia):
        frequencia[item] += 1
      else:
        frequencia[item] = 1
    return frequencia
print(numeros)
print(frequencia)