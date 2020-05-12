"""
mnozneCisloAj.py
kap.6

• Pokud slovo končí na S, X nebo Z, přidáme ES. Z bass se stává basses, z fax se stává faxes
a waltz se mění na waltzes.
• Pokud slovo končí hlasitým H, přidáme ES. Pokud končí tichým H, přidáme jen S. Co to je
hlasité H? Když H zkombinujeme s jinými písmeny, vydá zvuk, který slyšíme. Takže coach
[kouč] se změní na coaches a z rash [reš] se stane rashes, protože při vyslování slyšíme zvuky
pro CH [č] a SH [š]. Ale z cheetah [číta] se stane cheetahs, protože H je zde tiché.
• Pokud slovo končí písmenem Y, které zní jako I, změníme Y na IES. Pokud se Y kombinuje
se samohláskou tak, že zní jako něco jiného, pak pouze přidáme S. Vacancy se proto změní
na vacancies, ale z day se stane days.
• Pokud všechno selhalo, přidáme S a doufáme, že to projde.

"""
import re


def seznam_slov():
    # načtení souboru s anglickými slovy
    with open("c:/Users/krikavap/Documents/GitHub/python-ponorme-se-do-pythonu/05-regular/slova.txt", encoding="utf-8") as soubor:
        obsah = soubor.read()
    # vyčištění obsahu (nahrazení teček čárkami)
    slova = []
    slova = obsah.split(sep="\n")    # načtení řetězce s oddělovači (konec řádky) do seznamu (seznam = list)
    return (slova)
    
# přístup - varianta 1 
def plural_1(noun):
    """
    rozhodovací pravidla a substituční funkce je pohromadě ve funkci plural_1()
    """
    if re.search('[sxz]$', noun):        # slova končící na szx - přidáme -es
        return re.sub('$', 'es', noun)
    elif re.search('[^aeioudgkprt]h$', noun):   # slova, jejichž poslední znak před h není z řetězce aeioudgkprt - přidáme -es
        return re.sub('$', 'es', noun)
    elif re.search('[^aeiou]y$', noun):     # slova, jejichž poslední znak před písmenem y není z řetězce aeiou - přidáme -ies místo posledního y
        return re.sub('y$', 'ies', noun)
    else:                                   # k ostatním slovům přidáme prostě -s
        return noun + 's'

# přístup - varianta 2
# vyhledávací a substituční funkce jsou v samostatných funkcích (match..., apply...) a pravidla jsou v
def match_sxz(noun):
    return re.search('[sxz]$', noun)
def apply_sxz(noun):
    return re.sub('$', 'es', noun)

def match_h(noun):
    return re.search('[^aeioudgkprt]h$', noun)   # slova, jejichž poslední znak před h není z řetězce aeioudgkprt - přidáme -es
def apply_h(noun):
    return re.sub('$', 'es', noun)
    
def match_y(noun):
    return re.search('[^aeiou]y$', noun)     # slova, jejichž poslední znak před písmenem y není z řetězce aeiou - přidáme -ies místo posledního y
def apply_y(noun):
    return re.sub('y$', 'ies', noun)

def match_default(noun):
    return True                                  # k ostatním slovům přidáme prostě -s
def apply_default(noun):
    return noun + 's'

def plural_2(noun):
    """
    využívá pravidla nadefinovaná v n-tici rules, která řídí logiku
    1. Získej rozhodovací pravidlo (match rule).
    2. Došlo ke shodě? Tak volej aplikační pravidlo a vrať výsledek.
    3. Nedošlo ke shodě? Přejdi ke kroku 1.
    """
    for matches_rule, apply_rule in rules2:      #cyklus prochází prvky n-tice rules
        if matches_rule(noun):
            return apply_rule(noun)

# n-tice (tuple) s pravidly použita ve variantě 2
rules2 = (
    (match_sxz, apply_sxz),
    (match_h, apply_h),
    (match_y, apply_y),
    (match_default, apply_default)
    )

# varianta 3
def build_match_and_apply_functions(pattern, search, replace):
    """
    zobecňuje variantu 2, nemá pro každou variantu samostatnou fci, ale vytváří funkce dynamicky právě v této funkci
    """
    def matches_rule(word):
        return re.search(pattern, word)
    def apply_rule(word):
        return re.sub(search, replace, word)
    return (matches_rule, apply_rule)

patterns = \
    (
        ('[sxz]$',              '$', 'es'),
        ('[^aeioudgkprt]h$',    '$', 'es'),
        ('(qu|[^aeiou])y$',     'y$', 'ies'),
        ('$',                   '$', 's')
    )

rules3 = [build_match_and_apply_functions(pattern, search, replace) 
            for (pattern, search, replace) in patterns]

def plural_3(noun):
    """
    využívá pravidla nadefinovaná v n-tici rules, která řídí logiku
    1. Získej rozhodovací pravidlo (match rule).
    2. Došlo ke shodě? Tak volej aplikační pravidlo a vrať výsledek.
    3. Nedošlo ke shodě? Přejdi ke kroku 1.
    fce je shodná s prular_2
    """
    for matches_rule, apply_rule in rules3:      #cyklus prochází prvky n-tice rules
        if matches_rule(noun):
            return apply_rule(noun)

slova = seznam_slov()
for i in range(0,len(slova)):
    #print(f'{slova[i]} - {plural_1(slova[i])}')
    #print(f'{slova[i]} - {plural_2(slova[i])}')
    print(f'{slova[i]} - {plural_3(slova[i])}')

