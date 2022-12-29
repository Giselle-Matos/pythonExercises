# Utilize uma  função  do módulo mathparacalcular
#  o perímetro  de  umtriângulo  retângulo dados  os  seus  catetos.
#  Os  catetos  devem  ser  passados  por  argumento  e  um  dos
# catetos deve ter valor padrão igual
# a 3 e o outroigual a 5.A função deve retornar o perímetro.

catopt = int(input('Digite o cateto oposto: '))
catadj = int(input('Digite o cateto adjacente: '))
h = int(input('Digite a hipotenusa: '))


def perimetro(catopt, catadj, h):
    if ((catopt-catadj) < h < catopt+catadj):
        return(catopt+catadj+h)
    else:
        print('Não é um triângulo retângulo, logo nao calcularemos o perímetro.')


print(perimetro(catopt, catadj, h))

