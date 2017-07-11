#!/usr/bin/python
# provides math functions for GA
from random import *



def minimum(list):
    return min(list)

def maximum(list):
    return max(list)

def fitsum(list):
    """Sum of fitnesses in the list, needed to build 
    wheel of fortune."""
    sum=0.0
    for i in range(0,len(list)):
        sum+=list[i]
    return sum
    
def avg(list):
    """Returns average fitness of entity in list."""
    sum=fitsum(list)
    return (sum/len(list))
            
def bin_dec(bin):
    """Conversion binary -> decimal. Needed to calculate 
    decimal variable value from binary coded genome."""
    dec=0.0
    bin.reverse()
    for i in range(0, len(bin)):
        dec+=(bin[i]*(2**i))
    return dec
            

def dec_bin(dec):
    #
    pass


def flip():
    """Flips a coin. Returns 1 or 0 with 0.5 probability, respectively."""    
    tmp=decide(0.50)
    return tmp
           
def decide(prob):
    """ Returns true with 'prob' probability as a way to 
    decide the outcome of an event."""
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

