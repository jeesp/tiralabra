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
        self.nearest_neighbors = []
        self.test_samples = self.testdata[:9]
        self.input_image = []
        self.guess = []
    def start(self):
        i = 0
        x = 0
        display_gui(self)
        #for image in self.testdata:
        #    self.input_image = image
        #    
        #    if self.guess[0] == self.input_image[1]:
        #        x += 1
        #    i += 1
        #    print(str(x/i*100) + "%")
        #    display_gui(self)
        #    if i >= 1:
        #        break

    def process_image(self):
        """
        Metodi syötekuvan käsittelyyn.
        """
        self.nearest_neighbors = []
        for image in self.traindata:
            i = 0
            distance = 0
            added = False
            while i < len(self.input_image[0]):
                distance += self.distance_calculation(self.input_image[0][i], image[0][i])
                i += 1
            i = 0
            while i < len(self.nearest_neighbors):
                if distance < self.nearest_neighbors[i][2]:
                    self.nearest_neighbors.insert(i, (image[0], image[1], distance))
                    added = True
                    break
                i += 1
            if i < 7:
                if not added:
                    self.nearest_neighbors.append((image[0], image[1], distance))
            else:
                if not added:
                    self.nearest_neighbors = self.nearest_neighbors[:7]

        self.guess = self.calculate_the_guess()
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

    def calculate_the_guess(self):
        nearest = {}
        for neighbor in self.nearest_neighbors:
            if neighbor[1] not in nearest:
                nearest[neighbor[1]] = 1
            else:
                nearest[neighbor[1]] += 1
        number = 11
        count = 0
        for neighbor in nearest:
            if nearest[neighbor] > count:
                number = neighbor
                count = nearest[neighbor]
        return [number, count]
