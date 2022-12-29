d = {'Joao':2, 'Giselle':17,'Nathan':18,'Ana Eliza':167}
D = d.copy()
lista = []
laux = (d.keys())
laux = list(laux)

for a in range(0,len(laux)):
    chave = laux[a]
    if d[chave] < 18:
        D.pop(chave)
print(D)