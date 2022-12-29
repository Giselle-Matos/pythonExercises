# Utilize uma função domódulo mathparacalcular e retornar a distância
# entre dois pontos dadas as suas coordenadas

from math import dist
ponto1 = []
ponto2 = []
i = 0
while i < 3:
    a = int(input('Digite aa coordenadas do ponto 1: '))
    b = int(input('Digite as coordenadas do ponto 2: '))
    i = i + 1
    ponto1.append(a)
    ponto2.append(b)

print('ponto1= ', ponto1, 'ponto2= ', ponto2)
print(dist(ponto1, ponto2))
