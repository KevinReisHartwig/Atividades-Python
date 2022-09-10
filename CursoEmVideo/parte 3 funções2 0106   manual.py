'''Exercício Python 106: Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer. Quando
o usuário digitar a palavra ‘FIM’, o programa se encerrará. Importante: use cores.'''
c = ("\033[n",
     "\033[7;30m")
def ajuda(con):
    print(c[1],end="")
    help(con)
    print(c[0], end="")


def titulo(msg, cor=0):
    tam = len(msg) + 4
    print("=" * tam)
    print(f" {msg}")
    print("=" * tam)

comando = ''
while True:
    titulo("sistema de ajuda Pyhelp!")
    comando = str(input("função da biblioteca: "))
    if comando.upper() == "FIM":
        break
    else:
        ajuda(comando)
titulo("ate logo")

