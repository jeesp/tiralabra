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
        self.app.input_image = self.app.testdata[0]
        self.app.process_image()
        self.assertEqual(len(self.app.nearest_neighbors), self.app.k)
        i = 1
        if self.app.k > 1:
            while i < self.app.k:
                self.assertGreater(self.app.nearest_neighbors[i][2], self.app.nearest_neighbors[i-1][2])
                i += 1

    def test_calculate_guess(self):
        self.app.input_image = self.app.testdata[0]
        self.app.process_image()
        self.assertEqual(len(self.app.calculate_the_guess()), 2)
