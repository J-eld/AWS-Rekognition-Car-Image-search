from django.test import TestCase
import unittest
from Rekog import Rekog


# Create your tests here.

class TestAWSRekognition(unittest.TestCase):
    def test_sedan(self):
        self.assertTrue(Rekog('photos/sedan.jpg'), 'sedan')

    def test_coupe(self):
        self.assertTrue(Rekog('photos/coupe.jpg'), 'coupe')

    def test_suv(self):
        self.assertTrue(Rekog('photos/suv.jpg'), 'suv')

    def test_convertible(self):
        self.assertTrue(Rekog('photos/convertible.jpg'), 'convertible')

    def test_van(self):
        self.assertTrue(Rekog('photos/van.jpg'), 'van')

    def test_truck(self):
        self.assertTrue(Rekog('photos/truck.jpg'), 'truck')

if __name__ == '__main__':
    unittest.main()