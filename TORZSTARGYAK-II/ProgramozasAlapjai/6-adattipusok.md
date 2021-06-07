# 6. Egyszerű adattípusok: egész, valós, logikai és karakter típusok és kifejezések. Az egyszerű típusok reprezentációja, számábrázolási tartományuk, pontosságuk, memória igényük és műveleteik. Az összetett adattípusok és a típusképzések, valamint megvalósításuk C nyelven. A pointer, a tömb, a rekord és az unió típus. Az egyes típusok szerepe, használata


## Egyszerű adattípusok: egész, valós, logikai és karakter típusok és kifejezések. Az egyszerű típusok reprezentációja, számábrázolási tartományuk, pontosságuk, memória igényük és műveleteik

Az elemi adattípusok értékeit nem lehet önmagukban értelmes részekre bontani.

Ha a nyelv szintaktikája szerint a program egy adott pontján típusnak kellene következnie de az hiányzik, a fordító a típus helyére automatikusan int-et helyettesít.

### Egész típusok

A C nyelvben az egész típus az int.

Az int típus értékkészlete az alábbi kulcsszavakkal módosítható:

- signed: A típus előjeles értékeket fog tartalmazni (int, char).
- unsigned: A típus csak előjeltelen, nemnegatív értékeket fog tartalmazni (int, char).
- short: Rövidebb helyen tárolódik, így kisebb lesz az értékkészlet (int).
- long: Hosszabb helyen tárolódik, így bővebb lesz az értékkészlet (int). Duplán is alkalmazható (long long).

Az egész típusok az értékkészlet határain belüli minden egész értéket pontosan ábrázolnak.

Az egyes gépeken az egyes típusok mérete más-más lehet, de minden C megvalósításban teljesülnie kell a sizeof(short) ≤ sizeof(int) ≤ sizeof(long) ≤ sizeof(long long) relációnak.

A C nyelv különféle egész adattípusai az értékhalmazukban különböznek egymástól, az értelmezett műveletükben megegyeznek

Az egész adattípusokon általában az 5 matematikai alapműveletet és az értékadás műveletét értelmezzük, de C nyelven ennél jóval többet.

Értékadó művelet jobb oldalán álló kifejezés kiértékelése független attól, hogy a bal oldalon milyen típusú változó van.

A / művelet két egész értékre alkalmazva maradékos osztást jelent!

Tárolás:

n bites tárterületnek 2^n állapota van, vagyis egy n biten tárolt adattípusnak legfeljebb ennyi különböző értéke lehet.

Egész típusoknál a kettes komplemenst szokás használni, ha negatív értékek is szerepelhetnek az értékhalmazban.

Kettes komplemens:

- van egy pozitív számunk, és annak keressük a negatív párját
- a számot kettes számrendszerben felírjuk
- invertáljuk az összes bitet
- majd hozzáadunk a végén egyet
- a kapott szám lesz a szám ellentettje

Értékhalmaz mérete:

Ha negatív számok nem szerepelnek az értékhalmazban, akkor az értékhalmaz a [0 ... 2^n − 1] zárt intervallum. 
Ha az értékhalmazban negatív számok is szerepelnek, akkor az értékhalmaz a [−2^(n−1) ... 2^(n−1) − 1] zárt intervallum. 

Műveletei:

- bitenkénti
    - negáció
    - és
    - vagy
    - kizáró vagy
    - balra léptetés
    - jobbra léptetés

### Karakter típus

A char adattípus a C nyelv eleve definiált elemi adattípusa, értékkészlete 256 elemet tartalmaz.

A char adattípus egészként is használható, de alapvetően karakterek (betűk, számjegyek, írásjelek) tárolására való.

- Hogy melyik értékhez melyik karakter tartozik, az az alkalmazott kódtáblázattól függ.
- Bizonyos karakterek (általában a rendezés szerint első néhány) vezérlő karakternek számítanak, és nem megjeleníthetők.

