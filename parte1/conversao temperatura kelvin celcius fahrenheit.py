a = float(input('Digite a temperatura: '))
b = int(input('Indique a conversão de 1 a 6: '))


def temperatura(a, b):
    if (b == 1):
        print('Celcius para Fahrenheit: ')
        return 9*(a/5)+32
    elif (a == 2):
        print('Celcius para Kelvin: ')
        return (a + 273)
    elif (a == 3):
        print('Fahrenheit para Celcius: ')
        return (5*(a - 32))/9
    elif(a == 4):
        print('Fahrenheit para Kelvin: ')
        return (5*(a - 32))/9 + 273
    elif(a == 5):
        print('Kelvin para Celcius: ')
        return a - 273
    elif(a == 6):
        print('Kelvin para Fahrenheit: ')
        return ((9*(a - 273))/5)+32


print(temperatura(a, b))

