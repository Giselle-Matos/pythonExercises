vetor = []
lista = []
lista_pares = []
lista_impares = []
i = 0
while i == 0:
    x = int(input('Digite um numero (para parar, digite um valor negativo): '))
    if x < 0:
        break
    vetor.append(x)
    if x > 5:  # adicionar os numeros maiores do que 5 na lista
        lista.append(x)
    if (x % 2) == 0:
        lista_pares.append(x)
    if (x % 2) != 0:
        lista_impares.append(x)
print(vetor)
print('A quantidade de numeros maiores do que 5 é: ', len(lista))  # imprimir o
# tamanho da lista dos numeros maiores do que 5
# para encontrar a quantidade de numeros maiores do que 5
print('A soma dos numeros pares é igual a: ', sum(lista_pares))
print('A soma dos numeros impares é: ', sum(lista_impares))
print('A quantidade total de valores do vetor é: ', len(vetor))
