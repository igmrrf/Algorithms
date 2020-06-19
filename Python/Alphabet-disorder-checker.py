
def Alph(word):
    array1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
              'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    forbiden = []
    letters = []
    arr = []
    for l in word:
        arr.append(l)
    for letter in array1:
        forbiden.append(letter + array1[array1.index(letter) - 1])
        if(array1.index(letter) < (len(array1) - 1)):
            forbiden.append(letter + array1[array1.index(letter) + 1])
    for single in word:
        letters.append(single + arr[arr.index(single) + -1])
        if(arr.index(single) < (len(arr) - 1)):
            letters.append(single + arr[arr.index(single) + 1])
    for double in letters:
        if double in forbiden:
            return ("Invalid: " + double)
    return ("Valid: " + word)


print(Alph("computer"))
