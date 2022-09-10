'''15. Leia dois conjuntos de números (podem ter o tamanho diferente) já ordenados de forma crescente.
Crie um outro vetor para armazenar os dois conjuntos unidos, sendo que os números devem
permanecer ordenados.
Finalmente, exiba este vetor resultante'''

nu1 = []
nu2 = []
somar = []
for i in range(5):
    n1 = int(input("digite um numero: "))
    n2 = int(input("digite um numero: "))
    nu1.append(n1)
    nu2.append(n2)
    soma = (sum(nu1) )+ (sum(nu2))
    somar.append(soma)


nu1.sort()
nu2.sort()

print("a soma dos conjuntos {} e {} é {}".format(nu1,nu2, somar))