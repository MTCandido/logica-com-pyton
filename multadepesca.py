from os import system, name
system('cls') if(name == 'nt)') else system('clear')

kg = float (input('informe quantos kg de peixe'))
taxa = 4
if (kg > 50):
    diferenca = kg - 50
    multa = diferenca * taxa
    print(f"vc tem uma multa de R$ :{multa:.2f}")
else :
    print("vc nao tem multa para pagar")