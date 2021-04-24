def isNumber():
    try:
        return int(inputString)
    except ValueError as _:
        print("Bitte gib eine Zahl an.")
        return 0


inputString = input("Zahl: ")
number = isNumber()

if number != 0:
    isPrim = True

    if isPrim:
        print("{} ist eine Primzahl.".format(number))
    else:
        print("{} ist keine Primzahl.".format(number))
