__author__ = 'Alicia'
y = 'Please enter a valid social security number of the form ###-##-####: '


def question(s):
    social = input(s).strip()
    try:
        AAA, GG, SSSS = social.split('-')
        e, v, i, l = SSSS[0:4]
        area = int(AAA)
        group = int(GG)
        serial = int(SSSS)
        if len(AAA) == 3 and len(GG) == 2 and len(SSSS) == 4:
            if AAA == '078' and GG == '05' and SSSS == '1120':
                return None
            elif (e == '6' and v == '6' and i == '6') or (v == '6' and i == '6' and l == '6'):
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

print(SS(y))

