#!/usr/bin/python
#GA main program

from pyGA import *
    

# set world constants
population  = 100
generations = 1000

# create world with given number of generations 
# and number of entities per generation
world1=World(population,generations)

# run optimization
world1.runworld()

# show final results
world1.showreport()

