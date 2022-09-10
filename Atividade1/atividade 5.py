"""5. Um banco concederá um crédito especial aos seus clientes, que varia com o saldo médio no último ano. Faça
um algoritmo que leia o saldo médio de um cliente e calcule o valor do crédito (percentual sobre o saldo médio)
de acordo com a tabela a seguir. Mostre uma mensagem informando o saldo médio e o valor do crédito.
Saldo médio Percentual
Até que 200 /              nenhum crédito
Maior que 200 até 400 /    10% do valor do saldo médio
Acima de 400 /             20% do valor do saldo médio"""

salario_medio = float(input("digite seu salario médio: "))

if salario_medio <= 200:
    print("nenhum credito acrescentado!")
elif salario_medio <= 400:
    print("credito de 10%, seu novo credido é {:.2f}".format(salario_medio+(salario_medio*0.10)))
else:
    print("credito de 20%, seu novo credito é {:.2f}".format(salario_medio+(salario_medio*0.20)))

