# Numerontunnistus k-lähimmän naapurin algoritmilla

Projektissa toteutetaan ohjelma käsinkirjoitetun numeron tunnistamiseen.

## Dokumentaatio

[Määrittelydokumentti](https://github.com/jeesp/tiralabra/blob/main/dokumentaatio/maarittelydokumentti.md)
[Testausdokumentti](https://github.com/jeesp/tiralabra/blob/main/dokumentaatio/testausdokumentti.md)
[Toteutusdokumentti](https://github.com/jeesp/tiralabra/blob/main/dokumentaatio/toteutusdokumentti.md)
[Käyttöohje](https://github.com/jeesp/tiralabra/blob/main/dokumentaatio/kayttoohje.md)

## Viikkoraportit

[Viikko 1](https://github.com/jeesp/tiralabra/blob/main/dokumentaatio/viikkoraportit/viikko1.md)
[Viikko 2](https://github.com/jeesp/tiralabra/blob/main/dokumentaatio/viikkoraportit/viikko2.md)
[Viikko 3](https://github.com/jeesp/tiralabra/blob/main/dokumentaatio/viikkoraportit/viikko3.md)
[Viikko 4](https://github.com/jeesp/tiralabra/blob/main/dokumentaatio/viikkoraportit/viikko4.md)
[Viikko 5](https://github.com/jeesp/tiralabra/blob/main/dokumentaatio/viikkoraportit/viikko5.md)

## Käyttöohje testaamiseen

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
