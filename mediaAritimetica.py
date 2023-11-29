from os import system, name
system('cls') if(name == 'nt)') else system('clear')

print("media Aritimetica")
n1 = float (input('informe a 1ª nota'))
n2 = float (input('informe a 2ª nota'))
n3 = float (input('informe a 3ª nota'))
n4 = float (input('informe a 4ª nota'))
media = (n1+n2+n3+n4)/4
print(f"a media de : {n1} | {n2} | {n3} | {n4}:{media:.2f}")