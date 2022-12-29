# Faça uma função que recebe uma lista com nomes e números alternadamente (ex.: [‘Ana’, 10, ‘Pedro’, 9, ‘Maria’, 9, ‘Joao’, 10])e retorna um dicionário onde o nome é a chave e o número é o valor.


def dicionario(lista):
    d = {}
    i = 0
    z = len(lista)
    while i < z: 
        d[lista[i]]=lista[i+1]
        i = i + 2
    return(d)

print(dicionario(['Ana', 10, 'Pedro', 9, 'Maria', 9,'Joao', 10, 'Nathan', 509]))

