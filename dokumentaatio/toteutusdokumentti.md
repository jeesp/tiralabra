# Toteutusdokumentti

Ohjelman tehokkuutta on testattu vaihtamalla vertailudatan määrää. Kuten O-analyysissa on todettu, ohjelman suorittamiseen vaadittava aika kasvaa lineaarisesti vertailudatan kokoon nähden. Tämä myös huomataan suorituskykyvertailussa.

### Ohjelman yleisrakenne

Luokka App huolehtii sovelluslogiikan pyörittämisestä, se löytyy tiedostosta app/app.py.

MNISTIN tarjoama kuvadata ladataan load_data.py -tiedostossa.

Graafinen käyttöliittymä luodaan ja ylläpidetään tiedostossa ui/ui.py.

### O-analyysit

K-n lähimmän naapurin algoritmin aikavaativuus on O(ndk), missä n=harjoitusdatan koko, d=28x28 (pikseleiden määrä yhdessä kuvassa) ja k=naapureiden määrä.
Tilavaatimus on O(ndk), harjoitusdatan koko x 28x28 pikseliä x naapureiden määrä.

### Suorituskyky- ja O-analyysivertailu

Sovelluksen suorituskykyä testattiin eri vertailudatan (n) kokoluokilla, 1000 testikuvalla:

k = naapureiden määrä

k=7:
Kun n = 100: 59.4% Aikaa kului 56.23 sekuntia
Kun n = 1000: 85.0% Aikaa kului 439.59 sekuntia (7 min 19 s)
Kun n = 10000: 92.4% Aikaa kului 4613.7 sekuntia (76 min 53 s)

k=6:
Kun n = 100: 65.6%. Aikaa kului 44.54 sekuntia
Kun n = 1000: 88.7%. Aikaa kului 430.19 sekuntia
Kun n = 10000: 94.2%. Aikaa kului 4566.39 sekuntia

k=5:
Kun n = 100: 63.4%. Aikaa kului 48.64 sekuntia
Kun n = 1000: 87.4%. Aikaa kului 436.43 sekuntia
Kun n = 10000: 94.3%. Aikaa kului 4382.38 sekuntia

k=1:
Kun n = 100: 65.7%. Aikaa kului 44.58 sekuntia
Kun n = 1000: 88.7%. Aikaa kului 419.85 sekuntia
Kun n = 10000: 93.6%. Aikaa kului 4322.41 sekuntia

### Puutteet ja parannusehdotukset

Eri k:n arvojen välisiä vertailuja olisi voinut tehdä isommalla otannalla, esimerkiksi 10000 testikuvalla. 1000 kuvan testit antavat kuitenkin hyvän arvion onnistumisprosentista. Lisäksi testejä olisi voinut suorittaa vielä useammalla eri k:n arvolla.

### Lähteet

https://stats.stackexchange.com/questions/219655/k-nn-computational-complexity

https://www.javatpoint.com/k-nearest-neighbor-algorithm-for-machine-learning
