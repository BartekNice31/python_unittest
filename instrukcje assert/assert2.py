import unittest
from datetime import datetime
import os
import pathlib 
amount=1000
taxi_rate=1.15

assert amount>=0,'The amount should not be negative'
assert 0<taxi_rate<1, 'Taxi rate above of boundaries'