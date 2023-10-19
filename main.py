''' kérj be két számot a felhasználótól (main.py)
Írj eljárást
    szamok néven (ciklusok.py)
    melynek a paramétere a felhasználó által megadott két szám
    és
    az eljárás kiírja az egész számokat ezen két paraméter között.
'''
import ciklusok

a: int= int(input("Adjon meg egy számot (a) : "))

b: int= int(input("Adjon meg még egy számot (b) : "))
""" A felhasználó csak olyan b-t tudjon megadni, ami nagyobb, mint az a """
while (a>b):
    print("b-nek nagyobbnak kell lennie a-nál")
    b:int = int(input(f"Adj {a}-nál nagyobbat! "))

ciklusok.szamok(a, b)