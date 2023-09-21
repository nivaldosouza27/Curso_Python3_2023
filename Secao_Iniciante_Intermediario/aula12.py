nome = input("Digite nome completo. (Ex: João da Silva):")
altura = float(input("Digite sua altura em metros. (Ex: 1.80):"))
peso = float(input("Digite seu peso em Kg. (Ex: 90.5):"))

imc = round (peso / (altura ** 2), 1)

if imc <= 18.5: 
    print("Seu IMC é:", imc, 'Voce esta abaixo do peso')

elif imc > 18.5 and imc < 24.9: 
    print('Seu IMC é:', imc, 'Voce esta no seu peso normal')

elif imc > 25.0 and imc < 29.9: 
    print('Seu IMC é:', imc, 'Voce esta com excesso de peso')

elif imc > 30.0 and imc < 34.9: 
    print('Seu IMC é:', imc, 'Voce esta com obesidade grau I')

elif imc > 35.0 and imc < 39.9: 
    print('Seu IMC é:', imc, 'Voce esta com obesidade grau II')

elif imc > 40:
    print('Seu IMC é:', imc, 'Voce esta com obesidade grau III')


