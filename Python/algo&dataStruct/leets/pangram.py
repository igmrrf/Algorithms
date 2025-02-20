import string


def is_Pangram(s):
    s = s.lower()
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l','m', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    existingLetters = 0
    for letter in letters:
        if letter in s:
            existingLetters +=1
            print(existingLetters)
    if(existingLetters == 26):
        return True
    return False
    # return set(string.ascii_letters).issubset(s.lower())


print(is_Pangram("the brown fox jumped over the lazy dog"))
