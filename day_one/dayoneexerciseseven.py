def evenorodd():

    num = input(("Write an integer: "))
    if((num%2) == 0):
        print("The integer is even.")
    elif((num%2) == 1):
        print("The integer is odd.")
    else:
        print("An integer wasn't entered.")

evenorodd()