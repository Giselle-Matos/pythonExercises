def pares():
    n=50
    i=1
    somadepares = 0
    while(i==50):
        par = i%2
        if par == 0:
            somadepares = somadepares + 1
        i = i + 1
    print(somadepares)
    return
# soma dos numeros pares de 1 a 50
pares()
