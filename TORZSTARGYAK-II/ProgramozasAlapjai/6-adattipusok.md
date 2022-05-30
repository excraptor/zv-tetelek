
# 6. Egyszerű adattípusok: egész, valós, logikai és karakter típusok és kifejezések. Az egyszerű típusok reprezentációja, számábrázolási tartományuk, pontosságuk, memória igényük és műveleteik. Az összetett adattípusok és a típusképzések, valamint megvalósításuk C nyelven. A pointer, a tömb, a rekord és az unió típus. Az egyes típusok szerepe, használata


## Egyszerű adattípusok: egész, valós, logikai és karakter típusok és kifejezések. Az egyszerű típusok reprezentációja, számábrázolási tartományuk, pontosságuk, memória igényük és műveleteik


==Az **adattípus** (gyakran röviden **típus**) az értékek egy halmazához rendelt név vagy címke és ezen halmaz értékein végrehajtható néhány művelet==

Az elemi adattípusok értékeit nem lehet önmagukban értelmes részekre bontani.

Ha a nyelv szintaktikája szerint a program egy adott pontján típusnak kellene következnie de az hiányzik, a fordító a típus helyére automatikusan int-et helyettesít.

### Egész típusok

A C nyelvben az egész típus az int.

Az **int** típus értékkészlete az alábbi kulcsszavakkal módosítható:

- **signed** (1 byte): A típus előjeles értékeket fog tartalmazni (int, char).
- **unsigned** (1 byte): A típus csak előjeltelen, nemnegatív értékeket fog tartalmazni (int, char).
- **short** (2 byte): Rövidebb helyen tárolódik, így kisebb lesz az értékkészlet (int).
- **long** (4 byte): Hosszabb helyen tárolódik, így bővebb lesz az értékkészlet (int). Duplán is alkalmazható **(long long, ami 8 byte)**.

Az egész típusok az értékkészlet határain belüli minden egész értéket pontosan ábrázolnak.

Az egyes gépeken az egyes típusok mérete más-más lehet, de minden C megvalósításban teljesülnie kell a ==sizeof(short) ≤ sizeof(int) ≤ sizeof(long) ≤ sizeof(long long)== relációnak.

A C nyelv különféle egész adattípusai az értékhalmazukban különböznek egymástól, az értelmezett műveletükben megegyeznek

Az egész adattípusokon általában az 5 matematikai alapműveletet és az értékadás műveletét értelmezzük, de C nyelven ennél jóval többet.

Értékadó művelet jobb oldalán álló kifejezés kiértékelése független attól, hogy a bal oldalon milyen típusú változó van.

**A / művelet két egész értékre alkalmazva maradékos osztást jelent!**

**Tárolás:**
n bites tárterületnek 2^n állapota van, vagyis egy n biten tárolt adattípusnak legfeljebb ennyi különböző értéke lehet.

**Egész típusoknál a kettes komplemenst** szokás használni, ha negatív értékek is szerepelhetnek az értékhalmazban.

**Kettes komplemens:**
- van egy pozitív számunk, és annak keressük a negatív párját
- a számot kettes számrendszerben felírjuk
- invertáljuk az összes bitet
- majd hozzáadunk a végén egyet
- a kapott szám lesz a szám ellentettje

**Értékhalmaz mérete:**
Ha negatív számok nem szerepelnek az értékhalmazban, akkor az értékhalmaz a [0 ... 2^n − 1] zárt intervallum. 
Ha az értékhalmazban negatív számok is szerepelnek, akkor az értékhalmaz a [−2^(n−1) ... 2^(n−1) − 1] zárt intervallum. 

**Műveletei:**
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

**Egy C programban karakter értékeket megadhatunk:**
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

A C nyelvben a valós adattípusok a **float** és **double**.

**A double** adattípus az alábbi kulcsszóval módosítható:
    - **long**: Implementációfüggő módon 64, 80, 96 vagy 128 bites pontosságot megvalósító adattípus

A valós adattípusok az értékkészlet határain belül sem képesek minden valós értéket pontosan ábrázolni. Viszont az értékkészlet határain belüli minden a valós értéket képesek egy típusfüggő e relatív pontossággal ábrázolni, az a-hoz legközelebbi a típus által pontosan ábrázolható x valós értékkel.

- A C nyelv különféle valós adattípusai az értékhalmazukban különböznek egymástól, az értelmezett műveletükben megegyeznek.
- Valós kifejezésben bármely valós vagy egész típusú tényező (akár vegyesen többféle is) szerepelhet.
- Valós konstans típusa double, vagy a számleírásban megadott típus (f, l suffix).
- Értékadó művelet jobb oldalán álló kifejezés kiértékelése független attól, hogy a bal oldalon milyen típusú változó van.
- A típus pontatlansága miatt az == műveletet nagyon körültekintően kell használni!

