#!/usr/bin/python
#GA main program

from pyGA import *



# def F(param):

#     A=param['A']
#     B=param['B']
    
#     f=(A**2 + B**2)/2.0

#     return f
    


population = 1000
generations = 1000

world1=World(population,generations)

world1.runworld()
   
world1.showreport()



# TODO 