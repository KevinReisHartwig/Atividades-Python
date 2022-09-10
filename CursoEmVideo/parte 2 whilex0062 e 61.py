'''Exercício Python 62: Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encerrará quando ele disser que quer mostrar 0 termos.'''
print("Gerador de Pa")
print("-="*10)
primeiro = int(input("digite o primeiro termo: "))
razão = int(input("digite a razão PA: "))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print("{} ->".format(termo),end='')
        termo = termo + razão
        cont = cont + 1
    print("Pausa")
    mais = int(input("quantos termos você quer a mais? "))
print("um totoal de {} termos".format(total))