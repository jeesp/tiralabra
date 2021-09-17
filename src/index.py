from app.app import App
def main():
    """
    Metodi sovelluksen käynnistämiseen.
    """
    app = App()
    dataset = app.traindata
    print(dataset)

if __name__ == "__main__":
    main()
