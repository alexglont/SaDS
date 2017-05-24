#########################################
##            Homework 7               ##
##           Problem  7.2              ##
##     Alexandru Mihai Glontaru        ##
#########################################

#################################################################
## As we can notice by hashing the first 100 natural numbers,  ##
## all the powers of 2 have the same encoding.                 ##
## Collision appears in the case of the powers of 2            ##
#################################################################


from math import log

def computeHash( auxh, power ):
    if power == 1: return auxh
    if power < 1: return 1

    p = int(log(power,2))
    h = auxh

    for i in range(p):
        h = (h**2)%9993201131

    return ((h*computeHash( auxh, power-2**p ))%9993201131)

def hash( x ):
    if x==0: length = 0
    else: length = int(log( x, 2 )) + 1

    if length%32 != 0:
        shiftSize = 32 - (length % 32)
        length = length + shiftSize
        x = x<<shiftSize #padding the message

    h = 0

    mask = 2**32 - 1

    for i in range(length/32):
        word = (x & (mask<<(length/32-i-1)))>>(length/32-i-1)
        auxh = h+2+word
        h = computeHash(auxh, 1234567)


    return h

for i in range(1,100):
    print("%d -> %d" %(i,hash(i)))
