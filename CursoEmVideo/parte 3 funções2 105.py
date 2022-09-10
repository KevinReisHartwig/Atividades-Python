'''Exercício Python 105: Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai
retornar um dicionário com as seguintes informações:

– Quantidade de notas
– A maior nota
– A menor nota
– A média da turma
– A situação (opcional'''

def notas(* n, sit=False):
    """---> função para ver as notas e situação dos alunos
    n = notas dos alunos
    sit = situação do aluno se quer ou não mostrar
    retunr: dicionario com varias informações sobre a situação da turma

    """

    r = {}
    r["total"] = len(n)
    r["maior"] = max(n)
    r["menor"] = min(n)
    r["media"] = sum(n)/len(n)
    if sit:
        if r["media"] >= 7:
            r["situação"] = "boa"
        elif r["media"] >= 5:
            r["situação"] = "razoavel"
        else:
            r["situação"] = "pessima"
    return r

resp = notas(4,5,7,8,9,8, sit=True)
print(resp)
help(notas)

