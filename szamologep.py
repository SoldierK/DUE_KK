# Ez a program egy négy alapműveletes számológép
import  sajat_modul
from sajat_modul import kimenet

print('''Ez egy olyan program, 
amely számológépként működik
''')

szam1 = sajat_modul.bevitel('sz')
muvelet = sajat_modul.bevitel('m')
szam2 = sajat_modul.bevitel('sz')

eredmeny = sajat_modul.szamolas(szam1, muvelet, szam2)

kimenet(szam1, muvelet, szam2, eredmeny, 30)
