# DUE_KK
Szkript nyelvek - 2022-23/1

RockPaperScissors project - Készítette: Katona Kristóf (J9OC1F)

A program egy egyszerű kő-papír-olló játék, minden kötelező elemet tartalmaz a grafikai modulon kívül. PyCharm feljesztő rendszerben készült.

A program 3 alap Python import modult tartalmaz (random,os,time).
random: random számgenerálást biztosítja
os: operációs rendszer függvénye, esetünkben a konzolon lévő összes szöveget törléséért felelős
time: időfüggvények, késleltetésért lesz felelős

Ezután 3 definíció jön.
clear(): a konzolra kiírt adatokat fogja letörölni két játék között
rps_instructions(): a játék alapszabályait írja ki a konzolra
rps(): 3 globális változót tartalmaz

While ciklusban lesz minden egyes játék leírása, hogy a játékos milyen opciók közül választhat. Helytelen bevitel esetén kiírja és rövid késleltetés után újraküldi a ciklust.
help: segítséget kér a játékszabályokról
rock,paper,scissors: egyiket beírva kiválasztja a választott az adott játékban használt "jelét"
exit: kilép a programból

comp_move: a computernek ad egy random számot 0, 1 és 2 között

Ezután elhelyezi ez a számot a mátrixban a játékos által adott értékkel együtt és a mátrix szabályai alapján eldönti a nyertest, majd kiírja a konzolra.



