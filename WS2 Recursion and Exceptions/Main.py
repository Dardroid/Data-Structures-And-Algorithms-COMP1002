import Calc

print("1 - Factorial Iterative")
print("2 - Factorial Recursive")
print("3 - Fibonacci Iterative")
print("4 - Fibonacci Recursive")
print("5 - Greatest Common Denominator Recursive")
print("6 - Number Conversions Recursive")
print("7 - Towers of Hanoi")

validInp = False
while validInp == False:
    validInp = True
    inp = str(input("Selection: "))
    if inp == '1':
        n = input("Number: ")
        print(Calc.calcNFactorial(n))
    elif inp == '2':
        n = input("Number: ")
        print(Calc.calcNFactorialRecursive(n))
    elif inp == '3':
        n = input("Number: ")
        print(Calc.fibIterative(n))
    elif inp == '4':
        n = input("Number: ")
        print(Calc.fibRecursive(n))
    elif inp == '5':
        n1 = input("Number One: ")
        n2 = input("Number Two: ")
        print(Calc.greatestCommonDenominator(n1, n2))
    elif inp == '6':
        n = input("Number: ")
        base = input("Base: ")
        print(Calc.numberConversions(n, base))
    elif inp =='7':
        n = input("Number: ")
        source = input("Source (L, M, R): ")
        destination = input("Destination (L, M, R):")
        if (source == "L" or source == "M" or source == "R") and (destination == "L" or destination == "M" or destination == "R") and (source != destination):
            if (source == "L" and destination == "R") or (source == "R" and destination == "L"):
                other = "M"
            elif (source == "M" and destination == "R") or (source == "R" and destination == "M"):
                other = "L"
            else:
                other = "R"
            Calc.towerOfHanoi(n , source, destination, other, 0)
        else:
            print("Invalid input")
    else:
        validInp = False