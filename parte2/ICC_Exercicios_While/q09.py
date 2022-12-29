a = int(input('Digite o valor: '))
i = 0
nota50 = 0
nota20 = 0
nota10 = 0
nota5 = 0

while i < a and (i + 50)<=a:
    i += 50
    nota50 += 1
a = a - i
i=0
while i < a and (i + 20)<=a:
    i += 20
    nota20 += 1
a = a - i
i=0
while i < a and (i + 10)<=a:
    i += 10
    nota10 += 1
a = a - i
i=0
while i < a and (i + 5)<=a:
    i += 5
    nota5 += 1
a = a - i
i=0

print(nota50, 'notas de 50, ',nota20, 'notas de 20',
nota10,'notas de 10',nota5,'notas de 5')

# tentar fazer com if 