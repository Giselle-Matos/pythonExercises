x = int(input('Digite um numero: '))


import math

def seno(x):
    
    mudasinal = 1
    soma = 0

    for n in range(3, 21, 2):

        if (mudasinal%2) == 0:
            soma = soma + (x**n) / math.factorial(n)
        else:
            soma = soma - (x**n) / math.factorial(n)
        
        mudasinal = mudasinal + 1 

    return x + soma 

print(seno(x))
