import re

def roman_digits_to_int(number):
    if number in ["PREMIÈRE", "PREMIER","première","premier"]:
        return 1
    l = "I,II,III,IV,V,VI,VII,VIII,IX,X,XI,XII,XIII,XIV,XV".split(',')
    try:
        return l.index(number) + 1
    except:
        return "PREMIER,SECOND,TROISIÈME,QUATRIÈME,CINQUIÈME".split(',').index(number) + 1

def remove_brackets(string):
    return re.sub("\[\d{1,3}\]", "", string)

def remove_verse_number(string):
    return re.sub("^\d*", "", string)

def sanitize(string):
    return remove_verse_number(remove_brackets(string)).strip()