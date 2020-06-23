def diagonal_diff():
    n = int(input("Enter size of Matrix (N x N): "))
    if (-100 <= n <= 100):
        matrix, cool = [], []
        a, b, j, c, d, sum_left, sum_right = n, n-1, n-1, 0, n+1, 0, 0
        while (a > 0):
            row = list(map(int, input("Enter values:").split()))
            if (len(row) < n or len(row) > n):
                print("Please input equivalent number of elemetns")
                return diagonal_diff()
            matrix.append(row)
            a -= 1
        for arr in matrix:
            for bush in arr:
                cool.append(bush)
        while (n > 0):
            n -= 1
            sum_left += cool[b]
            sum_right += cool[c]
            b += j
            c += d
        result = sum_right - sum_left
        boom = str(result)
        main = boom.split("-", 1)
        if (len(main) > 1):
            finals = main[1]
            return finals
        else:
            finals = main[0]
            return finals
    else:
        print("Please input number -100 <= n <= 100 ")


print(diagonal_diff())