**Ábrázolása:**
Egy valós értéket tároló memóriaterület **három részre osztható:** az **előjelbitet**, a **törtet** és az **exponenciális kitevőt** kódoló részre.

- Az **előjelbit** 0 értéke a pozitív, 1 értéke a negatív számokat jelöli
- A számot kettes számrendszerben $1.m × 2^k$ alakra hozzuk, majd az $m$ **számjegyeit eltároljuk a törtnek**, a $k$-nak **egy típusfüggő $b$ konstanssal növelt értékét pedig a kitevőnek fenntartott részen.**
- Így a **tört rész hossza az ábrázolás pontosságát** (az értékes számjegyek számát), a **kitevő pedig az értéktartomány méretét** határozza meg.
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

Az összetett adattípusok értékei tovább bonthatóak, további értelmezésük lehetséges.

A C nyelv összetett adattípusai:

- **Pointer típus**
    - Függvény típus
- **Tömb típus**
    - Sztringek
- **Rekord típus**
    - Szorzat-rekord
    - Egyesítési-rekord

### Pointer típus

Az eddigi tárgyalásunkban szerepelt változók statikusak abban az értelemben, hogy létezésük annak a blokknak a végrehajtásához kötött, amelyben a változó deklarálva lett. A programozónak a deklaráció helyén túl nincs befolyása a változó létesítésére és megszüntetésére.

Az olyan változókat, amelyek a blokkok aktivizálásától függetlenül létesíthetők és megszüntethetők, dinamikus változóknak nevezzük.

Dinamikus változók megvalósításának általános eszköze a pointer típus.

Egy pointer típusú változó értéke (első megközelítésben) egy meghatározott típusú dinamikus változó.

Pointer típusú változót a * segítségével deklarálhatunk:

```
típus * változónév;
```

Az eddigiek során lényegében azonosítottuk a változóhivatkozást és a hivatkozott változót.

A dinamikus változók megértéséhez viszont világosan különbséget kell tennünk az alábbi három fogalom között:

- Változóhivatkozás
- Hivatkozott változó
- Változó értéke

A változóhivatkozás szintaktikus egység, meghatározott formai szabályok szerint képzett jelsorozat egy adott programnyelven, tehát egy kódrészlet.

A változó a program futása során a program által lefoglalt memóriaterület egy része, amelyen egy adott (elemi vagy összetett) típusú érték tárolódik.

Különböző változóhivatkozások hivatkozhatnak ugyanarra a változóra, illetve ugyanaz a változóhivatkozás a végrehajtás különböző időpontjaiban különböző változókra hivatkozhat.

Egy változóhivatkozáshoz nem biztos, hogy egy adott időben tartozik hivatkozott változó.

Műveletek:

- NULL
    - NULL, nem tartozik hozzá dinamikus változó
- Létesít
    - `x = malloc(sizeof(E))`
- Értékadás
    - `x = y`
- Törlés
    - `free(x)`
- Dereferencia: A pointer által mutatott dinamikus változó elérése, eredménye egy változóhivatkozás.
    - `*x`
- Egyenlő
    - `p == q`
- NemEgyenlő
    - `p != q`


**A memóriaműveletekhez szükség van az stdlib.h vagy a memory.h** használatára.

**malloc(S)**, lefoglal egy S méretű memóriaterületet
**sizeof(E)**, megmondja, hogy egy E típusú érték mekkora helyet igényel a memóriában
**malloc(sizeof(E))**, létrehoz egy E típusú érték tárolására is alkalmas változó
**free( p )**, felszabadítja a p-hez tartozó memóriaterületet, ezután a p-hez nem lesz érvényes változóhivatkozás 

Linux alatt logikailag minden programnak saját memória-tartománya van, amin belül az egyes memóriacímeket egy sorszám azonosítja.

**Pointer típusú változó** 32 bites rendszereken 4 bájt, 64 bites rendszereken 8 bájt hosszban a hozzá tartozó dinamikus változóhoz foglalt memóriamező kezdőcímét (sorszámát) tartalmazza.

A pointer értéke tehát (második megközelítésben) értelmezhető egy tetszőleges memóriacímként is, amely értelmezés egybeesik a pointer megvalósításával.

Ilyen módon viszont értelmezhetjük a címképző műveletet, ami egy változó memóriabeli pozícióját, címét adja vissza.

- **Cím**
    - `p = &x`

