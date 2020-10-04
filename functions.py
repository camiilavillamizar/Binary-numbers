import math

def menu():
    print("Seleccione 1 para convertir numeros enteros a numeros binarios")
    print("Seleccione 2 para convertir numeros binarios a numeros enteros")
    print("Seleccione 3 para convertir numeros flotantes a binarios")
    print("Seleccione 4 para convertir numeros binarios a flotantes")

"""
This function converts a int number to a binary
"""
def binaryProcess(num): 
    binary = []
    while (num >= 2):
        binary.append(num%2)
        num = int(num/2)
    binary.append(num)

    binary.reverse()
    return binary

"""
This function prints a binary number
"""
def printBinary(binary):

    for i in binary:
        print(i, end='')
    print('\n')

"""
This function swaps 0 for 1 and 1 for 0
"""
def swap(binary):
    for i in range (len(binary)):
        if binary[i] == 0:
            binary[i] = 1
        else:
            binary[i] = 0

    return binary

"""
This function adds 1 to a binary number 
"""
def add1(binary):

    binary.reverse()

    for i in range (len(binary)):
        if (binary[i] == 0):
            binary[i] = 1
            break
        elif (binary[i] == 1):
            binary[i] = 0
        elif (i == len(binary) - 1):
            binary.append(1)
    binary.reverse()
    return binary

"""
This function makes all the process to convert a negative number to binary
"""
def negativeIntToBinary(num):
    return fillBits(add1(swap(binaryProcess(num))), 8, True)

def positiveIntToBinary(num):
    return fillBits(binaryProcess(num), 8, False)

"""
This function makes the process to fill the bits 
"""
def fillBits(binary, bits, negative):
    binary.reverse()

    if (len(binary) >= bits):
        bits = len(binary)
    
    for i in range (bits):
        if (i >= len(binary)):
            if negative == False:
                binary.append(0)
            if negative == True:
                binary.append(1)
    binary.reverse()
    return binary

"""
Validates the string (only 0 and 1)
"""
def validate (num):

    for i in num: 
        if i == '0' or i == '1' or i == 0 or i ==1:
            pass
        else:
            return False

    return True
    
def positiveBinaryToDecimal(binary):
    decimal = 0
    binary.reverse()
    for i in range (len(binary)):
        decimal += int(binary[i]) * 2**i
    return decimal

def negativeBinaryToDecimal(num):
    return positiveBinaryToDecimal(add1(swap(num)))

def floatingToBinary(floating, presition):
    binary_float = []
    float_numbers = []

    if presition == 'single':
        presition_number = 23
    elif presition == 'double':
        presition_number = 52

    for i in range (presition_number):
        floating *= 2
        for j in float_numbers:
            if j == floating:
                periodic_binary = True

        float_numbers.append(floating)
        binary_float.append(int(floating))

        if floating == 1:
            periodic_binary = False
            return binary_float, periodic_binary

        floating -= int(floating)
        floating = round(floating, 10)

    return binary_float, periodic_binary

def binaryToString(binary):

    string = ''
    for i in binary:
        string += str(i)

    return string

def normalizedNotation(binary_integer, binary_floating):

    exponent = len(binary_integer) - 1

    binary_integer.insert(1, '.')
    strint = binaryToString(binary_integer)
    strfloat = binaryToString(binary_floating)

    binary_float_number = strint +  strfloat

    return binary_float_number, exponent

def floatSign(num):

    if num > 0:
        return 0
    if num < 0:
        return 1

def fillBits2 (mantisa, bits):
    for i in range (bits):
        if i >= len(mantisa):
            mantisa.append(0)

    while len(mantisa) > bits:
        mantisa.pop(-1)
        
    return mantisa

def normalizedMantisa(number, bits):

    mantisa = []
    num = [char for char in number]
    for i in range (len(num)):
        if i == 0 or i == 1:
            pass
        else: 
            mantisa.append(num[i])

    return fillBits2(mantisa, bits)

def definingPresitionValues(presition):
    if presition == 'single':
        bias = 127
        mantisa_bits = 23
    elif presition == 'double':
        bias = 1023
        mantisa_bits = 52

    return bias, mantisa_bits

def stringToBinary(string):
    binary = [int(char) for char in string]
    return binary

def validatingMantisa(mantisa):
    man = stringToBinary(mantisa) 
    if (man[0] == 0):
        man.pop(0)

    return man

def convertFraction(mantisa):
    fraction = []
    mantisa_2 = mantisa
    mantisa_2.reverse()

    for i in mantisa_2:
        if i == 0 and len(fraction) == 0:
            pass
        else:
            fraction.append(i)

    fraction.reverse()

    sum = 0
    for i in range (1, len(fraction) + 1):
        sum += fraction[i-1] * 2**(-i) 

    num = 1 + sum

    return num

def exponentToDecimal(exponent):

    exp = stringToBinary(exponent)
    if (exp[0] == 1):
        exp.insert(0, 0)

    return binaryToDecimal(exp)
#-------------------------------------------------------------------------------------

def decimalToBinary(num):

    if (num >= 0):
        return binaryToString(positiveIntToBinary(num))

    if (num < 0):
        return binaryToString(negativeIntToBinary(abs(num)))

def binaryToDecimal(num):

    while (validate(num) == False):
        num = input("Digite numero binario: ")
    

    binary = [int(char) for char in num] 

    if binary[0] == 0:
        return positiveBinaryToDecimal(binary)

    elif binary[0] == 1:
        return negativeBinaryToDecimal(binary)

def floatToBinary(num, presition):    
    """
    La presición se le pregunta al usuario, puede haber una opción para seleccionar 
    sigle presition o double presition
    """

    floating, integer = math.modf(num)

    binary_integer = binaryProcess(abs(int(integer)))
    binary_floating, periodic = floatingToBinary(abs(round(floating, 10)), presition)

    number, exp = normalizedNotation(binary_integer, binary_floating)

    bias, bits = definingPresitionValues(presition)

    exponent = exp + bias


    sign = floatSign(num)
    binary_exponent = binaryProcess(exponent)
    mantisa = normalizedMantisa(number, bits)

    if periodic == True:
        message = "Como el decimal es periodico, esta es una aproximación"
    else: 
        message = ''

    return sign, binaryToString(binary_exponent), binaryToString(mantisa), message

def binaryToFloat(sign, exponent, mantisa, presition):
    bias, bits = definingPresitionValues(presition)

    fraction = convertFraction(stringToBinary(mantisa))

    print("Exponent en decimal: ", binaryToDecimal(exponent))
    print("bias: ", bias)
    exp = exponentToDecimal(exponent) - bias


    print("Fraction: ", fraction)
    print("Exponent: ", exp)

    return ((-1)**int(sign) ) * fraction * 2**(exp)
    


