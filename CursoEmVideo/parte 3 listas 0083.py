'''Exercício Python 083: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar
se a expressão passada está com os parênteses abertos e fechados na ordem correta.'''
exp = str(input("digite a expresão: "))
pilha = []
for simb in exp:
    if simb == "(":
        pilha.append("(")
    elif simb == ")":
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(")")
            break
if len(pilha) == 0:
    print("valido")
else:
    print("invalido")