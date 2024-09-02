import math

def calcNFactorial(n):
    if validInput(n, 0, 0):
        n = int(n)
        nFactorial = 1
        for ii in range(n, 1, -1):
            nFactorial = nFactorial * ii
        return nFactorial

def calcNFactorialRecursive(n):
    if validInput(n, 0, 0):
        n = int(n)
        factorial = 1
        if n == 0:
            factorial = 1
        else:
            factorial = n * calcNFactorialRecursive(n-1)
        return factorial

def fibIterative(n):
    if validInput(n, 0, 0):
        n = int(n)
        fibVal = 0
        currVal = 1
        lastVal = 0
        if n == 0:
            fibVal = 0
        elif n == 1:
            fibVal = 1
        else:
            for ii in range(2, n+1):
                fibVal = currVal + lastVal
                lastVal = currVal
                currVal = fibVal
        return fibVal

def fibRecursive(n):
    if validInput(n, 0, 0):
        n = int(n)
        fibval = 0
        if n == 0:
            fibVal = 0
        elif n == 1:
            fibVal = 1
        else:
            fibVal = fibRecursive(n-1) + fibRecursive(n-2)
        return fibVal

def greatestCommonDenominator(n1, n2):
    if validInput(n1, 1, 0) and validInput(n2, 1, 0):
        n1 = int(n1)
        n2 = int(n2)
        highFac = 1
        ii = 2
        while ii <= n1 and highFac == 1:
            if n1 % ii == 0 and n2 % ii == 0:
                highFac = ii * greatestCommonDenominator(n1/ii, n2/ii)
            ii = ii + 1
        return highFac

def numberConversions(n, base):
    if validInput(n, 0, 0) and validInput(base, 2, 16):
        n = int(n)
        base = int(base)
        ii = 1
        output = '0'
        character = '0'
        while n >= (base ** ii):
            ii = ii + 1
        character = math.floor(n /((base ** (ii - 1))))
        if int(character) >= 10:
            character = chr(int(character) + 87)
        num0 = 0
        while (n % (base ** (ii - 1))) < (base ** (ii - num0 - 2)) and n / (base ** num0) > base:
            num0 = num0 + 1
            character = str(character) + '0'
        if ii > 1:
            output = str(character) + numberConversions((n % (base ** (ii - 1))), base)
        else:
            output = str(character)
        return output


def towerOfHanoi(n , P1, P2, P3, level): 
    n = int(n)
    level = level + 1        
    if n == 1:
        indents(level)
        print("Recursion Level:", level)
        indents(level)
        print("Disc 1 goes from the",P1,"pole to the",P2,"pole")
        print("")
    else:
        towerOfHanoi(n-1, P1, P3, P2, level)
        indents(level)
        print("Recursion Level:", level)
        indents(level)
        print("Disc",n,"goes from the", P1, "pole to the",P2,"pole")
        print("")
        towerOfHanoi(n-1, P3, P2, P1, level)

def indents(n):
    ii = 1
    while ii < n:
        print("   ", end='')
        ii = ii + 1


def validInput(n, lower, upper):
    output = False
    try:
        if int(n) < 0:
            raise ValueError
        elif int(n) < lower and lower != 0:
            raise ValueError
        elif int(n) > upper and upper != 0:
            raise ValueError
        else:
            output = True
    except ValueError:
        print("Incorrect Import")
    return output
    
print(numberConversions(823562, 16))