import unittest
from datetime import datetime
import os
import pathlib 
amount=1000
taxi_rate=1.15

width=int(input('Enter width of rectangle:\n'))
height=int(input('Enter height of rectangle:\n'))

assert width>0,'width can not be negative'
assert height>0,'height can not be negative'

area=width*height
print('Area:{}'.format(area))