pi = 3.14

def osszeg(a, b):
    return a+b

def bevitel(tipus):             #  sz - szám,  m - művelet, (4 - négy hosszúságú)
    if tipus == 'sz':
        sz_text = input('Kérek egy egész számot számjegyekkel: ')
        while not sz_text.isnumeric():
            print('Nem számokat írt be!')
            sz_text = input('Kérek egy egész számot számjegyekkel: ')
        vissza = int(sz_text)
    elif tipus == 'm':
        muvelet = input('Kérek egy műveleti jelet (+,-,*,/): ')
        while muvelet not in ['+', '-', '*', '/']:
            print('Nem létező műveleti jel!')
            muvelet = input('Kérek egy műveleti jelet (+,-,*,/): ')
        vissza = muvelet
    return vissza

def szamolas(szam1, muvelet, szam2):
    if muvelet == '+':
        l_eredmeny = szam1 + szam2
    elif muvelet == '-':
        l_eredmeny = szam1 - szam2
    elif muvelet == '*':
        l_eredmeny = szam1 * szam2
    elif muvelet == '/':
        l_eredmeny = szam1 / szam2
    return l_eredmeny

def kimenet(szam1, muvelet, szam2, eredmeny, x):
    print('Az eredmény:'.center(x, ' '))
    print(str(szam1).rjust(x, ' '))
    print(str(szam2).rjust(x, ' '))
    print(muvelet, ''.rjust(x-1, '_'))
    print(str(eredmeny).rjust(x, ' '))
