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
def volume(a,b,c):
    if not isinstance(a,(int,float)):  
        raise TypeError("bad type of one of input value")
    if not isinstance(b,(int,float)):
        raise TypeError("bad type of one of input value")
    if not isinstance(c,(int,float)):
        raise TypeError("bad type of one of input value")
    if not (a>0 and b>0 and c>0):
        raise ValueError("one value is negative")
    return a*b*c
class TestArea(unittest.TestCase):
    def test_area(self):
        self.assertEqual(area(4,5),20,'message')
    def test_area_incorrect_type_raises_error(self):
        self.assertRaises(TypeError,area,'4',5)
        self.assertRaises(TypeError,area,4,'5')
    def test_area_negative_values_raises_error(self):
        self.assertRaises(ValueError,area,-4,5)
        self.assertRaises(ValueError,area,4,-5)
class TestVolume(unittest.TestCase):
    def volume_test(self):
        self.assertEqual(TypeError,volume(3,3,3),28,'bad volume')
    def test_volume_incorrect_type_raises_error(self):
        self.assertRaises(TypeError,volume,'3',3,3)
        self.assertRaises(TypeError,volume,3,'3',3)
        self.assertRaises(TypeError,volume,3,3,'3')
        self.assertRaises(ValueError,volume,-3,3,3)
        self.assertRaises(ValueError,volume,3,-3,3)
        self.assertRaises(ValueError,volume,3,3,-3)
if __name__=='__main__':
    unittest.main(verbosity=2)