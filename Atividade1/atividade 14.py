'''14. Uma empresa de energia elétrica trabalha com 3 tipos de consumidores: I – Industrial; C – Comercial; R –
Residencial. Fazer um algoritmo para ler o tipo de consumidor („I‟, „C‟ ou „R‟), a quantidade de energia
consumida, e calcular e imprimir qual será o valor pago. Para calcular o valor pago, verificar a tabela abaixo.
Tipo de Consumidor Cálculo
Industrial    0.68*Consumo + 34
Comercial     0.52*Consumo + 45
Residencial   0.47*Consumo + 22 '''

tipo_consumidor = input('Tipo de consumidor (I, C ou R): ')
if not tipo_consumidor == "I" or tipo_consumidor == "C" or tipo_consumidor == "R":
  print("Tipo de consumidor inválido!")
else:
  consumo = float(input('Qual a quantidade de energia consumida:'))
  if tipo_consumidor == "I":
    print('Valor pago: R$',round(0.68*consumo + 34,2))
  elif tipo_consumidor == "C":
    print('Valor pago: R$',round(0.52*consumo + 45,2))
  elif tipo_consumidor == "R":
     print('Valor pago: R$',round(0.47*consumo + 22,2))
