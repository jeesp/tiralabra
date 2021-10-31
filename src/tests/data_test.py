import unittest
from data.load_data import load_data

class TestData(unittest.TestCase):

    def test_train_data_length(self):
        data = load_data(True, 1000)
        self.assertEqual(len(data), 1000)
    def test_test_data_length(self):
        data = load_data(False, 100)
        self.assertEqual(len(data), 100)