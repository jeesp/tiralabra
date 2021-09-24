from app.app import App

def main():
    """
    Metodi sovelluksen käynnistämiseen.
    """
    app = App()
    i = 0
    for image in app.testdata:
        app.process_image(image)
        i += 1
        if i >= 5:
            break

if __name__ == "__main__":
    main()
