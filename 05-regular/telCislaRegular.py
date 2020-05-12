"""
telCislaRegular.py

cvičení na regulární výrazy
parsuje americká telefonní čísla (různé tvary) do čtyřprvkové n-tice
několik verzí, šestá a sedmá funguje pro celý vzorek

Následující věci už by vám neměly být cizí:
^ odpovídá začátku řetězce.
$ vyjadřuje konec řetězce.
\b odpovídá hranici slova (word boundary).
\d odpovídá číslici.
\D odpovídá znaku jinému než číslice.
x? odpovídá nepovinnému znaku x (jinými slovy vyjadřuje žádný nebo jeden výskyt x).
x* vyjadřuje nula nebo více výskytů x.
x+ odpovídá x jedenkrát nebo víckrát.
x{n,m} vyjadřuje znak x opakovaný nejméně n-krát, ale ne více než m-krát.
(a|b|c) odpovídá přesně jedné z možností a, b nebo c.
(x) vyjadřuje obecně zapamatovanou skupinu. Hodnotu zapamatované skupiny můžeme
získat voláním metody groups() objektu, který byl vrácen voláním re.search.
"""
import re

def prvni_verze(cislo):
    phonePattern = re.compile(r'^(\d{3})-(\d{3})-(\d{4})$') # začátek, 3 číslice, pomlčka, 3 číslice, pomlčka, 4 číslice, konec řetězce. Každou skupinu v závorce si zapamatuje
    print(f'{cislo} ... {phonePattern.search(cislo).groups()}')     # .groups vrací n-tici prvků (skupin) v regulárním výrazu oddělených závorkami (viz předchozí řádek)

def druha_verze(cislo):
    # začátek, 3 číslice, pomlčka, 3 číslice, pomlčka, 4 číslice, pomlčka, skupina jedné nebo více číslic, konec řetězce. Každou skupinu v závorce si zapamatuje
    phonePattern = re.compile(r'^(\d{3})-(\d{3})-(\d{4})-(\d+)$') 
    print(f'{cislo} ... {phonePattern.search(cislo).groups()}')     # .groups vrací n-tici prvků (skupin) v regulárním výrazu oddělených závorkami (viz předchozí řádek)

def treti_verze(cislo):
    # začátek, 3 číslice, libovolný nečíselný znak, 3 číslice, libovolný nečíselný znak, 4 číslice, libovolný nečíselný znak, skupina jedné nebo více číslic, konec řetězce. 
    # Každou skupinu v závorce si zapamatuje
    phonePattern = re.compile(r'^(\d{3})\D+(\d{3})\D+(\d{4})\D+(\d+)$') 
    print(f'{cislo} ... {phonePattern.search(cislo).groups()}')     # .groups vrací n-tici prvků (skupin) v regulárním výrazu oddělených závorkami (viz předchozí řádek)

def ctvrta_verze(cislo):
    # + v regulárním výrazu znamená jednou nebo vícekrát, * znamená nula nebo vícekrát
    # začátek, 3 číslice, nepovinný libovolný nečíselný znak (nebo více znaků), 3 číslice, nepovinný libovolný nečíselný znak (nebo více znaků), 4 číslice, nepovinný libovolný nečíselný znak (nebo více znaků), volitelná skupina jedné nebo více číslic, konec řetězce. 
    # Každou skupinu v závorce si zapamatuje
    phonePattern = re.compile(r'^(\d{3})\D*(\d{3})\D*(\d{4})\D*(\d*)$') 
    print(f'{cislo} ... {phonePattern.search(cislo).groups()}')     # .groups vrací n-tici prvků (skupin) v regulárním výrazu oddělených závorkami (viz předchozí řádek)

def pata_verze(cislo):
    # + v regulárním výrazu znamená jednou nebo vícekrát, * znamená nula nebo vícekrát
    # začátek, nepovinný libovolný nečíselný znak (nebo více znaků), 3 číslice, nepovinný libovolný nečíselný znak (nebo více znaků), 3 číslice, 
    # nepovinný libovolný nečíselný znak (nebo více znaků), 4 číslice, nepovinný libovolný nečíselný znak (nebo více znaků), 
    # volitelná skupina jedné nebo více číslic, konec řetězce. 
    # Každou skupinu v závorce si zapamatuje, první skupinu mimo závorky si nepamatuje
    phonePattern = re.compile(r'^\D*(\d{3})\D*(\d{3})\D*(\d{4})\D*(\d*)$') 
    print(f'{cislo} ... {phonePattern.search(cislo).groups()}')     # .groups vrací n-tici prvků (skupin) v regulárním výrazu oddělených závorkami (viz předchozí řádek)

def sesta_verze(cislo):
    # jediná změna oproti předchozí verzi - neukotvujeme začátek řetězce a netestujeme jej (chybí ^\D*)
    # a funguje na všechna telefonní čísla z našeho vzorku
    
    phonePattern = re.compile(r'(\d{3})\D*(\d{3})\D*(\d{4})\D*(\d*)$') 
    print(f'{cislo} ... {phonePattern.search(cislo).groups()}')     # .groups vrací n-tici prvků (skupin) v regulárním výrazu oddělených závorkami (viz předchozí řádek)

def sedma_verze(cislo):
    # ten samý regulární výraz víceslovně
    # a funguje na všechna telefonní čísla z našeho vzorku
    
    phonePattern = re.compile(r'''
                # nevázat se na začátek řetězce, číslo může začít kdekoli
    (\d{3})     # číslo oblasti má 3 číslice (např. 800)
    \D*         # nepovinný oddělovač - libovolný počet nenumerických znaků
    (\d{3})     # číslo hlavní linky 3 číslice (např. 555)
    \D*         # nepovinný oddělovač - libovolný počet nenumerických znaků
    (\d{4})     # zbytek čísla má 4 číslice (např. 1212)
    \D*         # nepovinný oddělovač - libovolný počet nenumerických znaků
    (\d*)       # nepovinná klapka - libovolný počet číslic
    $           # konec řetězce
    ''',re.VERBOSE)
    print(f'{cislo} ... {phonePattern.search(cislo).groups()}')     # .groups vrací n-tici prvků (skupin) v regulárním výrazu oddělených závorkami (viz předchozí řádek)

tel_cisla = [
'800-555-1212', 
'800-555-1212-1234', 
'800 555 1212', 
'800.555.1212', 
'(800) 555-1212', 
'1-800-222-1212', 
'800-555-1212x1234', 
'800-555-1212 ext. 1234',
'work 1-(800) 555.1212 #1234',
'80055512121234'
]

for i in range(0,10):   
    #print(i)
    #prvni_verze(i)      # první verze - projde první řetězec, na druhém chyba
    #druha_verze(i)      # funguje pro druhé číslo, ale pro první ne, tj. umí číslo se 4 skupinami oddělenými pomlčkami, neumí číslo se 3 skupinami. Neumí jiné oddělovače než pomlčky
    #treti_verze(i)     # projde druhé, sedmé, osmé číslo, tj. umí číslo s libovolným oddělovačem se 4 skupinami
    #ctvrta_verze(i)     # projde 1. - 4. číslo, sedmé, osmé, desáté. neprojde 5. - 6. a 9. Umí to samé jako treti_verze() a navíc čísla bez oddělovače a i čísla jen s 3 skupinami
    #pata_verze(tel_cisla[i])   # projdou všechny čísla kromě 6. a 9. 
    #sesta_verze(tel_cisla[i])   # projdou všechna čísla 
    sedma_verze(tel_cisla[i])   # projdou všechna čísla, pouze regularni vyraz je víceslovný