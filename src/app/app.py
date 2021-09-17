import math
from data.load_data import load_traindata, load_testdata

class App:
    """
    Luokka sovelluslogiikan pyörittämiseen.
    """
    def __init__(self):
        self.traindata = load_traindata()
        self.testdata = load_testdata()
        self.nearestneighbors = []

    def process_image(self):
        """
        Metodi syötekuvan käsittelyyn.
        """
        return
    def distance_calculation(self, row1, row2):
        """
        Metodi laskee yksittäisen rivin etäisyyden testattavan kuvan
        ja harjoittelukuvan välillä.
        """
        distance = 0
        i = 0
        while i < len(row1):
            distance += (row1[i] - row2[i])**2
            i += 1
        return math.sqrt(distance)
    