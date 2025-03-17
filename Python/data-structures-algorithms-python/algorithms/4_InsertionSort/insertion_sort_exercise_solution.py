def place_to_insert(array, key):
    index = 0
    for i in array:
        if i > key:
            break
        else:
            index += 1
    return index


def insert_to_sorted(array, key):
    index = place_to_insert(array, key)
    return array[0:index] + [key] + array[index:]


if __name__ == "__main__":
    # input array
    # array = [2, 1, 5, 7, 2, 0, 5]

    # stream
    stream = []

    # maintain count
    count = 0

    while True:
        # take in input
        i = int(input())
        # increase count
        count += 1
        # update stream
        stream = insert_to_sorted(stream, i)
        if count % 2 == 1:
            print(f"Median of {stream} : {stream[(count)//2]}")
        else:
            i1 = count // 2
            i2 = (count // 2) - 1
            print(f"Median of {stream} : {(stream[i1] + stream[i2])/2}")
