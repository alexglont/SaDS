#########################################
##            Homework 7               ##
##           Problem  7.3              ##
##     Alexandru Mihai Glontaru        ##
#########################################

from math import log

def computeHash( auxh, power ):
    if power == 1: return auxh
    if power < 1: return 1

    p = int(log(power,2))
    h = auxh

    for i in range(p):
        h = (h**2)%9993201131

    return int((h*computeHash( auxh, power-2**p ))%9993201131)

def hash( x ):
    h = 0
    for i in x:
        word = ord(i)
        if word == 0: length = 0
        else: length = int(log( word, 2)) + 1
        word = word << (32-length)
        auxh = h+2+word
        h = computeHash(auxh, 1234567)


    return h

for i in range(97,122):
    print(hash(chr(i)),chr(i))

print(hash('pass'),'pass')
print(hash(''),'')
print(hash('1234'),'1234')
print(hash('password'),'password')
