'''6. Criar um algoritmo que leia o código da carga e o peso (em toneladas) da carga de um caminhão. Caso o
código não esteja entre os intervalos descritos na tabela, imprimir mensagem: “código inválido”. Calcule e
imprima: o peso da carga do caminhão convertido em quilos (1 ton – 1000kg) e o preço da carga do caminhão,
de acordo com a tabela abaixo.
Código da Carga Preço por Quilo (em R$)
10 a 20 100
21 a 30 250
31 a 40 330'''

codigo_carga = int(input("digite o codigo da carga: "))
peso_carga = float(input("digite o peso da carga em toneladas: "))


if codigo_carga >= 10 and codigo_carga <= 20:
    print("o peso em quilos é de {} KG e o preço da carga é de R${}".format(peso_carga*1000, (peso_carga*1000)*100))
elif codigo_carga >= 21 and codigo_carga <= 30:
    print("o peso em quilos é de {} KG e o preço da carga é de R${}".format(peso_carga * 1000, (peso_carga * 1000) * 250))
elif codigo_carga >= 31 and codigo_carga <= 40:
    print("o peso em quilos é de {} KG e o preço da carga é de R${}".format(peso_carga*1000, (peso_carga*1000) * 330))
else:
    print("codigo invalido!")
