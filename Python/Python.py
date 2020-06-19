
# def Alph(word):
#     array1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
#               'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#     forbiden = []
#     letters = []
#     arr = []
#     for l in word:
#         arr.append(l)
#     for letter in array1:
#         forbiden.append(letter + array1[array1.index(letter) - 1])
#         if(array1.index(letter) < (len(array1) - 1)):
#             forbiden.append(letter + array1[array1.index(letter) + 1])
#     for single in word:
#         letters.append(single + arr[arr.index(single) + -1])
#         if(arr.index(single) < (len(arr) - 1)):
#             letters.append(single + arr[arr.index(single) + 1])
#     for double in letters:
#         if double in forbiden:
#             return ("Invalid: " + double)
#     return ("Valid: " + word)


# print(Alph("computer"))

# def DoubleSquare(B):
#     array = []
#     back = []
#     i = 0

#     def ifFunc(a, b, c):
#         if (len(back) == a):
#             num = int(back[b]) + int(back[c])
#             back.pop(b)
#             back.pop(b)
#             back.insert(b, str(num))
#     for d in str(B):
#         array.append(d)
#         d = int(d)
#         if(i == 0):
#             temp1 = d * d
#             for e in str(temp1):
#                 back.append(e)
#         else:
#             temp2 = int(array[0]) * int(array[1]) * 2
#             for e in str(temp2):
#                 back.append(e)
#             ifFunc(3, 0, 1)
#             ifFunc(4, 1, 2)
#             blast = d * d
#             for m in str(blast):
#                 back.append(m)
#             ifFunc(4, 1, 2)
#             ifFunc(5, 2, 3)
#             print(int("".join(back)))
#         i += 1


# DoubleSquare(12)

# array1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
#           'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# for a in array1:
#     for b in array1:
#         for c in array1:
#             print(a + b + c)
