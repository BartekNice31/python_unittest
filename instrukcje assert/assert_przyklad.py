import unittest
from datetime import datetime
import os
import pathlib 


def area(width,height):
    assert (type(width)==int or type(width)==float),'width must be int or float value'
    assert (type(height)==int or type(height)==float),'width must be int or float value'
    assert width>0,'width must be positive value'
    assert height>0,'height must be positive value'
    if type(width)==float or type(height)==float:
        return round(width*height,2)
    else:
        return width*height
    
print(area(5.0,6.4322))
#print(area('s',9))
print(area(10,10))

assert area(4,10)==50,'invalid parameters of area'