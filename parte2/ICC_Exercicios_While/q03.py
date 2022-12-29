#  ecebe um número inteiro por argumento e calcula o somatório dos 
# números entre 1 e o número  passado  por  argumento(inclusive).
# A  variável recebida  por  argumento  deve  
# ter valor padrão igual a 0.O resultado do somatório deve ser retornado.
help(sum)
a = 0
a = int(input('Digite um numero: '))
i = 0
lista = []
while i <= a:
    lista.append(i)
    i = i + 1

print(sum(lista))