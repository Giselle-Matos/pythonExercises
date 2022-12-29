from random import randint
i = 0
lista = []
qtd = 0

while i< 50:
    i=i+1
    x=randint(0, 20)
    lista.append(x)

print('esta é a soma dos itens da lista: ', sum(lista)) # soma os valores da lista aleatoria

for n in range(0, 50):
    y = lista[0 + n]
    if y==9:
        qtd=qtd+1
print('essa é a quantidade de "9" da lista: ', qtd)
print('essa é a lista: ', lista)
print('essa é a posição do numero 9: ', lista.index(9))
