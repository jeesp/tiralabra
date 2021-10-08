# Testausdokumentti

Projektin testaaminen on hieman hankalaa, sillä prosessoitava kuva vaihtelee ja näin myös tunnistuksen tulokset vaihtelevat. Yksittäiset apumetodit on pyritty testaamaan kattavasti.

Ohjelmaa testataan empiirisesti jatkuvasti. Ohjelma näyttää yksittäisen kuvan algoritmin antaman veikkauksen, sekä prosenttiosuuden tästä numerosta lähimpien naapureiden joukossa.

Ohjelma antaa myös komentoriville prosenttiosuuden oikein menneistä arvauksista.

##

Ohjelmaa testattu eri vertailudatan (n) kokoluokilla:
Kun n = 100: ~63% onnistuminen. Testi suoritettiin 5000 testikuvalla (Aikaa kului n. puoli minuuttia)
Kun n = 1000: ~85% onnistuminen. Testi suoritettiin 1000 testikuvalla (Aikaa kului n. 5 minuuttia)
Kun n = 10000: ~93% onnistuminen. Testi suoritettiin 100 testikuvalla (Aikaa kului n. 3 minuuttia)

### Kattavuusraportti:

![Kattavuusraportti](kattavuusraportti.png)
