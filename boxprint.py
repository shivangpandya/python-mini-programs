'''
Progaram prints box of particular link and particular size
*******
*     *
*     *
*     *
*******
'''

def boxPrint(symbol,width,height):
    if len(symbol) ! = 1:
        raise Exception ( '"Symbol" needs to bea string of Length 1') #Custom Exception
    print(symbol * width )
    if (width<2 ) or (height <2) 
        raise Exception ( '"Width" and height must be greater than 2')

    for i in range(height-2)
        print(symbol + (' ' * (width-2)) + symbol )

    print symbol * width

boxprint('*',15,5)
boxPrint('O',5,16)
