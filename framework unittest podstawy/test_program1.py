import unittest
from datetime import datetime
import os
import pathlib 

class TestArea(unittest.TestCase):
    def test_area(self):
        self.assertEqual(area(4,5),20,'message')
    def test_circle(self):
        self.assertEqual(area_circle(2),6.328)
class TestAreaSquare(unittest.TestCase):
    def test_area_square(self):
        self.assertEqual(area(10,5),50)
def area_circle(radius):
    return radius*3.14
def area(width,height):
    if not isinstance(width,(float,int)):
        raise TypeError(f"width must be float or integer value, not {type(width)}")
    if not isinstance(height,(float,int)):
        raise TypeError(f"height must be float or integer value, not {type(width)}")
    if width<0 or height<0:
        raise ValueError(f"width and height must be postive values")
    return width*height

area1=area(20,20)
assert area1==400,'wrong calculated area!'
print(f"area1={area1}")
# area2=area(10,-10)
# assert area2==100,'wrong calculated area!'
# print(area2)

test_area1=TestArea()

if __name__=='__main__':
    unittest.main(verbosity=2)