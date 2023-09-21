#declaração das variaveis
nome = input ("Digite nome completo. (Ex: João da Silva):")
altura = float(input("Digite sua altura em metros. (Ex: 1.80):"))
peso = float(input("Digite seu peso em Kg. (Ex: 90.5):"))
imc = peso / altura ** 2

#usando as fStrings para concatenar textos e variaveis em string
linha_texto1 = f'Seu peso é: {peso:.2f} - Sua Altura é: {altura:.2f} Seu IMC é: {imc:.2f}, Voce esta abaixo do peso '
linha_texto2 = f'Seu peso é: {peso:.2f} - Sua Altura é: {altura:.2f} Seu IMC é: {imc:.2f}, Voce esta no seu peso normal '
linha_texto3 = f'Seu peso é: {peso:.2f} - Sua Altura é: {altura:.2f} Seu IMC é: {imc:.2f}, Voce esta com excesso de peso '
linha_texto4 = f'Seu peso é: {peso:.2f} - Sua Altura é: {altura:.2f} Seu IMC é: {imc:.2f}, Voce esta com obesidade grau I '
linha_texto5 = f'Seu peso é: {peso:.2f} - Sua Altura é: {altura:.2f} Seu IMC é: {imc:.2f}, Voce esta com obesidade grau II '
linha_texto6 = f'Seu peso é: {peso:.2f} - Sua Altura é: {altura:.2f} Seu IMC é: {imc:.2f}, Voce esta com obesidade grau III '


#condicionais para cada case com if e elif
if imc <= 18.5: 
    print(linha_texto1)

elif imc > 18.5 and imc < 24.9: 
    print(linha_texto2)

elif imc > 25.0 and imc < 29.9: 
    print(linha_texto3)

elif imc > 30.0 and imc < 34.9: 
    print(linha_texto4)

elif imc > 35.0 and imc < 39.9: 
    print(linha_texto5)

elif imc > 40:
    print(linha_texto6)

else:
    print('erro');

print("Cuide de sua saúde!")