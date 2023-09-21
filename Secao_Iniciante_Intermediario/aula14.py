#declarando as variaveis

primeiro_valor = input("Digite o primeiro valor: ")
segundo_valor = input("Digite o segundo valor: ")

if float(primeiro_valor) > float(segundo_valor):
    print("Primeiro valor é: ",primeiro_valor,", e é maior que o segundo_valor: ",segundo_valor)
elif float(primeiro_valor) == float(segundo_valor):
    print("Primeiro valor é: ",primeiro_valor,", e é igual que o segundo_valor: ",segundo_valor)
elif float(primeiro_valor) < float(segundo_valor):
    print("Primeiro valor é: ",primeiro_valor,", e é menor que o segundo_valor: ",segundo_valor)
else:
    print("Valores Incorretos");