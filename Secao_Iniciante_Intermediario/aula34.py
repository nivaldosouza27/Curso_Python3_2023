def is_par_impar(numero):
    resultado = numero % 2 == 0
    if resultado:
        return f'Numero Par'
    return f'Numero Impar'
    
numero_digitado = input('Digite um numero: ')
is_par_impar(int(numero_digitado))
