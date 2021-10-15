from app.app import App

def main():
    """
    Metodi sovelluksen käynnistämiseen.
    """
    app = App()
    app.start()
    # Jos haluat testata ohjelman tarkkuutta,
    # vaihda app.start() -> app.test_accuracy()

if __name__ == "__main__":
    main()
