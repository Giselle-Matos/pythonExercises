# Recebea  quantidade  de habitantes
# e  a taxa  anual  de  crescimento  de dos  países
#  A e  Be calcula e retornao número de anos
# necessários para que a populaçãodo paísA ultrapasse ou
# iguale  a  população  do  país  B considerando  que
# não há  alteração  nastaxas  de crescimento.

habA = int(input('Digite a quantidade de habitantes do país A: '))
taxaA = float(input('Digite a taxa de crescimento do país A: '))
habB = int(input('Digite a quantidade de habitantes do país B: '))
taxaB = float(input('Digite a taxa de crescimento do país B: '))
anos = 1
popA = habA
popB = habB

if taxaA > taxaB:
    while popA < popB:

        popA = habA*taxaA
        habA = popA
        popB = habB*taxaB
        popB = popB
        anos += 1

else:
    print('Taxa inválida')

print(anos)
