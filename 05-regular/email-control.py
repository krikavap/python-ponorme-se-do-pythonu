# coding=utf8
# the above tag defines encoding for this document and is for Python 2.x compatibility

import re

regex = r"^.*@.+\.cz$"

test_str = ("jan.tleskac@letadlo.cz\n"
	"vontove.stinadla.cz\n"
	"kocici.pracka@.cz\n"
	"@vkleci.sk\n"
	"rychlonozka@rychle.sipy.cz\n"
	"mirek.dusin3@gmail.com\n"
	"cervenacek12@centrum.cz\n"
	"bidlo@fbi.com\n"
	"jindra7@centrum.cz\n"
	"siroko@hluboko.co.uk\n"
	"maznak@loupeznik.cz\n"
	"tam@tam.cz")

matches = re.finditer(regex, test_str, re.MULTILINE)

for matchNum, match in enumerate(matches, start=1):
    
    print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
    
    for groupNum in range(0, len(match.groups())):
        groupNum = groupNum + 1
        
        print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))

# Note: for Python 2.7 compatibility, use ur"" to prefix the regex and u"" to prefix the test string and substitution.


# coding=utf8
# the above tag defines encoding for this document and is for Python 2.x compatibility

import re

regex = r"^(\D*)\|\D*\|\d*\|\D*(\d*,\d*)$"

test_str = ("Austrálie|dolar|1|AUD|17,744\n"
	"Brazílie|real|1|BRL|10,276\n"
	"Bulharsko|lev|1|BGN|12,319\n"
	"Čína|renminbi|1|CNY|2,559\n"
	"Dánsko|koruna|1|DKK|3,231\n"
	"EMU|euro|1|EUR|24,095\n"
	"Hongkong|dolar|1|HKD|2,138\n"
	"Indie|rupie|100|INR|37,047\n"
	"Izrael|šekel|1|ILS|4,804\n"
	"Jihoafrická rep.|rand|1|ZAR|2,458\n"
	"Kanada|dolar|1|CAD|17,243\n"
	"Maďarsko|forint|100|HUF|9,096\n"
	"Polsko|zlotý|1|PLN|6,096\n"
	"Rusko|rubl|100|RUB|59,768\n"
	"USA|dolar|1|USD|16,616\n"
	"Velká Británie|libra|1|GBP|27,262")

subst = "\\1: \\2"

# You can manually specify the number of replacements by changing the 4th argument
result = re.sub(regex, subst, test_str, 0, re.MULTILINE)

if result:
    print (result)

# Note: for Python 2.7 compatibility, use ur"" to prefix the regex and u"" to prefix the test string and substitution.