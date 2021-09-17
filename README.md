# Numerontunnistus k-lähimmän naapurin algoritmilla

Projektissa toteutetaan ohjelma käsinkirjoitetun numeron tunnistamiseen.

## Dokumentaatio

[Määrittelydokumentti](https://github.com/jeesp/tiralabra/blob/main/dokumentaatio/maarittelydokumentti.md)

## Viikkoraportit

[Viikko 1](https://github.com/jeesp/tiralabra/blob/main/dokumentaatio/viikkoraportit/viikko1.md)
[Viikko 2](https://github.com/jeesp/tiralabra/blob/main/dokumentaatio/viikkoraportit/viikko2.md)

## Käyttöohje testaamiseen

<h3> Konfigurointi </h3>

1. Asenna riippuvuudet komennolla:

```bash
poetry install
```

Ohjeet Poetryn lataamiseen löydät tarvittaessa esimerkiksi [täältä](https://ohjelmistotekniikka-hy.github.io/python/poetry).

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
