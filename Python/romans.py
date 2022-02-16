import time


def getRomans(num):
    time1 = time.time()
    roman = []
    if(num / 1000 >= 1):
        num -= 1000
        roman.extend("M")
        roman.extend(getRomans(num))

    elif num % 900 < 900 and num / 900 >= 1:
        num -= 900
        roman.extend("CM")
        roman.extend(getRomans(num))

    elif num / 500 >= 1:
        num -= 500
        roman.extend("D")
        roman.extend(getRomans(num))

    elif num % 400 < 400 and num / 400 >= 1:
        num -= 400
        roman.extend("CD")
        roman.extend(getRomans(num))

    elif num / 100 >= 1:
        num -= 100
        roman.extend("C")
        roman.extend(getRomans(num))

    elif num % 90 < 90 and num / 90 >= 1:
        num -= 90
        roman.extend("XC"+getRomans(num))

    elif num / 50 >= 1:
        num -= 50
        roman.extend("L"+getRomans(num))

    elif num % 40 < 40 and num / 40 >= 1:
        num -= 40
        roman.extend("XL")
        roman.extend(getRomans(num))

    elif num / 10 >= 1:
        num -= 10
        roman.extend("X")
        roman.extend(getRomans(num))

    elif num % 9 < 9 and num / 9 >= 1:
        num -= 9
        roman.extend("IX")
        roman.extend(getRomans(num))

    elif num / 5 >= 1:
        num -= 5
        roman.extend("V")
        roman.extend(getRomans(num))

    elif num % 4 < 4 and num / 4 >= 1:
        num -= 4
        roman.extend("IV"+getRomans(num))

    elif num / 1 >= 1:
        num -= 1
        roman.extend("I")

    time2 = time.time()

    print(time2-time1)
    return "".join(roman)


random = [1, 3999, 608, 543]

for value in odd:
    print(value)
    print(getRomans(value))
