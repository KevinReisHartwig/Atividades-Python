'''6) Inicializar as variáveis FATORIAL e CONTADOR com 1; Solicitar o valor de um número
para calcular o seu fatorial; Multiplicar sucessivamente a variável FATORIAL pela
variável CONTADOR; Incrementar 1 à variável CONTADOR, efetuando o controle até
o valor solicitado; Apresentar ao final o valor obtido.'''

fatorial = 1


numero = int(input("digite um numero inteiro para calcurar o fatorial: "))

for n in range(1, numero):
    fatorial = fatorial + (fatorial * n)
print("o fatorial do numero {} é {}".format(numero, fatorial))