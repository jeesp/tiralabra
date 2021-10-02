from app.app import App

def main():
    """
    Metodi sovelluksen käynnistämiseen.
    """
    app = App()
    i = 0
    x = 0
    for image in app.testdata:
        result = app.process_image(image)
        if result[0] == result[2][0]:
            x += 1
        i += 1
        print(str(x/i*100) + "%")
        if i >= 1:
            break

if __name__ == "__main__":
    main()
