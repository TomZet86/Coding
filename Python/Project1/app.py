mesta = ["Praha", "Viden", "Olomouc", "Svitavy", "Zlin", "Ostrava"]
domeny = ("gmail.com", "seznam.cz", "email.cz")
slevy = ("Olomouc", "Svitavy", "Ostrava")
ceny = (150, 200, 120, 120, 100, 180)
dvojita_cara = "=" * 35
cara = "-" * 35
nabidka = """
1 - Praha   | 150
2 - Viden   | 200
3 - Olomouc | 120
4 - Svitavy | 120
5 - Zlin    | 100
6 - Ostrava | 180
"""
AKT_ROK = 2021

print('vitejte u nasi aplikace destinatio'.upper())
print(dvojita_cara, end='')
print(nabidka, end='')
print(dvojita_cara)

vyber_destinace = int(input('Vyber cislo destinace: '))
if vyber_destinace in range(1,7):
    print('Destinace:',mesta[vyber_destinace - 1])
    print(cara)
    if mesta[vyber_destinace - 1] in slevy:
        print('ZISKAVATE 25% slevu! cena:'.upper(), ceny[vyber_destinace - 1] / 100 * 75)
        cena_jizdneho = ceny[vyber_destinace - 1] / 100 * 75
        print(cara)
    else:
        print('cena:'.upper(), ceny[vyber_destinace - 1])
        cena_jizdneho = ceny[vyber_destinace - 1]
        print(cara)
else:   
    print('vyber:'.upper(), vyber_destinace, 'neexistuje! Ukoncuji')
    quit()
print(cara)
   
    
cele_jmeno = input('Zadej cele jmeno: ')
rozdelene_jmeno = cele_jmeno.split(" ")
if rozdelene_jmeno[0].isalpha():
    print('Jmeno je v poradku')
else:
    print('Jmeno nebo prijmeni nejsou v poradku! Ukoncuji..')
    quit()
print(cara)
    
email = input('Zadej svuj email: ')


if '@' in email and email.split("@")[1] in domeny:
    print('Email je v poradku')
    print('Dekuji,', rozdelene_jmeno[0] + ' ,za obejdnavku'.upper() )
    print('cil. destinace:'.upper(), mesta[vyber_destinace - 1],'cena jizdneho:'.upper(), str(cena_jizdneho) + ",-" )
    print('na tvuj email:'.upper(), email, 'jsme ti poslali listek'.upper())
else:
    print('Neplatna emailova adresa. Ukoncuji..')
    quit()
print(dvojita_cara)