#  Recebe  dois  números  inteirose  positivospor  argumento,
#  x  e  y,  e  calcula  x  elevado  a  y. 
# y deve ter valor padrão igual a 2. 
# Retorne o valor resultante. 
# Não utilize o duplo asterisco ou qualquer módulo do Python.

x = int(input('Digite outro número: '))
y = int(input('Digite outro numero: '))
aux = x
while 1 < y:
    y -= 1
    aux *= x
print(aux)