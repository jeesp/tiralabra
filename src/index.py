from app.app import App

def main():
    """
    Metodi sovelluksen käynnistämiseen.
    """
    app = App()
    app.start()
    # Jos haluat testata ohjelman tarkkuutta,
    # vaihda app.start() -> app.test_accuracy()
    # Testidatan kokoa voi muuttaa luokan App muuttujasta testdata_size
    # Vertailudatan kokoa voi muuttaa luokan App muuttujasta traindata_size

if __name__ == "__main__":
    main()
