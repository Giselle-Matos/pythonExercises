n = int(input('Digite a posição do numero da serie de fibonacci: '))

def fibonacci(n):
    i=0
    lista = [1, 1]
    while i<=n:
        i=i+1
        fib=(lista(i))+(lista(i+1))
        lista.append(fib)
    print(lista)
    return
print(fibonacci(n))