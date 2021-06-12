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

Részfeladatra bontás
Optimalizálás

A mohó algoritmus minden lépésben az aktuálisan optimálisnak tűnő megoldást választja.
Nem minden problémára adható mohó algoritmus!
    De ha igen, akkor az nagyon hatékony

Részproblémára bontáskor a cél: 
    a mohó választás egyetlen részproblémát eredményezzen, aminek az optimális
    megoldása a probléma optimális megoldása is egyben

Mohó algoritmusok helyessége:
- fogalmazzuk meg a feladatot úgy, hogy minden döntés hatására egy kisebb részprobléma keletkezzen
- bizonyítsuk be, hogy mindig van mohó választási lehetőség, tehát biztonságos
- mohó választással olyan részprobléma keletkezik, amihez hozzávéve a mohó választást, az eredeti probléma optimális megoldását kapjuk (optimális részstruktúrák)

Egy feladat optimális részstruktúrájú, ha a probléma egy opt. megoldása tartalmazza a részfeladatok optimális megoldásait is.

#### Példák

Hátizsák probléma

- adott egy hátizsák kapacitása, és n tárgy, mindegyik értékkel és súllyal megadva
- mekkora a legnagyobb összérték, amit a hátizsákba tehetünk?

Töredékes hátizsák probléma

- a tárgyak feldarabolhatók
- de minden tárgyból egy darab van

Mohó algoritmus a töredékes hátizsákra:

- számoljuk ki minden tárgyra az érték/súly arányt
- tegyük a hátizsákba a legnagyobb ilyen arányú tárgyat, az egészet ha belefér, vagy törjük, ha nem

### Rendező algoritmusok
input: n számból álló tömb\
output: bemenő tömb elemeinek olyan sorrendje, ahol minden következő elem nagyobbegyenlő az előzőnél\
fontossága: sok probléma triviális, ha rendezett a bemenet (pl bináris keresés, medián megállapítás)\
- Buborék rendezés
	- mindig 2 elemet vizsgálunk,úgy csúszik kerül a legkisebb elem az első helyre
- Beszúró rendezés
	- folyton haladunk előre a tömbben, az aktuális elemet beszúrjuk a megfelelő helyre
- Összefésülő rendezés
	- oszd meg és uralkodj
- Helyben rendezés
- Kupacrendezés
- Gyorsrendezés
- Leszámláló rendezés
- Számjegyes rendezés
- Edényrendezés

### Gráfalgoritmusok

#### Szélességi keresés
Feladat: Járjuk be az összes csúcsot ami egy s kezdő csúcsból elérhető.Mindeközben kiszámoljuk az elérhető csúcsok távolságát s-től

Bemenet: Irányítatlan vagy irányított G gráf és annak egy s csúcsa

Kimenet: Egy szótár, ami tartalmazza az s-ből elérhető csúcsokat és azok távolságát 

#### Mélységi keresés

Amikor egy megoldást megtalálni elégséges, nincs szükség mindre/optimálisra, pl. (ki)útkeresés

#### Minimális feszítőfák

##### Kruskal algoritmus

- Minden lépésben a legkisebb, két fát összekötő élt húzzuk be (egyesítjük egyetlen fává a két fát)
- Mohó algoritmus!

##### Prim algoritmus

- minden lépésben új csúcsot kötünk be a fába
- legolcsóbb éllel elérhető csúcsot választjuk
- Mohó algoritmus!
Sűrű gráfok esetén (sok él van) Prim előnyösebb, egyébként Kruskal

#### Legrövidebb utak (csúcsból kiindulva)

##### Dijkstra algoritmus

- azokat a csúcsokat tárolja amihez már megtalálta a legrövidebb utat
- minden lépésben egyel bővíti az elért csúcsok halmazát
- legkisebb legrövidebb úttal bíró csúcsot választja
- Mohó algoritmus!
- nem ad helyes megoldást negatív élsúlyok esetén

##### Bellman-Ford algoritmus

- negatív súlyok esetén is működik

##### Floyd-Warshall algoritmus (legrövidebb utak minden pontpárra)

- dinamikus programozás
- minden egyes lépésben egyre több csúcsot használhatunk
Ha nincsenek negatív élsúlyok és ritka a gráf akkor Dijsktra minden kezdőpontból O(VElogV)
Ha vannak negatív élsúlyok, de nincsenek negatív összköltségű körök vagy sűrű a gráf akkor Floyd-Warshall O(V3)
Ha negatív összköltésgű körök is lehetnek akkor Ford-Bellman minden kezdőcsúcsra O(V2E)
