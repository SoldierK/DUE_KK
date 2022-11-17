def hossz(jelszo): #psw-t vizsgáljuk
    hiba = False #vizsgálat alapértéke
    if len(jelszo) < 8:
        print('Nem elég hosszú jelszó (min 8 karakter)!')
        hiba = True #vizsgálat eredménye
    return hiba

def szamjegyek(jelszo):
    hiba = True
    for i in range(len(jelszo)):
        if jelszo[i].isnumeric():
            hiba = False
            break #ha talál egyet kilép
    if hiba:
        print('Számjegyet kell tartalmaznia!')
    return hiba

def nagybetu(jelszo):
    hiba = True
    for i in range(len(jelszo)):
        if jelszo[i].isupper():
            hiba = False
            break #ha talál egyet kilép
    if hiba:
        print('Nagybetűt kell tartalmaznia!')
    return hiba

def kisbetu(jelszo):
    hiba = True
    for i in range(len(jelszo)):
        if jelszo[i].islower():
            hiba = False
            break  # ha talál egyet kilép
    if hiba:
        print('Kisbetűt kell tartalmaznia!')
    return hiba

def jelszo_bekerese():
    hibakod = 1 #hogy belépjen a whileba
    while hibakod != 0:
        hibakod = 0
        psw = input('Kérek egy jelszót: ')
        if hossz(psw): #hibát visszaadjuk ide, eldönti h folytatjuk-e
            hibakod += 1 #ha talál hibát
        if szamjegyek(psw):
            hibakod += 1
        if nagybetu(psw):
            hibakod += 1
        if kisbetu(psw):
            hibakod += 1
    print('\nSikeres jelszó!')
    return psw

def jelszo_ellenorzes():
    jelszo1 = jelszo_bekerese()
    jelszo2 = input('\nKérem ismételje meg a jelszót!: ')
    probalkozas = 1
    while jelszo1 != jelszo2: #ha nem egyezik akkor kéri ismét
        if probalkozas == 3: break
        jelszo2 = input('\nNem egyforma a két jelszó, kérem ismételje meg!: ')
        probalkozas +=1

    if probalkozas == 3:
        print('\nNem sikerült jelszót választani, regisztráció vége!')
    else:
        print('\nKész a regisztráció!')
    with open('jelszo.txt', 'a', encoding='utf-8') as user:
        user.write('\n' + jelszo1)

def felhasznalonev():
    print('A regisztrációhoz kérek egy felhasználónevet és jelszót')
    felhasznalonev = input('Kérem a felhasználóneved (email): ')
    while '@' not in felhasznalonev or '.' not in felhasznalonev or ' ' in felhasznalonev:
        print('Nem megfelelő email cím!')
        felhasznalonev = input('Kérem a felhasználóneved (email): ')
    with open('jelszo.txt', 'w', encoding='utf-8') as user:
        user.write(felhasznalonev)

felhasznalonev()
jelszo_ellenorzes()

print('BELÉPTETÉS')
with open('jelszo.txt', 'r', encoding='utf-8') as fajl:
    user_fajl = fajl.readlines()

user = input('Kérem a felhasználónevét: ')
if user_fajl[0].strip() != user:
    print('Nincs ilyen felhasználó!')
else:
    jelszo = input('Kérem a jelszót: ')
    probalkozas = 1
    while jelszo != user_fajl[1]:
        if probalkozas == 3: break
        print('Nem megfelelő jelszó!')
        jelszo = input('Kérem a jelszót: ')
        probalkozas +=1
    if probalkozas == 3:
        print('Belépés megtagadva!')
    else:
        print('Belépett a rendszerbe!')