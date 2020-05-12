"""
mnozneCisloAj_iterator.py
kap.7

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
    
class LazyRules:
    rules_filename = 'c:/Users/krikavap/Documents/GitHub/python-ponorme-se-do-pythonu/05-regular/mnozneCisloAj-pravidla.txt'

    def __init__(self):
        with open(self.rules_filename, encoding = 'utf-8') as self.pattern_file:
            obsah = self.pattern_file.read() # načtení celého souboru a uzavření
            
        obsah_list = obsah.split(sep = '\n')    # načte obsah souboru do seznamu, kde co řádka souboru je jeden prvek pole
        self.pravidla=[]
        for i in range(0, len(obsah_list)):
            l = obsah_list[i]
            p = l.split(sep = ' ')
            self.pravidla.append(p)
            
        print(self.pravidla)
      
    def __iter__(self):
        self.pravidla_index = 0
        return self

    def __next__(self):
        self.pravidla_index += 1
        if len(self.pravidla) >= self.pravidla_index:
            return self.pravidla[self.pravidla_index - 1]
        pattern, search, replace = self.pravidla(self.pravidla_index)
        funcs = build_match_and_apply_functions(pattern, search,replace)
        return funcs

def build_match_and_apply_functions(pattern, search, replace):
    """
    zobecňuje variantu 2, nemá pro každou variantu samostatnou fci, ale vytváří funkce dynamicky právě v této funkci
    """
    def matches_rule(word):
        return re.search(pattern, word)
    def apply_rule(word):
        return re.sub(search, replace, word)
    return (matches_rule, apply_rule)

def plural(noun):
    for matches_rule, apply_rule in rules:
        if matches_rule(noun):
            return apply_rule(noun)



rules = LazyRules()
slova = seznam_slov()
for i in range(0,len(slova)):
    #print(f'{slova[i]} - {plural_1(slova[i])}')
    #print(f'{slova[i]} - {plural_2(slova[i])}')
    print(f'{slova[i]} - {plural(slova[i])}')