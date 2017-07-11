#!/usr/bin/python



   
def F(param):
    """Fitness function to be maximized, parameterized 
    using the variables A and B. Has to return a float 
    value, representative of the 'quality' of the parameters.
    The fitness is higher when better the parameters are chosen."""


    A=param['A']
    B=param['B']
    
    f=(A**2 + B**2)/2.0

    return f
    



