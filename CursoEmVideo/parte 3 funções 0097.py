'''Exercício Python 097: Faça um programa que tenha uma função chamada escreva(),
que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.  '''
def escreve(msg):
    tan = len(msg)+4
    print("=-"*tan)
    print(f"  {msg}")
    print("=-" * tan)


escreve("Bom dia")