#########################################
##            Homework 7               ##
##           Problem  7.1              ##
##     Alexandru Mihai Glontaru        ##
#########################################

from Crypto.Util.number import getPrime
from random import randint
from fractions import gcd

class AsymES:

    def inverse(self, e, m ):
        d = 0
        auxd = 1
        r = m
        auxr = e
        while auxr != 0:
            quot = r//auxr
            (d, auxd) = (auxd, d - quot*auxd)
            (r, auxr) = (auxr, r - quot*auxr)

        if d<0:
            d = d + m
        result = (self.e*d)%m
        print("e:",self.e," d:",d ," result:",result)
        return d


    def generateKey(self, n ):
        p = int(getPrime( n//2 + 3))
        q = int(getPrime( n//2 + 3))
        print("p:", p," q:", q)
        self.N = p*q
        m = (p-1)*(q-1)

        self.e = randint(2, m-1)
        while gcd(m,self.e)!=1 :
            self.e = (self.e+1)%m
        print("e:", self.e," m:", m, " gcd:",gcd(m,self.e))
        self.d = self.inverse( self.e, m )

    def encript(self, n, message ):
        cypher = 1

        for i in range(self.e):
            cypher = (cypher*message)%self.N

        return cypher

    def decript(self, n, cypher ):
        message = 1

        for i in range(self.d):
            message = (message*cypher)%self.N

        return message

n=4
myAsymES = AsymES()
myAsymES.generateKey(n)
print(myAsymES.decript(n,myAsymES.encript(n,9)))
