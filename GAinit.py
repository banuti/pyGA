#!/usr/bin/python
# provides constants for GA

print 'reading constants'

# #natural
# maxgen=15           # integer: number of generations
# maxpop=30           # integer: maximum population
chromlen=10          # integer: length of chromosomes
mutprob=0.01       # float (<=1): mutation probability

# #artificial
crossprob=0.6       # float (<=1): crossover probability
floodfactor=0.85     # float (<=1): fitness scaling with avg
# vaccbestprob=0.2        # float (<=1): spread best from previous generation


   
def F(param):

    A=param['A']
    B=param['B']
    
    f=(A**2 + B**2)/2.0

##    print f

    return f
    



