def print_repeatedly():
    # * Printing a string multiple Times
    my_string = input("Enter String to be Printed: ")
    n = int(input("How many times do you want to repeat: "))
    my_string += "\n"
    print(my_string * n)


print_repeatedly()