Egy C programban karakter értékeket megadhatunk

- karakterkóddal számértékként, vagy
- aposztrófok közé írt karakterrel

A speciális karaktereket, illetve magát az aposztrófot (és végső soron tetszőleges karaktert is) escape-szekvenciákkal lehet megadni.
Az escape-szekvenciákat a \ (backslash) karakterrel kell kezdeni.

Konvertáljunk egy tetszőleges számjegy karaktert (ch) a neki megfelelő egész számmá és egy egyjegyű egészet (i) karakterré:

```
i = ch - '0';
ch = i + '0';
```

### Valós típusok

A C nyelvben a valós adattípusok a float és double.

A double adattípus az alábbi kulcsszóval módosítható:
    - long: Implementációfüggő módon 64, 80, 96 vagy 128 bites pontosságot megvalósító adattípus

A valós adattípusok az értékkészlet határain belül sem képesek minden valós értéket pontosan ábrázolni. Viszont az értékkészlet határain belüli minden a valós értéket képesek egy típusfüggő e relatív pontossággal ábrázolni, az a-hoz legközelebbi a típus által pontosan ábrázolható x valós értékkel.

- A C nyelv különféle valós adattípusai az értékhalmazukban különböznek egymástól, az értelmezett műveletükben megegyeznek.
- Valós kifejezésben bármely valós vagy egész típusú tényező (akár vegyesen többféle is) szerepelhet.
- Valós konstans típusa double, vagy a számleírásban megadott típus (f, l suffix).
- Értékadó művelet jobb oldalán álló kifejezés kiértékelése független attól, hogy a bal oldalon milyen típusú változó van.
- A típus pontatlansága miatt az == műveletet nagyon körültekintően kell használni!

Ábrázolása:

Egy valós értéket tároló memóriaterület három részre osztható: az előjelbitet, a törtet és az exponenciális kitevőt kódoló részre.

- Az előjelbit 0 értéke a pozitív, 1 értéke a negatív számokat jelöli
- A számot kettes számrendszerben 1.m × 2^k alakra hozzuk, majd az m számjegyeit eltároljuk a törtnek, a k-nak egy típusfüggő b konstanssal növelt értékét pedig a kitevőnek fenntartott részen.
- Így a tört rész hossza az ábrázolás pontosságát (az értékes számjegyek számát), a kitevő pedig az értéktartomány méretét határozza meg.
- Nagyon kicsi számokat speciálisan 0.m × 2^(1−b) alakban tárolhatunk, ekkor a kitevő összes bitje 0.
- Ha a kitevő összes bitje 1, az csupa 0 bitből álló tört esetén a ∞, minden más esetben NaN értéket jelenti.
- A 32/64 bites float/double az 1 előjelbit mögött 8/11 biten a kitevő b = 127-tel/1023-mal növelt értékét, majd 23/52 biten a törtet tárolja.


### Logikai típus

A C nyelvnek csak a C99 szabvány óta része a logikai (_Bool) típus (melynek értékkészlete a {0, 1} halmaz), de azért logikai értékek persze előtte is keletkeztek.

A műveletek eredményeként keletkező logikai hamis értéket a 0 egész érték reprezentálja, és a 0 egész érték logikai értékként értelmezve hamisat jelent.

A műveletek eredményeként keletkező logikai igaz értéket az 1 egész érték reprezentálja, de bármely 0-tól különböző egész érték logikai értékként értelmezve igazat jelent.

stdbool.h-ban definiált a bool típus és a true, false konstansok

Konstansként is definiálhatjuk, pl

```
#define TRUE 1
#define FALSE 0
```

## Az összetett adattípusok és a típusképzések, valamint megvalósításuk C nyelven. A pointer, a tömb, a rekord és az unió típus. Az egyes típusok szerepe, használata

### Összetett adattípusok, típusképzések

### Pointer típus

### Tömb típus

### Rekord típus

### Unió típus


