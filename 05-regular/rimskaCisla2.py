"""
rimska-cisla2.py
upravená verze po čísla 0 - 4999
"""
import re

class OutOfRangeError(ValueError): pass
class NotIntegerError(ValueError): pass
class InvalidRomanNumeralError(ValueError): pass

roman_numeral_pattern = re.compile('''
^                   # začátek řetězce
M{0,4}              # tisíce - 0 až 4 M
(CM|CD|D?C{0,3})    # stovky - 900 (CM), 400 (CD), 0-300 (0 až 3 C) nebo 500-800 (D následované 0 až 3 C)
(XC|XL|L?X{0,3})    # desítky - 90 (XC), 40 (XL), 0 - 30 (0 až 3X) nebo 50 - 80 (L následované 0 až 3 X)
(IX|IV|V?I{0,3})    # jednotky
$                   # konec řetězce
''', re.VERBOSE)

roman_numeral_map = (
    ('M', 1000),
    ('CM', 900),
    ('D', 500),
    ('CD', 400),
    ('C', 100),
    ('XC', 90),
    ('L', 50),
    ('XL', 40),
    ('X', 10),
    ('IX', 9),
    ('V', 5),
    ('IV', 4),
    ('I', 1) 
)

def to_roman(cislo):
    '''convert integer to Roman numeral'''
    if isinstance(cislo, int):
        if 0 < cislo < 5000:
            result = ''
            for numeral, integer in roman_numeral_map:
                while cislo >= integer:
                    result += numeral       #result = result + numeral
                    cislo -= integer        # cislo = cislo - integer
            return result
        else:
            raise OutOfRangeError('number out of range (must be 1..3999)')
    raise NotIntegerError('non-integers can not be converted')

def from_roman(cislo):
    '''convert Roman numeral to integer'''
    if not cislo:
        raise InvalidRomanNumeralError(f'Input can not be blank')
    if not roman_numeral_pattern.search(cislo):
        raise InvalidRomanNumeralError(f'Invalid Roman numeral: {cislo}')

    result = 0
    index = 0
    for roman, integer in roman_numeral_map:
        while cislo[index:index + len(roman)] == roman:
            result += integer
            index += len(roman)
            # print('found', roman, 'of length', len(roman), ', adding', integer)
    return result




#from_roman('MMMMM')    
