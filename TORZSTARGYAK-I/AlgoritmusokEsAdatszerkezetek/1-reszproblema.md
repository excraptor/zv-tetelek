# Részproblémára bontó algoritmusok (mohó, oszd-meg-és-uralkodj, dinamikus programozás), rendező algoritmusok, gráfalgoritmusok (szélességi- és mélységi keresés, minimális feszítőfák, legrövidebb utak)

## Részproblémára bontó algoritmusok

### Oszd meg és uralkodj

- a feladatot több részfeladatra osztjuk
- a részfeladatok hasonlóak az eredeti feladathoz, de kisebbek
- rekurzívan megoldjuk a kisebb részfeladatokat
- a megoldásokat összevonjuk, és az adja a végső megoldást

Felosztás: hogyan osztjuk több részfeladatra

Uralkodás: a részfeladatokat rekurzív módon megoldjuk

Összevonás: a részfeladatok megoldásait összevonjuk

#### Példa

Felező-csúcskereső algoritmus

Input: egy számsorozat
Output: van-e benne csúcs?

Algoritmus: az *n* méretű sorozat helyett vizsgáljunk egy *(n-1)/2* méretűt, és ebben keressünk csúcsot,
    majd ezt folytatjuk rekurzívan

### Dinamikus programozás

#### Pénzváltási feladat

Input: *P_1, P_2, ... , P_n* típusú pénzérmék, *F* forint
Output: legkevesebb hány érmével fizethető ki pontosan *F* forint?

Dinamikus programozás akkor, ha a részproblémák nem függetlenek, hanem vannak közös részeik

Alapgondolat: a már megoldott részproblémák optimális megoldásait megjegyezzük

- így minden részproblémát csak egyszer fogunk megoldani
  
Pénzváltási feladat megoldása DP-vel: minden összegre *F*-ig kiszámoljuk, hogy azt minimum hány pénzérmével tudjuk kifizetni

- ötlet: minden érmére megnézzük, hogy a korábbi optimális megoldás a jó, amiben nem volt benne az az érme, vagy az, ha benne van az érme
- futásidő: *O(Fn)*

Iteratív megoldás: bottom-up építkezünk, és minden lehetséges értéket megnézünk
Rekurzív megoldás memorizálással: top-down építkezünk, és kulcs-érték párokat nézünk (csak akkor, ha nem kell minden részmegoldás)

### Mohó algoritmusok
