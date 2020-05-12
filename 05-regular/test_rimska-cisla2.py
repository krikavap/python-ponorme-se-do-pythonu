'''
test_rimska-cisla2.py
''' 
import pytest
from rimskaCisla2 import to_roman
from rimskaCisla2 import from_roman, InvalidRomanNumeralError

test_data = [ 
    (1, 'I'),
    (2, 'II'),
    (3, 'III'),
    (4, 'IV'),
    (5, 'V'),
    (6, 'VI'),
    (7, 'VII'),
    (8, 'VIII'),
    (9, 'IX'),
    (10, 'X'),
    (50, 'L'),
    (100, 'C'),
    (500, 'D'),
    (1000, 'M'),
    (31, 'XXXI'),
    (148, 'CXLVIII'),
    (294, 'CCXCIV'),
    (312, 'CCCXII'),
    (421, 'CDXXI'),
    (528, 'DXXVIII'),
    (621, 'DCXXI'),
    (782, 'DCCLXXXII'),
    (870, 'DCCCLXX'),
    (941, 'CMXLI'),
    (1043, 'MXLIII'),
    (1110, 'MCX'),
    (1226, 'MCCXXVI'),
    (1301, 'MCCCI'),
    (1485, 'MCDLXXXV'),
    (1509, 'MDIX'),
    (1607, 'MDCVII'),
    (1754, 'MDCCLIV'),
    (1832, 'MDCCCXXXII'),
    (1993, 'MCMXCIII'),
    (2074, 'MMLXXIV'),
    (2152, 'MMCLII'),
    (2212, 'MMCCXII'),
    (2343, 'MMCCCXLIII'),
    (2499, 'MMCDXCIX'),
    (2574, 'MMDLXXIV'),
    (2646, 'MMDCXLVI'),
    (2723, 'MMDCCXXIII'),
    (2892, 'MMDCCCXCII'),
    (2975, 'MMCMLXXV'),
    (3051, 'MMMLI'),
    (3185, 'MMMCLXXXV'),
    (3250, 'MMMCCL'),
    (3313, 'MMMCCCXIII'),
    (3408, 'MMMCDVIII'),
    (3501, 'MMMDI'),
    (3610, 'MMMDCX'),
    (3743, 'MMMDCCXLIII'),
    (3844, 'MMMDCCCXLIV'),
    (3888, 'MMMDCCCLXXXVIII'),
    (3940, 'MMMCMXL'),
    (3999, 'MMMCMXCIX'),
    (4000, 'MMMM'),
    (4500, 'MMMMD'),
    (4888, 'MMMMDCCCLXXXVIII'),
    (4999, 'MMMMCMXCIX'), 
    pytest.param(99,'IC', marks=pytest.mark.xfail(reason = 'IC není platné římské číslo')), # fce by měl vracet chybu - toto číslo neexistuje jako římské číslo
    pytest.param(5000, 'MMMMM', marks=pytest.mark.xfail(reason = '5000 je mimo intervel platných římských čísel 1-3999')), # fce by měl vracet chybu - toto číslo neexistuje jako římské číslo
    pytest.param(10.25, 'X', marks=pytest.mark.xfail(reason = '10.25 není celé číslo')), # fce by měl vracet chybu - toto číslo neexistuje jako římské číslo
    pytest.param(-10, 'X', marks=pytest.mark.xfail(reason = '-10 je mimo intervel platných římských čísel 1-3999')), # fce by měl vracet chybu - toto číslo neexistuje jako římské číslo
    pytest.param('deset', 'X', marks=pytest.mark.xfail(reason = '"deset" není int')), # fce by měl vracet chybu - text není možné převést na římské číslo
    pytest.param(9000, 'MMMMMMMMM', marks=pytest.mark.xfail(reason = '9000 je mimo intervel platných římských čísel 1-3999')) # fce by měl vracet chybu - toto číslo neexistuje jako římské číslo
]

def test_roundtrip():
    for integer in range(1,5000):
        roman = to_roman(integer)
        result = from_roman(roman)
        assert integer == result

@pytest.mark.parametrize ("integer, roman",test_data)
def test_to_roman_known_values(integer, roman):
    assert to_roman(integer) == roman


@pytest.mark.parametrize ("integer, roman",test_data)
def test_from_roman_known_values(integer, roman):
    'testuje fci from_roman'
    assert from_roman(roman) == integer

def test_too_many_repeated_numerals():
    '''from_roman should fail with too many repeated numerals'''
    for s in ('MMMMM', 'DD', 'CCCC', 'LL', 'XXXX', 'VV', 'IIII'):
        with pytest.raises(InvalidRomanNumeralError):
            from_roman(s)

def test_repeated_pairs():
    '''from_roman should fail with repeated pairs of numerals'''
    for s in ('CMCM', 'CDCD', 'XCXC', 'XLXL', 'IXIX', 'IVIV'):
        #raise InvalidRomanNumeralError('repeated pairs of numerals', s)
        with pytest.raises(InvalidRomanNumeralError):
            from_roman(s)

def test_malformed_antecedents():
    '''from_roman should fail with malformed antecedents'''
    for s in ('IIMXCC', 'VX', 'DCM', 'CMM', 'IXIV', 'MCMC', 'XCX', 'IVI', 'LM', 'LD', 'LC'):
        #raise InvalidRomanNumeralError('fail with malformed antecedents', s)
        with pytest.raises(InvalidRomanNumeralError):
            from_roman(s)

def test_Blank():
    '''from_roman should fail with blank string'''
    s = ''
    with pytest.raises(InvalidRomanNumeralError):
            from_roman(s)