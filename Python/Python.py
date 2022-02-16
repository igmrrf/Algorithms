# PYTHON Tips and Tricks for Better Code

class Python:
    def multi_multi(self):
        # * Multiple Assignment for Multiple Variables
        a, b, c, d = 1, 2, 3, 4
        print(a, b, c, d)  # 1,2,3,4

    def multi_single(self):
        # * Multiple Assignment for a Single Variable
        e = 5, 6, 7, 8
        print(e)  # (5,6,7,8)

    def multi_mixed_multi(self):
        # * Multiple Assignment for Mixed Multi Variables
        f, *g = 10, 11, 12
        print(f)  # 10
        print(g)  # [11,12]

    def single_multi(self):
        # * Single Assignment for Multiple Variables
        h = i = i = j = 13

    def swap_using_temp(self, a, b):
        # * Swapping Two Variables using a temp value
        k, l = a, b
        print(k, l)
        temp = k
        k = l
        l = temp
        print(k, l)

    def Swap_no_temp(self, a, b):
        # * Swappint Two Variables without using a temp value
        m, n = 16, 17
        print(m, n)
        m = m + n
        n = m - n
        m = m - n
        print(m, n)

    def Swap_optimal(self):
        # * Swappint Two Variables: Optimal Python Solution
        o, p = 18, 19
        print(o, p)
        o, p = p, o
        print(o, p)

    def Split_Letter(self, string):
        # * Splitting letter spaces in a Line
        school, my_list = string, []
        for word in school:
            my_list.append(word)
        print(my_list)

    def Split_Word(self, string):
        # * Splitting Word in a Line using Iterations
        start, end, my_list = 0, 0, []
        for x in string:
            end = end + 1
            if (x == ' '):
                my_list.append(string[start:end-1])
                start = end
            if (x == string[len(string) - 1]):
                my_list.append(string[start:end])
        print(my_list)

    def Split_Word_Using_Split(self, string):
        # * Splitting Word in a Line using Split Functions
        my_list = string.split(' ')
        print(my_list)

    def Join_List(self, your_list):
        joined = ' '.join(list)
        print(joined)

    def Most_Frequent(self, your_list):
        most_frequent = max(set(your_list), key=your_list.count)
        print(most_frequent)

    def Occurence(self, your_list):
        my_list = []
        for x in your_list:
            frequency = max(set(your_list), key=your_list.count)
            my_list.append(frequency)


print(Python.Reverse_String("I am good"))
