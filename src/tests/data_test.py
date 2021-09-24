import unittest
from data.load_data import load_testdata, load_traindata

class TestData(unittest.TestCase):

    def test_train_data_length(self):
        data = load_traindata()
        self.assertEqual(len(data), 1000)
    def test_test_data_length(self):
        data = load_testdata()
        self.assertEqual(len(data), 100)