def tabuada():
    aux = 0
    
    while aux < 9:
        aux += 1
        resultado = numero*aux
        print(resultado)
        
numero = int(input('Digite um número: '))
tabuada()
