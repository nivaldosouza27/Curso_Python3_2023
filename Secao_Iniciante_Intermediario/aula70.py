# Funções recursivas e recursividade
# - funções que podem se chamar de volta
# - úteis p/ dividir problemas grandes em partes menores
# Toda função recursiva deve ter:
# - Um problema que possa ser dividido em partes menores
# - Um caso recursivo que resolve o pequeno problema
# - Um caso base que para a recursão
# - fatorial - n! = 5! = 5 * 4 * 3 * 2 * 1 = 120
# https://brasilescola.uol.com.br/matematica/fatorial.htm

## Função que formata o numero com separador de milhares e casas decimais
def formart_number(func):
    format_n = f'{func:_.2f}'.replace('.',',').replace('_','.')
    func = print(f'Seu fatorial de formatado é: "{format_n}"')
    return func

## Função recursiva que retorna o fatorial de 'n'
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)

#imprimindo a função factorial formatada
formart_number(factorial(15))

#imprimindo a função fatorial sem formatação
print(f'Seu fatorial não formatado é: "{factorial(15)}"')