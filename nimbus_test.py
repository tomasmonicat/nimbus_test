# -*- coding: utf-8 -*-
"""
This script contains the Python Challenge for the Analytics Engineer 
traineeship at Nimbus Intelligence Academy
"""

import random

def nimbus_test():
    """
    The function creates two random numbers and multiplies them. If the 
    result equals 4, the function ends with success. If not, it prints 
    one of the two numbers and the result of the multiplication and 
    starts over.
    """
    a = random.randrange(1,10)
    b = random.randrange(1,10)
    c = a * b
    if c == 4:
        print('Success! A = {}, B = {}'.format(a, b))
    else:
        print('A = {}, C = {}'.format(a, c))
        nimbus_test()
        
if __name__ == '__main__':
    nimbus_test()