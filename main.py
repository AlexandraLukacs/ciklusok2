''' kérj be két számot a felhasználótól (main.py)
Írj eljárást
    szamok néven (ciklusok.py)
    melynek a paramétere a felhasználó által megadott két szám
    és
    az eljárás kiírja az egész számokat ezen két paraméter között.
'''

szam1: int= int(input("Adjon meg egy számot: "))
szam2: int= int(input("Adjon meg még egy számot: "))

import ciklusok
ciklusok.szamok(szam1, szam2)