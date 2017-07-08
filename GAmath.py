#!/usr/bin/python
# provides math functions for GA
from random import *



def minimum(list):
        return min(list)

def maximum(list):
        return max(list)

def fitsum(list):
        sum=0.0
        for i in range(0,len(list)):
            sum+=list[i]
        return sum
        
def avg(list):
        sum=fitsum(list)
        return (sum/len(list))
            
def bin_dec(bin):
        dec=0.0
        bin.reverse()
        for i in range(0, len(bin)):
            dec+=(bin[i]*(2**i))
        return dec
            

def dec_bin(dec):
        #
        pass


def flip():
        tmp=decide(0.50)
        return tmp
           
def decide(prob):
        tmp=random()
        if tmp>=prob:
            return 0
        if tmp<prob:
            return 1

def rangeint(lo, hi):
        if hi>lo:
            tmp=randrange(lo, hi)
            return tmp
        else:
            return hi

def rangefloat(lo, hi):
        pass

def rnd():
        return random()

