from functions import *


"""
Se hace un menu bonito con 4 botones 
 - NUMERO DECIMAL A BINARIO (+ y -) -ready
 - NUMERO BINARIO A DECIMAL ENTERO (+ y -) -ready
 - NUMERO FLOAT A BINARIO (+ y -) -ready

 - NUMERO BINARIO A FLOAT

 Aca lo voy a hacer seleccionando la opción
"""
menu()
res = int(input('SELECCIONE OPCIÓN: '))

if (res == 1):
    print(decimalToBinary(2))
elif (res == 2):
    print(binaryToDecimal('100010010101'))
elif (res == 3):
    sign, exponent, mantisa, m = floatToBinary(85.125, 'single')
    print("sign: ", sign)
    print("exponent: ", exponent)
    print("mantisa: ", mantisa)
    print("m: ", m)

elif (res == 4):
    print(binaryToFloat('0', '10000101', '010101001', 'single'))



