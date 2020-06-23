def DoubleSquare(B):
    array, back, i = [], [], 0

    def ifFunc(a, b, c):
        if (len(back) == a):
            num = int(back[b]) + int(back[c])
            back.pop(b)
            back.pop(b)
            back.insert(b, str(num))
    for d in str(B):
        array.append(d)
        d = int(d)
        if(i == 0):
            temp1 = d * d
            for e in str(temp1):
                back.append(e)
        else:
            temp2 = int(array[0]) * int(array[1]) * 2
            for e in str(temp2):
                back.append(e)
            ifFunc(3, 0, 1)
            ifFunc(4, 1, 2)
            blast = d * d
            for m in str(blast):
                back.append(m)
            ifFunc(4, 1, 2)
            ifFunc(5, 2, 3)
            print(int("".join(back)))
        i += 1


DoubleSquare(12)
