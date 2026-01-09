from datetime import datetime
import unittest

def area(width,height):
    if not isinstance(width,(int,float)):
        raise TypeError(f"width must be type of float or int, not {type(width)}")
    if not isinstance(height,(int,float)):
        raise TypeError(f"height must be type of float or int, not {type(height)}")
    if not (width>0 and height>0):
        raise ValueError("width and height must be positive values")
    return width*height 
class TestArea(unittest.TestCase):
    def test_area_1(self):
        self.assertEqual(area(4,5),20,'message not area 20') 
    def test_area_2(self):
        self.assertEqual(area(4,5),21,'message not area 21')
    def test_area_3(self):
        raise AssertionError('error message.')
    def test_area_4(self):
        raise TypeError('error message.')
if __name__=='__main__':
    unittest.main(verbosity=2)