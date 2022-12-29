#  Função  que  recebe  uma  string referente  a  um  mês  e
#  retorna  o valor  numérico  referente àquele  mês.
#  Defina  um  dicionário  dentro  da  função  que  permita  esse
#  mapeamento  para qualquer mês. Se a string passada não forválida,
#  imprimauma mensagem de erro.

a = str(input('Digite o mês por extenso: '))

d = {'Janeiro':1, 'Fevereiro':2,'Março':3,'Abril':4,'Maio':5,'Junho':6,
'Julho':7,'Agosto':8,'Setembro':9,'Outubro':10,'Novembro':11,'Dezembro':12}

if a in d:
    print(d[a])
else: 
    print('O mês é inválido')