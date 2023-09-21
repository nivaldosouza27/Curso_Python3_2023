##### Calculadora com IF ######

entrada01   = input("Digite um primeiro numero inteiro: ")
operador    = input("Digite um dos operadores (+,-,*,/): ")
entrada02   = input("Digite um segundo numero inteiro: ")

if entrada01.isdigit() and entrada02.isdigit():
    num01 = int(entrada01)
    num02 = int(entrada02)
    resultado = int()
    if operador == "+":
        resultado = num01 + num02
        print(f'{num01} + {num02} = {resultado}')

    elif operador == "-":
        resultado = num01 - num02
        print(f'{num01} - {num02} = {resultado}')

    elif operador == "*":
        resultado = num01 * num02
        print(f'{num01} * {num02} = {resultado}')

    elif operador == "/":
        resultado = num01 / num02
        print(f'{num01} / {num02} = {resultado}')
    
    else: 
        print(f'{operador} não é um operador válido')

elif entrada01.isdigit() and entrada02.isdigit() is False:
    print(f'{entrada02} não é um numeros valido para este programa')
    print('Digite somente numeros inteiros')

elif entrada01.isdigit() is False and entrada02.isdigit():
    print(f'{entrada01} não é um numeros valido para este programa')
    print('Digite somente numeros inteiros')

else:
    print(f'{entrada01} e {entrada02} não são numeros validos para este programa')
    print('Digite somente numeros inteiros')
