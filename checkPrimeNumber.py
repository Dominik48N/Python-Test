def isNumber():
    try:
        return int(inputString)
    except ValueError as _:
        print("Bitte gib eine Zahl an.")
        return None


inputString = input("Zahl: ")
number = isNumber()

if number is not None:
    isPrim = True

    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                print("{} ist keine Primzahl!".format(number))
                break
            else:
                print("{} ist eine Primzahl.".format(number))
                break
    else:
        print("{} ist keine Primzahl.".format(number))
