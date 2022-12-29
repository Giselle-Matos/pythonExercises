# Faça uma função em Python que recebe um número n por argumento e retorna
# True se ele for  perfeito  ou False  se  não  for.

a = int(input('Digite um numero: '))
i = 1
lista = []
while i <= a:
    i = i+1
    if (a % i) == 0:
        lista.append(i)
if (sum(lista)) == a:
    print('É um número perfeito.')
else:
    print('Não é um numero perfeito.')
print(lista)
print(sum(lista))

