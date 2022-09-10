'''13. A loja Constrói em Partes produz dois tipos de hastes: cobre e alumínio. Cada haste de cobre é vendida por
R$ 2,00, e cada haste de alumínio é vendida por R$ 4,00. O desconto dado dependerá da quantidade de hastes
compradas, conforme tabela abaixo. Fazer um algoritmo para ler a quantidade comprada de cada tipo de haste
e imprima o total pago.
Quantidade comprada
(duas hastes juntas)
Percentual
de Desconto
Abaixo de 5       0
Entre 5 e 15     10
Entre 16 e 20    15
Acima de 20      20'''

hates = int(input('digite a quantidade comprada: '))
compra = input("digite qual a hastes comprada cobre ou alumínio: ")


cobre1 = hates * 2
aluminio1 = hates * 4

if compra == 'cobre' and hates <= 5:
    print("ele recebeu 0 de desconto, ele comprou {} e pagou R${}".format(compra, cobre1 - 10))
elif compra == 'cobre' and hates <= 20:
    print("ele recebeu 15 de desconto, ele comprou {} e pagou R${}".format(compra, cobre1 - 15))
elif compra == 'cobre' and hates > 20:
    print("ele recebeu 20 de desconto, ele comprou {} e pagou R${}".format(compra, cobre1 - 20))
elif compra == 'alumínio' and hates <= 5:
    print("ele recebeu 0 de desconto, ele comprou {} e pagou R${}".format(compra, cobre1))
elif compra == 'alumínio' and hates <= 15:
    print("ele recebeu 10 de desconto, ele comprou {} e pagou R${}".format(compra, cobre1 - 10))
elif compra == 'alumínio' and hates <= 20:
    print("ele recebeu 15 de desconto, ele comprou {} e pagou R${}".format(compra, cobre1 - 15))
elif compra == 'alumínio' and hates > 20:
    print("ele recebeu 20 de desconto, ele comprou {} e pagou R${}".format(compra, cobre1 - 20))
else:
    print("você pode ter escrevido errado olhe se nã faltou um acento ou colocou a informação errada!")


