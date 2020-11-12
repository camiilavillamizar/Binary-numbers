import math

def menu():
    print("Seleccione 1 para convertir numeros enteros a numeros binarios")
    print("Seleccione 2 para convertir numeros binarios a numeros enteros")
    print("Seleccione 3 para convertir numeros decimales a numeros binarios")
    print("Seleccione 4 para convertir numeros binarios a numeros decimales")
    print("Seleccione 5 para convertir numeros flotantes a binarios")
    print("Seleccione 6 para convertir numeros binarios a flotantes")

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
def negativeIntToBinary(num, bits):
    return fillBits(add1(swap(binaryProcess(num))), bits, True)

def positiveIntToBinary(num, bits):
    return fillBits(binaryProcess(num), bits, False)

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
    
def positiveBinaryToInteger(binary):
    decimal = 0
    binary.reverse()
    for i in range (len(binary)):
        decimal += int(binary[i]) * 2**i
    return decimal

def negativeBinaryToInteger(num):
    return positiveBinaryToInteger(add1(swap(num)))

def floatingToBinary(floating, presition):
    binary_float = []
    float_numbers = []

    if presition == 'single':
        presition_number = 23
    elif presition == 'double':
        presition_number = 52
    else: 
        presition_number = presition

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
    periodic_binary = True

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
        exponent_bits = 8
    elif presition == 'double':
        bias = 1023
        mantisa_bits = 52
        exponent_bits = 11

    return bias, mantisa_bits, exponent_bits

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

def binaryDecimalPartToDecimal(decimal):
    string = str(decimal)

    decimalBinario = 0

    exponent = -1
    for i in string:
        decimalBinario += int(i)*(2**exponent)
        exponent -= 1
    
    DecimalBinario = str(decimalBinario)
    final = ""
    flag = False
    for i in DecimalBinario:
        if (i == '.'):
            flag = True
        
        if (flag):
            if i != '.':
                final += i
    return final

#-------------------------------------------------------------------------------------

def integerToBinary(num, bits):

    if (num >= 0):
        return binaryToString(positiveIntToBinary(num, bits))

    if (num < 0):
        return binaryToString(negativeIntToBinary(abs(num), bits))

def binaryToInteger(num, bits):

    while (validate(num) == False):
        num = input("Digite numero binario: ")
    
    while (len(num) > bits):
        print("len(num): ", len(num), "bits: ", bits, "num: ", num)
        num = input("Hay mayor numero de bits de los requeridos. Digite nuevamente: ")

    binary = [int(char) for char in num] 

    if len(binary) == bits:
        if binary[0] == 0:
            return positiveBinaryToInteger(binary)

        elif binary[0] == 1:
            return -negativeBinaryToInteger(binary)
    else:
        return positiveBinaryToInteger(binary)

def decimalToBinary(num, bits):

    floating, integer = math.modf(num)

    if (num > 0):
        first = binaryProcess(int(integer))
    elif (num < 0):
        first = -add1(swap(binaryProcess(abs(int(integer)))))
    
    decimalBinario, m = floatingToBinary(abs(round(floating, 10)), bits - len(binaryToString(first)))

    binary = binaryToString(first)+'.'+ binaryToString(decimalBinario)
    result = binary

    if (len(binary) + 1 < bits):
        result = ''
        diff = bits - len(binary) + 1
        for i in range (diff):
            result += '0'
        result += binary
    
    if len(binary) + 1 > bits:
        result = ''
        for i in range (bits + 1): 
            result += binary[i]

    return result

def binaryToDecimal(num, bits):
    flag = True

    integer = ""
    decimal = ""
    for i in num: 
        if i == '.':
            flag = False

        if (flag):
            integer += i
        else:
            if i != '.':
                decimal +=i

    decimalBinario = binaryDecimalPartToDecimal(decimal)
    first = binaryToInteger(integer, bits - len(decimalBinario))

    return str(first) +'.'+ decimalBinario

def floatToBinary(num, presition):    
    """
    La presición se le pregunta al usuario, puede haber una opción para seleccionar 
    sigle presition o double presition
    """

    floating, integer = math.modf(num)

    print(floating)
    binary_integer = binaryProcess(abs(int(integer)))
    binary_floating, periodic = floatingToBinary(abs(round(floating, 60)), presition)

    number, exp = normalizedNotation(binary_integer, binary_floating)

    bias, bitsf, bitse = definingPresitionValues(presition)

    exponent = exp + bias

    sign = floatSign(num)
    binary_exponent = binaryProcess(exponent)

    exponent_result = binary_exponent
    if len(binaryToString(binary_exponent)) < bitse:
        exponent_result = ''
        diff = bitse - len(binaryToString(binary_exponent))
        for i in range (diff):
            exponent_result += '0'
        exponent_result += binaryToString(binary_exponent)
    
    mantisa = normalizedMantisa(number, bitsf)

    if periodic == True:
        message = "Como el decimal es periodico, esta es una aproximación"
    else: 
        message = ''

    return sign, binaryToString(exponent_result), binaryToString(mantisa), message

def binaryToFloat(sign, exponent, mantisa, presition):
    bias, bitf, bitse = definingPresitionValues(presition)

    while (len(exponent) != bitse):
        print("Error, digite de manera correcta el exponente. Debe tener ", bitse, " bits")
    while (len(sign) != 1):
        print("Error, digite de manera correcta el sgno. Debe tener 1 bit")


    fraction = convertFraction(stringToBinary(mantisa))

    print("Exponent en decimal: ", positiveBinaryToInteger(stringToBinary(exponent)))
    print("bias: ", bias)
    exp = positiveBinaryToInteger(stringToBinary(exponent)) - bias 


    print("Fraction: ", fraction)
    print("Exponent: ", exp)

    return ((-1)**int(sign) ) * fraction * 2**(exp)
    


