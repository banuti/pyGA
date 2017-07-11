#!/usr/bin/python



   
def F(param):
    """Fitness function to be maximized, parameterized 
    using the variables A and B."""


    A=param['A']
    B=param['B']
    
    f=(A**2 + B**2)/2.0

    return f
    



