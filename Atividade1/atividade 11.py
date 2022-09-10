'''11. Leia um mês e ano e imprima a quantidade de dias que este mês possui. Lembre-se dos anos bissextos.'''

ano = int(input('Digite o ano: '))
mes = int(input('Digite o mês: '))

if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
  print("O mês",mes,"tem 31 dias",)

elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
  print("O mês",mes,"tem 30 dias")

elif mes == 2:
  if ano % 100 != 0 and ano % 4 == 0 or ano % 400 == 0:
    print("O mês",mes,"tem 29 dias")
  else:
    print("O mês",mes,"tem 28 dias")
else:
    print("O valor não corresponde a um mês válido!")