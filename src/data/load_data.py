import random
import mnist

def load_data(training, size):
    """
    Lataa vertailudatasetin mnistilta. Alkuperäisessä setissä on
    60000 kuvaa, joten tässä lisäksi toiminto, joka muodostaa
    datasta 1000 kuvan samplen.
    """
    if training:
        images = mnist.train_images()
        labels = mnist.train_labels()
    else:
        images = mnist.test_images()
        labels = mnist.test_labels()
    i = 0
    sample_set = []
    while i < size:
        number = random.randint(0, len(images)-1)
        sample_set.append((images[number], labels[number]))
        i += 1
    return sample_set
