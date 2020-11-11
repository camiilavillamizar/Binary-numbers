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
    print(integerToBinary(2))
elif (res == 2):
    print(binaryToInteger('100010010101'))
elif( res == 3):
    print(decimalToBinary(1.125))
elif (res == 4):
    print(binaryToDecimal('1.001'))
elif (res == 5):
    sign, exponent, mantisa, m = floatToBinary(0.125, 'single')
    print("sign: ", sign)
    print("exponent: ", exponent)
    print("mantisa: ", mantisa)
    print("m: ", m)

elif (res == 6):
    print(binaryToFloat('0', '10000101', '010101001', 'single'))



