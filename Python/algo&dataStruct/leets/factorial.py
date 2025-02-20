def factorial(data):

    if (data == 0):
        return 1
    return data * factorial(data-1)


print(factorial(4))