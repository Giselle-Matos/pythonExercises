a = int(input('Digite um número: '))
lista = [2, 3, 5, 7, 11, 13, 19, 23,  29, 31, 37, 41, 43, 47, 53]
i=0
z = len(lista)
while i < z:
    if (a%(lista[i]))==0:
        print('O numero não é primo.')
        break
    i = i + 1
    if  (a%1)==0 and (a%a)==0:
        print('O numero é primo')
        break