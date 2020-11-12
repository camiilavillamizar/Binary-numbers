from functions import *


"""
Se hace un menu bonito con 4 botones 
 - NUMEROENTERO A BINARIO (+ y -)
 - NUMERO BINARIO A ENTERO (+ y -) 
 - NUMERO FLOAT A BINARIO (+ y -) 
 - NUMERO BINARIO A FLOAT

 Aca lo voy a hacer seleccionando la opción
"""
menu()
res = int(input('SELECCIONE OPCIÓN: '))

if (res == 1):
    print(integerToBinary(2, 8))
elif (res == 2):
    print(binaryToInteger('111110', 6))
elif( res == 3):
    print(decimalToBinary(11.25e-1, 10)) 
elif (res == 4):
    print(binaryToDecimal('1.001', 10))
elif (res == 5):
    sign, exponent, mantisa, m = floatToBinary(263.3, 'single')
    print("sign: ", sign)
    print("exponent: ", exponent)
    print("mantisa: ", mantisa)
    print("m: ", m)

elif (res == 6):
    print(binaryToFloat('0', '10000111', '00000111010011001100110', 'single'))



