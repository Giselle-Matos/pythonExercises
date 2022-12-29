d = {'Joao':2, 'Ana': 20,'Pedro': 31, 'Maria': 10, 'Luiz':18}
D=d.copy()
lista = []
lista = list(d.keys())

for i in range(0,len(lista)): 
    chave = lista[i]
    if d[chave]<18:
        D.pop(chave)
    
print(D)