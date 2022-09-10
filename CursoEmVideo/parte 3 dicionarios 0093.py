'''Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol.
O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final,
tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.'''
jogador = dict()
partidas = list()
jogador["nome"] = str(input("jogador: "))
tot = int(input("total de partidas: "))
for i in range(0,tot):
    partidas.append(int(input(f"quantos gols na partida {i}? ")))
jogador["gols"]=partidas[:]
jogador["total"]=sum(partidas)
print("=-"*20)
print(jogador)
print("=-"*20)
for k,v in jogador.items():
    print(f"o campo {k} tem o valor {v}")
print("=-"*20)
print(f'o jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas ')
for i,v in enumerate(jogador["gols"]):
    print(f"   => Na partida {i+1}°, fez {v} gols")
print(f'Foi um total de {jogador["total"]} gols')