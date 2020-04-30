def readposint():
    x = input("please, fill in a postive integer: ")
    try:
        integer = int(x)
        if integer <= 0:
           raise ValueError
    except ValueError:
        print(x, " is not a postive integer")
    else:
        print("Correct!", x, " is a postive integer.")
readposint()