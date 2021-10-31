import math
import time
from data.load_data import load_data
from ui.ui import display_gui

class App:
    """
    Luokka sovelluslogiikan pyörittämiseen.
    """
    def __init__(self):
        self.traindata_size = 1000
        self.testdata_size = 1000
        self.traindata = load_data(True, self.traindata_size)
        self.testdata = load_data(False, self.testdata_size)
        self.nearest_neighbors = []
        self.test_samples = self.testdata[:100]
        self.input_image = []
        self.guess = []
        self.right_answers = 0
        self.guesses = 0
        self.success_rate = 0.0
        self.k = 6
    def start(self):
        """
        Metodi sovelluksen käynnistämiseen.
        """
        display_gui(self)

    def test_accuracy(self):
        """
        Metodi ohjelman onnistumisprosentin laskemiseen.
        Testin voi suorittaa index-tiedostosta.
        """
        i = 0
        x = 0
        starting_time = time.time()
        for image in self.testdata:
            self.input_image = image
            self.process_image()
            if self.guess[0] == self.input_image[1]:
                x += 1
            i += 1
            print(str(round(x/i*100, 2)) + "%")
            if i%100 == 0:
                print("sekunteja:", round(time.time() - starting_time, 2))
        end_time = time.time()
        print("Aikaa kului ", round(end_time-starting_time, 2), " sekuntia")
    def process_image(self):
        """
        Metodi syötekuvan käsittelyyn.
        """
        # Looppi käy läpi vertailudatan, ja lisää kuvia lähimpien naapurien listaan
        # mikäli niitä siihen vielä mahtuu. Jos ei, rajataan lista takaisin k:n pituiseksi
        self.nearest_neighbors = []
        for image in self.traindata:
            i = 0
            distance = 0
            in_list = False
            while i < len(self.input_image[0]):
                distance += self.distance_calculation(self.input_image[0][i], image[0][i])
                i += 1
            i = 0
            while i < len(self.nearest_neighbors):
                if distance < self.nearest_neighbors[i][2]:
                    self.nearest_neighbors.insert(i, (image[0], image[1], distance))
                    in_list = True
                    break
                i += 1
            if i < self.k:
                if not in_list:
                    self.nearest_neighbors.append((image[0], image[1], distance))
            else:
                if not in_list:
                    self.nearest_neighbors = self.nearest_neighbors[:self.k]

        self.guess = self.calculate_the_guess()
        self.guesses += 1
        if self.guess[0] == self.input_image[1]:
            self.right_answers += 1
        self.success_rate = self.right_answers/self.guesses*100
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
        """
        Metodi koneen veikkauksen laskemiseen.
        """
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