A void* egy speciális, úgynevezett típustalan pointer. Az ilyen típusú pointerek „csak” memóriacímek tárolására alkalmasak, a dereferencia művelet alkalmazása rájuk értelmetlen. Viszont minden típusú pointerrel kompatibilisek értékadás és összehasonlítás tekintetében.

### Tömb típus

Algoritmusok tervezésekor gyakran előfordul, hogy adatok sorozatával kell dolgozni, vagy mert az input adatok sorozatot alkotnak, vagy mert a feladat megoldásához kell.

Tegyük fel, hogy a sorozat rögzített elemszámú (n) és mindegyik komponensük egy megadott (elemi vagy összetett) típusból (E ) való érték.

Ekkor tehát egy olyan összetett adathalmazzal van dolgunk, amelynek egy eleme A = (a 0 , . . . , a n−1 ), ahol a i ∈ E , ∀i ∈ (0, . . . , n − 1)-re.

Ha az ilyen sorozatokon a következő műveleteket értelmezzük, akkor egy (absztrakt) adattípushoz jutunk, amit Tömb típusnak nevezünk.

Jelöljük ezt a Tömb típust T -vel, a 0, . . . , n − 1 intervallumot pedig I-vel.

**Műveletek**
- *Kiolvas*
    - a sorozat i. elemének kiolvasása egy változóba
- *Módosít*
    - a sorozat i. elemének módosítása egy E típusú értékre
- *Értékadás*
    - a változó felveszi a tömb értékét

Tömb típusú változót az alábbi módon deklarálhatunk:

```
típus változónév[elemszám];
```

Tömbelem hivatkozásra a `[]` operátort használjuk.

Ez egy olyan tömbökön értelmezett művelet C-ben, ami nagyon magas precedenciával rendelkezik és balasszociatív.

Egy tömbre a tömbindexelés operátort (megfelelő index használatával) alkalmazva a tömb adott elemét változóként kapjuk vissza.


### Rekord típus

A tömb típus nagyszámú, de ugyanazon típusú adat tárolására alkalmas.

Problémák megoldása során viszont gyakran előfordul, hogy különböző típusú, de logikailag összetartozó adatelemek együttesével kell dolgozni.

Az ilyen adatok tárolására szolgálnak a rekord típusok, ezek létrehozására pedig a rekord típusképzések.

Ha az egyes típusú adatokat egyszerre kell tudnunk tárolni, szorzat-rekordról beszélünk.

Az új adattípusra a T=Rekord(T 1 , . . . , T k ) jelölést használjuk és szorzat-rekordnak vagy struktúrának nevezzük.

- kiolvas
- módosít
- értékadás

```
typedef struct T {
    T1 M1;
    ...
    Tk Mk;
} T;
```

A fenti típusképzésben az M1,. . . ,Mk azonosítókat mezőazonosítóknak (tagnak, member-nek) hívjuk és lokálisak a típusképzésre nézve.

Az absztrakt típus műveletei mezőhivatkozások segítségével valósíthatóak meg.

A mezőhivatkozásra a . operátort használjuk. Ez egy olyan rekordokon értelmezett művelet C-ben, ami nagyon magas precedenciával rendelkezik és balasszociatív.

Egy rekordra a mezőkiválasztás operátort (megfelelő mezőnévvel) alkalmazva a rekord mezőjét változóként kapjuk vissza.



### Unió típus

Ha az egyes típusú adatokat nem kell egyszerre tárolni, egyesített-rekordról beszélünk

A T halmazon is a szorzat rekordhoz hasonló módon értelmezhetünk kiolvasó és módosító műveletet.

Az új adattípust a T 0 változati típusból és T 1 , . . . , T k egyesítési-tag típusokból képzett egyesített-rekord típusnak nevezzük.

```
typedef union T {
    T1 M1;
    ...
    Tk Mk;
} T;
```

A union típusú változó számára foglalt memória mérete, amely a
sizeof függvénnyel lekérdezhető:
```
sizeof(T) = max{sizeof(T1), ..., sizeof(Tk)}
```

Valamennyi változati mező ugyanazon a memóriacímen kezdődik, ami
megegyezik a teljes union típusú érték címével (azaz minden mező
eltolása, offset-je 0).


### Union vs Struct

|                | Struct                                        | Union                                     |
|----------------|-----------------------------------------------|-------------------------------------------|
| **Méret**          | A tagok elemei méretének az összege           | A legnagyobb elemnek a mérete             |
| **Memória**        | Minden tagnak van külön memória részlete      | A memórián osztoznak                      |
| **Tagok elérése**  | Bármelyik tagot el lehet érni bármikor        | Egyszerre csak egy tagot lehet egy időben |
| **Inicializálása** | Bármennyi tagot lehet inicializálni egyszerre | Csak az első tagot tudjuk inicializálni.  
