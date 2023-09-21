hora = input("Digite as horas em numero inteiro: ")

if hora.isdigit():
    hora_int = int(hora)

    if hora_int >= 0 and hora_int <=11:
        print("Bom dia")

    elif hora_int >= 12 and hora_int <=17:
        print("Boa tarde")
        
    elif hora_int >= 18 and hora_int <=23:
        print("Boa noite")
    else:
        print("Hora não reconhecida")
else:
    print("Hora invalida, digite numeros inteiros")