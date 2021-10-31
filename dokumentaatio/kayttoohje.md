# Käyttöohje testaamiseen

<h3> Konfigurointi </h3>

1. Asenna riippuvuudet komennolla:

```bash
poetry install
```

Ohjeet Poetryn lataamiseen löydät tarvittaessa esimerkiksi [täältä](https://ohjelmistotekniikka-hy.github.io/python/poetry).

2. Käynnistä sovellus komennolla:

```bash
poetry run invoke start
```

## Testaus

1. Testit voi suorittaa komennolla:

```bash
poetry run invoke test
```

2. Testikattavuusraportin voi generoida komennolla:

```bash
poetry run invoke coverage-report
```

3. Pylint-tarkistuksen voi suorittaa komennolla:

```bash
poetry run invoke lint
```

## Ohjelman käyttäminen

Ohjelman käynnistyessä valitse ikkunan oikeasta laidasta haluamasi vertailukuva. Ohjelma laskee lähimmät naapurit ja antaa tämän jälkeen veikkauksen numerosta. Ruudun vasemmassa alareunassa näkyy koneen veikkaus ja onnistumisprosentti. Voit klikata useampaa eri kuvaa ja tarkistaa miten kone suoriutuu eri kuvista.

Jos haluat suorittaa vertailuanalyysia, voit vaihtaa index.py tiedostosta start-komennon tilalle test_accuracy. Tämä toiminto printtaa komentoriville onnistumisprosentin ja lopuksi testin suorittamiseen kuluneen ajan sekunteina. Voit vaihtaa vertailudatan kokoa, testattavien kuvien määrää sekä k:n arvoa luokan App muuttujista. Luokka App löytyy tiedostosta app/app.py.
