#update
# While para que o Programa não feche
while True:

    try:
        # Input para pedir o valor
        valor = int(input('Digite um valor: '))
        # Comparando o Valor
        if valor % 2 == 0:
            print('Par')
        else:
            print('Impar')
    except:
        # Caso o usuario digite uma string
        print('Digite somente números')
