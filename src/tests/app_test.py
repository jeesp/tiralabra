import unittest
from app.app import App

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = App()

    def test_distance_calculation(self):
        row1 = [0,0,0,1,0,1,0,0,0]
        row2 = [0,0,0,1,0,0,0,0,0]
        row3 = [1,1,1,1,1,1,1,1,1]
        distance1 = self.app.distance_calculation(row1, row2)
        distance2 = self.app.distance_calculation(row1, row3)
        self.assertGreater(distance2, distance1)
    
    def test_process_image(self):
        img = self.app.testdata[0]
        result = self.app.process_image(img)
        self.assertEqual(len(result[1]), 7)
