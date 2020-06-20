def convert_and_check(x):
    # Converting the number to binary
    bit, max_gap, current_gap = [], 0, 0
    while x:
        bit.append(x % 2)
        x >>= 1
        # * The Converted value is reversed by bit[::-1] to give the value in binary
    for i in bit[::-1]:
        # incrementing the gap and assigning a max gap
        current_gap = current_gap + 1 if (i < 1) else 0
        mmax_gapax = current_gap if (max_gap < current_gap) else max_gap
    return max_gap


print(convert_and_check(1041))

# A binary gap within a positive integer N is any maximal sequence of consecutive zeros that is surrounded by ones at both ends in the binary representation of N.

# For example, number 9 has binary representation 1001 and contains a binary gap of length 2. The number 529 has binary representation 1000010001 and contains two binary gaps: one of length 4 and one of length 3. The number 20 has binary representation 10100 and contains one binary gap of length 1. The number 15 has binary representation 1111 and has no binary gaps. The number 32 has binary representation 100000 and has no binary gaps.

# Write a function:

# function solution(N)

# that, given a positive integer N, returns the length of its longest binary gap. The function should return 0 if N doesn't contain a binary gap.

# For example, given N = 1041 the function should return 5, because N has binary representation 10000010001 and so its longest binary gap is of length 5. Given N = 32 the function should return 0, because N has binary representation '100000' and thus no binary gaps.

# Write an efficient algorithm for the following assumptions:

# N is an integer within the range[1..2, 147, 483, 647].
