__author__ = 'Alicia'
y = 'Enter SS#: '
inputstring = 'Please enter a valid social security number of the form ###-##-#### including the dashes: '


def question(s):
    social = input(s).strip()
    try:
        AAA, GG, SSSS = social.split('-')
        area = int(AAA)
        group = int(GG)
        serial = int(SSSS)
        if len(AAA) == 3 and len(GG) == 2 and len(SSSS) == 4:
            if AAA == '078' and GG == '05' and SSSS == '1120':
                return None
            elif 1 <= area < 900 and area != 666:
                if 1 <= group <= 99:
                    if 1 <= serial <= 9999:
                        return AAA, GG, SSSS
                    else:
                        return None
                else:
                    return None
            else:
                return None
        else:
            return None
    except ValueError:
        return None


def SS(s):
    while True:
        x = question(s)
        if x is not None:
            return x
        else:
            print('That was an invalid social security number, please re-enter.\n')
            return SS(s)


print(SS(inputstring))
#print(SS(y))