# Recebe dois números inteiros por argumento e 
# retorna o somatório de todos os números pares 
# entre esses dois números (inclusive).

a = int(input('Digite um número: '))
b = int(input('Digite outro número: '))
i = a
lista = []

if (a % 2) == 0:
        lista.append(a)
if (b % 2) == 0:
        lista.append(b)
while i < b:
    i = i + 1
    if (i % 2) == 0 and (i != b):
        lista.append(i)

print(lista)    
print(sum(lista))
    