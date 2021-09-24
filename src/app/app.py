import math
from data.load_data import load_traindata, load_testdata
from ui.ui import display_gui

class App:
    """
    Luokka sovelluslogiikan pyörittämiseen.
    """
    def __init__(self):
        self.traindata = load_traindata()
        self.testdata = load_testdata()
        self.nearestneighbors = []
        

    def process_image(self, input_image):
        """
        Metodi syötekuvan käsittelyyn.
        """
        nearest_neighbors = []
        for image in self.traindata:
            i = 0
            distance = 0
            while i < len(input_image[0]):
                distance += self.distance_calculation(input_image[0][i], image[0][i])
                i += 1
            nearest_neighbors.append((distance, image[1], image[0]))
        nearest_neighbors.sort(key=lambda a: (a[0]))
        display_gui(input_image, nearest_neighbors[:7])
        return (input_image[1], nearest_neighbors[:7])

    def distance_calculation(self, row1, row2):
        """
        Metodi laskee yksittäisen rivin etäisyyden testattavan kuvan
        ja harjoittelukuvan välillä.
        """
        distance = 0
        i = 0
        while i < len(row1):
            distance += (int(row1[i]) - int(row2[i]))**2
            i += 1
        return math.sqrt(distance)
    