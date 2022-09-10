'''Exercício Python 095: Aprimore o desafio 93 para que ele funcione com vários jogadores,
incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.'''
jogador = dict()
partidas = list()
time = list()
while True:
    jogador.clear()
    jogador["nome"] = str(input("jogador: "))
    tot = int(input("total de partidas: "))
    partidas.clear()
    for i in range(0,tot):
        partidas.append(int(input(f"quantos gols na partida {i}? ")))
    jogador["gols"]=partidas[:]
    jogador["total"]=sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input("quer continuar S/N: ")).upper()[0]
        if resp in "SN":
            break
        print("erro digite S/N!")
    if resp == "N":
        break

print("=-"*20)
print("Cod ", end="")
for i in jogador.keys():
    print(f"{i:<15}",end='')
print()
print("=-"*20)
for k,v in enumerate(time):
    print(f"{k:>3} ",end="")
    for d in v.values():
        print(f"{str(d):<15}",end='')
    print()
print("=-"*20)
while True:
    busca =int(input("mostrar dados de qual jogador? (999 para parar): "))
    if busca == 999:
        break
    if busca >= len(time):
        print(f"jogador não existe, tente novamente! erro = {busca} ")
    else:
        print(f'--Levantamento do jogador: {time[busca]["nome"]}:')
        for i,g in enumerate(time[busca]["gols"]):
            print(f"   no jogo {i+1} fez {g} gols")
print("=-"*20)