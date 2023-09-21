numero = input("Digite um numero inteiro: ")

if numero.isdigit():
    numero_int = int(numero)
    numero_par = numero_int % 2 == 0
    
    if numero_par:
        print("Seu numero é inteiro") 
        print("Seu numero é par")
    else:
        print("Seu numero é inteiro") 
        print("Seu numero é impar");
else:
    print("Seu numero não é inteiro");
 