# EX5: R2D2000 Brain.
result = ''
booly = True
count_for_fun = 0

if booly * 7:
    booly = booly != booly # now booly is false
    if booly or True != booly:
        if True + (booly or False) - booly:
            if True * 2 - booly * 3:
                booly = booly <= booly # booly true
                if booly and booly != 1 or booly - booly:
                    result += 'R2D1000 '
                    booly = booly != booly
                    count_for_fun -= 1
                elif booly and booly == 1 or booly - booly:
                    result += 'R2D2000 ' # booly true
                    count_for_fun += 1 # = 1
                if 3 ** 2 / 10 ** 2 * -5 // (1 / 100) % 2 == 0:
                    count_for_fun += 1
            if booly == booly and booly == booly: # need it to be true
                result += 'is '
                booly = booly <= booly
                count_for_fun += 1
            booly = booly != booly # booly false
        if booly ** True != True ** booly:# need it to be true
            if booly or True != booly: # need it to be true
                if booly or ((booly * 0) == booly): # need it to be true
                    if 0 or (True == booly): #need it to be false
                        if booly == True + booly or booly:
                            if booly > (booly - 1) and booly < 1:
                                count_for_fun += 1
                        else:
                            count_for_fun += 1
                    else: # need this
                        result += 'ALL '
                        count_for_fun += 1
                if 3 ** 3 / 10 ** 2 * 9 // (1 / 100) % 2 < 0: # need it to be false
                    result += 'far from '
                    count_for_fun -= 1
                elif 1 + booly and (-2 + booly or booly > 1):
                    result += 'GOOD! '
                    count_for_fun += 1
            else:
                count_for_fun += 1
        elif booly and -1 + booly ** 3 or booly % 2 != 1:
            count_for_fun += 1
if (5 % 2 < 3 / 6) + 1: # need it to be true, here booly false
    if count_for_fun != booly: # need it to be true
        if booly == 0:
            if 6 / 2 * 1 + 2:
                if 3 ** 3 / 10 ** 2 * 5 + 9 // (1 / 100) % 2 > 0: # need it to be true
                    result += 'Ready '
                    count_for_fun += 1
        else:
            if booly or booly <= booly and booly < 1:
                if booly - booly ** booly < 1:
                    if 3 ** 2 / 10 ** 2 * -5 // ((1 and False + True / 100) % 2) != 0:
                        result += 'I '
                        count_for_fun -= 1
if booly == booly - booly:
    pass
if 4 ** 3 / 10 ** 3 * 4 // (1 / 1000) % 2 >= 0: # need it to be true, booly false
    if booly == 0:
        result += 'to '
        count_for_fun += 1
    elif booly or booly <= booly and booly < 1:
        if booly > 1 / count_for_fun:
            result += 'will never '
            count_for_fun -= 1
        else:
            count_for_fun += 1
    if 4 ** 3 / 10 * 3 * count_for_fun - 1 * 16 // (1 / 1000) % 4 != 0: # need it to be true
        result += 'work! :)'
        count_for_fun += 1
    elif 4 ** 3 >= -2 * count_for_fun or 9 * 10 ** 3 * 16 < (1 / 2 and 9000) % 4 != 0:
        result += 'work! :('
        count_for_fun += 1

print("Result:", result)