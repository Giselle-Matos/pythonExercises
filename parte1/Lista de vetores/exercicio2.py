vetor = [2, 1, 20, 5, 17, 19, 14, 4, 18, 5]
aux = vetor[0]
n = 1
while n < 10:
    temp = vetor[n]
    vetor[n]=aux
    aux = temp
    if n == 9:
        vetor[0]=vetor[9]
    n += 1
    print(vetor)
print(vetor)