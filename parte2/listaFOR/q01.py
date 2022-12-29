lista = [1,2,3,4,5,6,63]
def media(lista):
    soma = 0
    for i in range(0,len(lista)):
        soma = soma + lista[i]
    media = soma/len(lista)
    return
print(media(lista))