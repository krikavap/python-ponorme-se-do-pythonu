"""
rimska-cisla.py
"""
import re
"""
# regulární výraz - kompaktní  způsob zápisu, ? znamená nepovinný znak, ^ začátek řetězce, $ konec řetězce ( | ) výlučné vzorky oddělené |
#pattern = '^M?M?M?(CM|CD|D?C?C?C?)(XC|XL|L?X?X?X?)(IX|IV|V?I?I?I?)$'      

# druhý kompaktní způsob  se {m,n}, kde m je minimální počet a n maximální počet znaků M                                            
pattern = '^M{0,3}(CM|CD|D?C?C?C?)$'        
print('M',re.search(pattern, 'M'))
print('MM',re.search(pattern, 'MM'))
print('MMM',re.search(pattern, 'MMM'))
print('MMMM',re.search(pattern, 'MMMM'))
print("''", re.search(pattern, ''))
print('C',re.search(pattern, 'C'))
print('CC',re.search(pattern, 'CC'))
print('CCC',re.search(pattern, 'CCC'))
print('CCCC',re.search(pattern, 'CCCC'))
print('D',re.search(pattern, 'D'))
print('DC',re.search(pattern, 'DC'))
print('DCC',re.search(pattern, 'DCC'))
print('DCCC',re.search(pattern, 'DCCC'))
print('CM',re.search(pattern, 'CM'))
print('CD',re.search(pattern, 'CD'))
print('CCD',re.search(pattern, 'CCD'))
print('MCM',re.search(pattern, 'MCM'))
print('MD',re.search(pattern, 'MD'))
print('MMMCCC',re.search(pattern, 'MMMCCC'))
print('MCMC',re.search(pattern, 'MCMC'))
print('MCMXL',re.search(pattern, 'MCMXL'))
print('MCML',re.search(pattern, 'MCML'))
print('MCMLX',re.search(pattern, 'MCMLX'))
print('MCMLXXX',re.search(pattern, 'MCMLXXX'))
print('MCMLXXXX',re.search(pattern, 'MCMLXXXX'))
print('MDLV',re.search(pattern, 'MDLV'))
print('MMDCLXVI',re.search(pattern, 'MMDCLXVI'))
print('MMMDCCCLXXXVIII',re.search(pattern, 'MMMDCCCLXXXVIII'))
print('MMMIM',re.search(pattern, 'MMMIM'))
print('MMMCMXCIX',re.search(pattern, 'MMMCMXCIX'))
print('I',re.search(pattern, 'I'))

"""
# přehlednější výceslovný výraz, kde je možné i vkládat komentáře - lepší pro údržbu
pattern = '''
^                   # začátek řetězce
M{0,3}              # tisíce - 0 až 3 M
(CM|CD|D?C{0,3})    # stovky - 900 (CM), 400 (CD), 0-300 (0 až 3 C) nebo 500-800 (D následované 0 až 3 C)
(XC|XL|L?X{0,3})    # desítky - 90 (XC), 40 (XL), 0 - 30 (0 až 3X) nebo 50 - 80 (L následované 0 až 3 X)
(IX|IV|V?I{0,3})    # jednotky
$                   # konec řetězce
'''
print('M',re.search(pattern, 'M', re.VERBOSE))
print('MM',re.search(pattern, 'MM', re.VERBOSE))
print('MMM',re.search(pattern, 'MMM', re.VERBOSE))
print('MMMM',re.search(pattern, 'MMMM', re.VERBOSE))
print("''", re.search(pattern, '', re.VERBOSE))
print('C',re.search(pattern, 'C', re.VERBOSE))
print('CC',re.search(pattern, 'CC', re.VERBOSE))
print('CCC',re.search(pattern, 'CCC', re.VERBOSE))
print('CCCC',re.search(pattern, 'CCCC', re.VERBOSE))
print('D',re.search(pattern, 'D', re.VERBOSE))
print('DC',re.search(pattern, 'DC', re.VERBOSE))
print('DCC',re.search(pattern, 'DCC', re.VERBOSE))
print('DCCC',re.search(pattern, 'DCCC', re.VERBOSE))
print('CM',re.search(pattern, 'CM', re.VERBOSE))
print('CD',re.search(pattern, 'CD', re.VERBOSE))
print('CCD',re.search(pattern, 'CCD', re.VERBOSE))
print('MCM',re.search(pattern, 'MCM', re.VERBOSE))
print('MD',re.search(pattern, 'MD', re.VERBOSE))
print('MMMCCC',re.search(pattern, 'MMMCCC', re.VERBOSE))
print('MCMC',re.search(pattern, 'MCMC', re.VERBOSE))
print('MCMXL',re.search(pattern, 'MCMXL', re.VERBOSE))
print('MCML',re.search(pattern, 'MCML', re.VERBOSE))
print('MCMLX',re.search(pattern, 'MCMLX', re.VERBOSE))
print('MCMLXXX',re.search(pattern, 'MCMLXXX', re.VERBOSE))
print('MCMLXXXX',re.search(pattern, 'MCMLXXXX', re.VERBOSE))
print('MDLV',re.search(pattern, 'MDLV', re.VERBOSE))
print('MMDCLXVI',re.search(pattern, 'MMDCLXVI', re.VERBOSE))
print('MMMDCCCLXXXVIII',re.search(pattern, 'MMMDCCCLXXXVIII', re.VERBOSE))
print('MMMIM',re.search(pattern, 'MMMIM', re.VERBOSE))
print('MMMCMXCIX',re.search(pattern, 'MMMCMXCIX', re.VERBOSE))
print('I',re.search(pattern, 'I', re.VERBOSE))