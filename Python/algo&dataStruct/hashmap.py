class HashTable:
    def __init__(self):
        self.Max = 10
        self.arr = [None for i in range(self.Max)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.Max

    def __setitem__(self, key, value):
        h = self.get_hash(key)
        if self.arr[h] is None:
            self.arr[h] = (key, value)
        else:
            new_h = self.find_slot(key, h)
            self.arr[new_h] = (key, value)
        print(self.arr)

    def get_prob_range(self, index):
        return [*range(index, len(self.arr))] + [*range(0, index)]

    def find_slot(self, key, index):
        prob_range = self.get_prob_range(index)
        for prob_index in prob_range:
            if self.arr[prob_index] is None:
                return prob_index
            elif self.arr[prob_index][0] == key:
                return prob_index
        raise Exception("hashmap full")

    def __getitem__(self, key):
        h = self.get_hash(key)
        if self.arr[h] is None:
            return

        prob_range = self.get_prob_range(h)
        for prob_index in prob_range:
            element = self.arr[prob_index]
            if element is None:
                return
            elif element[0] == key:
                return element[1]

    def __delitem__(self, key):
        h = self.get_hash(key)
        prob_range = self.get_prob_range(h)
        for prob_index in prob_range:
            if self.arr[prob_index] is None:
                return  # Item not found
            elif self.arr[prob_index][0] == key:
                self.arr[prob_index] = None

    #
    # def __setitem__(self, key, value):
    #     h = self.get_hash(key)
    #     found = False
    #     for idx, element in enumerate(self.arr[h]):
    #         if len(element) == 2 and element[0] == key:
    #             self.arr[h][idx] = (key, value)
    #             found = True
    #             break
    #
    #     if not found:
    #         self.arr[h].append((key, value))
    #
    # def __getitem__(self, key):
    #     h = self.get_hash(key)
    #
    #     for element in self.arr[h]:
    #         if len(element) == 2 and element[0] == key:
    #             return element[1]
    #
    # def __delitem__(self, key):
    #     h = self.get_hash(key)
    #
    #     for idx, element in enumerate(self.arr[h]):
    #         if element[0] == key:
    #             last_value = self.arr[h][-1]
    #             if last_value[0] == key:
    #                 self.arr[h].pop()
    #             else:
    #                 self.arr[h][idx] = last_value
    #                 self.arr[h][-1] = element
    #                 self.arr[h].pop()
    #             break


map = HashTable()
map["march 6"] = 9
map["march 8"] = 13
map["march 6"] = 18
map["march 17"] = 19
map["march 9"] = 12
map["march 12"] = 10

print(map["march 6"])
print(map["march 17"])
print(map["march 8"])
print(map["march 9"])
print(map["march 12"])
print(map.arr)
# del map["march 17"]
print(map.arr)
