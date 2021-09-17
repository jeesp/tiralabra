import random
import mnist

def load_traindata():
    """
    Lataa vertailudatasetin mnistilta. Alkuperäisessä setissä on
    60000 kuvaa, joten tässä lisäksi toiminto, joka muodostaa
    datasta 1000 kuvan samplen.
    """
    train_images = mnist.train_images()
    train_labels = mnist.train_labels()
    i = 0
    training_sample = []
    while i < 100:
        number = random.randint(0,len(train_images)-1)
        training_sample.append((train_images[number], train_labels[number]))
        i += 1
    return training_sample

def load_testdata():
    """
    Lataa testidatasetin Mnistilta.
    """
    test_images = mnist.test_images()
    test_labels = mnist.test_labels()
    i = 0
    test_set = []
    while i < 100:
        number = random.randint(0,len(test_images)-1)
        test_set.append((test_images[number], test_labels[number]))
        i += 1
    return test_set
