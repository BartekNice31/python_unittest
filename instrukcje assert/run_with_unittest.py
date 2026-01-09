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
    def test_area(self):
        self.assertEqual(area(4,5),20,'message')
    def test_area_incorrect_type_raises_error(self):
        self.assertRaises(TypeError,area,'4',5)
        self.assertRaises(TypeError,area,4,'5')
    def test_area_negative_values_raises_error(self):
        self.assertRaises(ValueError,area,-4,5)
        self.assertRaises(ValueError,area,4,-5) 
 