# Részproblémára bontó algoritmusok (mohó, oszd-meg-és-uralkodj, dinamikus programozás), rendező algoritmusok, gráfalgoritmusok (szélességi- és mélységi keresés, minimális feszítőfák, legrövidebb utak)

## Részproblémára bontó algoritmusok

### Oszd meg és uralkodj

1. **Felosztás:** a feladatot több részfeladatra osztjuk, a részfeladatok hasonlóak az eredeti feladathoz, de kisebbek
2. **Uralkodás:** rekurzívan megoldjuk a kisebb részfeladatokat.
3. **Összevonás:** a részfeladatok megoldásait összevonjuk, és az adja a végső megoldást.

#### Példa
Felező-csúcskereső algoritmus

**Input:** egy számsorozat
**Output:** van-e benne csúcs?

Algoritmus: az *n* méretű sorozat helyett vizsgáljunk egy *(n-1)/2* méretűt, és ebben keressünk csúcsot,
    majd ezt folytatjuk rekurzívan

### Dinamikus programozás

**Alapgondolat**: Mi lenne, ha a már  megoldott részproblémákat nem számolnánk ki újra  
minden egyes alkalommal ⇒ eltároljuk a részproblémák megoldásait. ==Idő tárra cseré-  
lése==
- Dinamikus programozás akkor, ha a részproblémák nem függetlenek, hanem vannak közös részeik
- így minden részproblémát csak egyszer fogunk megoldani

**Iteratív megoldás**: bottom-up építkezünk, és minden lehetséges értéket megnézünk
**Rekurzív megoldás memorizálással**: top-down építkezünk, és kulcs-érték párokat nézünk (csak akkor, ha nem kell minden részmegoldás)

Pénzváltás probléma
**Input:** *P_1, P_2, ... , P_n* típusú pénzérmék, *F* forint
**Output:** legkevesebb hány érmével fizethető ki pontosan *F* forint?
  
Pénzváltási feladat megoldása DP-vel: minden összegre *F*-ig kiszámoljuk, hogy azt minimum hány pénzérmével tudjuk kifizetni

- ötlet: minden érmére megnézzük, hogy a korábbi optimális megoldás a jó, amiben nem volt benne az az érme, vagy az, ha benne van az érme
- futásidő: *O(Fn)*

### Mohó algoritmusok

A mohó algoritmusok **lokálisan** legjobb döntést hozzák, de ==NEM mindig optimális== meg-  
oldás az egész feladatra. Viszont, ha adható ilyen algoritmus akkor rendkívűl hatékony.  
Két tulajdonság, ha megadható ilyen algoritmus:  
1.  **Optimális részstruktúra**: A részfeladatok is optimális megoldást adnak.  
2.  **Mohó választás**:  Lokálisan optimális választások a globális optimális megoldás-  
hoz vezetnek


**Mohó algoritmusok helyessége:**
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
fontossága: sok probléma triviális, ha rendezett a bemenet (pl bináris keresés, medián megállapítás)
**Stabilitás:** hogy az azonosnak ítélt elemek közötti sorrendet megőrzi-e.
- Buborék rendezés
	- Elve, hogy egy „buborékkal” haladva a tömbben több menetben elölről hátra a buborékban szereplő két elemet felcseréljük, ha azok rossz sorrendben vannak. **Stabil rendezés.**
	- Átlagos eset: $\mathcal{O}(n^2)$
	- Legrosszabb eset: $\mathcal{O}(n^2)$
	- Tárigénye: $\mathcal{O}(1)$
- Beszúró rendezés
	- folyton haladunk előre a tömbben, az aktuális elemet beszúrjuk a megfelelő helyre. **Stabil rendezés.**
	- Átlagos eset: $\mathcal{O}(n^2)$
	- Legrosszabb eset: $\mathcal{O}(n^2)$
	- Tárigénye: $\mathcal{O}(1)$
- Összefésülő rendezés
	- oszd meg és uralkodj: Felbontjuk elemi részekre a tömböt, majd végighaladva összefésüljük őket megfelelő sorrendbe. **Stabil rendezés.**
	- Átlagos eset: $\mathcal{O}(n*logn)$
	- Legrosszabb eset: $\mathcal{O}(n*logn)$
	- Tárigénye: $\mathcal{O}(n)$ vagy ha láncolt lista akkor $\mathcal{O}(1)$ 
- Gyorsrendezés:
	- Rekurzív algoritmus, kettéosztja a rendezendő listát egy kiemelt elemnél kisebb és nagyobb elemekre, majd a részekre külön-külön alkalmazza a gyorsrendezést. **Nem stabil rendezés**
	- **Átlagos eset:** $\mathcal{O}(n log n)$
	- **Legrosszabb eset:** $\mathcal{O}(n^2)$
	- **Tárigénye:** $\mathcal{O}(logn)$
- Leszámláló rendezés
- Helyben rendezés
- Kupacrendezés
- Számjegyes rendezés
- Edényrendezés

### Gráfalgoritmusok

#### Szélességi keresés
Feladat: Járjuk be az összes csúcsot ami egy **s** kezdő csúcsból elérhető. Mindeközben kiszámoljuk az elérhető csúcsok távolságát **s**-től

**Bemenet:** Irányítatlan vagy irányított G gráf és annak egy s csúcsa

**Kimenet:** Egy szótár, ami tartalmazza az **s**-ből elérhető csúcsokat és azok távolságát 

**Idő- és térkomplexitás:**
Ha $|V|$ a csúcsok és $|E|$ a gráf éleinek száma akkor,
**Időigénye:** $\mathcal{O}(|V|+|E|)$
**Tárigénye:** $\mathcal{O}(|V|)$


#### Mélységi keresés

Amikor egy megoldást megtalálni elégséges, nincs szükség mindre/optimálisra, pl. (ki)útkeresés
Gyökércsúcsból indulva az útkeresés/bejárás során balra lefelé tartva járja be. Ha nem tud sehova lefelé menni tovább, akkor visszalép a legalsó elágazásig és a következő utat választja.

**Idő- és térkomplexitás:**
Ha $|V|$ a csúcsok és $|E|$ a gráf éleinek száma akkor,
**Időigénye:**  $\mathcal{O}(|V|+|E|)$
**Tárigénye:** $\mathcal{O}(|V|)$
#### Minimális feszítőfák

##### Kruskal algoritmus

- Minden lépésben a legkisebb, két fát összekötő élt húzzuk be (egyesítjük egyetlen fává a két fát)
- Ha a gráf összefüggő, akkor **minimális feszitőfa megalkotására** szolgál, AMÚGY meg **minimális feszitőerdőt** hoz létre.
- **Mohó algoritmus!**
- **Algoritmus:**
	- Éleket súlyok szerint növekvőbe rendezzük
	- Ezeket megvizsgáljuk, hogy melyeket vegyük be
	- Gráfok csúcsa halmazt alkot, és csak akkor kerülnek be, ha két végpontja különböző halmazban van $\rightarrow$ halmazegyesítés.

##### Prim algoritmus

Összefüggő súlyozott gráf minimális feszítőfáját határozza meg.
- minden lépésben új csúcsot kötünk be a fába
- legolcsóbb éllel elérhető csúcsot választjuk
- **Mohó algoritmus!**
Sűrű gráfok esetén (sok él van) Prim előnyösebb, egyébként Kruskal.

#### Legrövidebb utak (csúcsból kiindulva)

##### Dijkstra algoritmus

- azokat a csúcsokat tárolja amihez már megtalálta a legrövidebb utat
- minden lépésben egyel bővíti az elért csúcsok halmazát
- legkisebb legrövidebb úttal bíró csúcsot választja
- **Mohó algoritmus!**
- nem ad helyes megoldást negatív élsúlyok esetén (beragadhat).
- **Időigény:** $\mathcal{O}(|E|+|V|*log|V|)$

##### Bellman-Ford algoritmus

- negatív súlyok esetén is működik
- **Időigény:** $\mathcal{O}(|V|*|E|)$
##### Floyd-Warshall algoritmus (legrövidebb utak minden pontpárra)

- dinamikus programozás
- minden egyes lépésben egyre több csúcsot használhatunk
-  **Időigény:** $\mathcal{O}(|V|^3)$


1. Ha nincsenek negatív élsúlyok és ritka a gráf akkor **Dijsktra**
2. Ha vannak negatív élsúlyok, de nincsenek negatív összköltségű körök vagy sűrű a gráf akkor **Floyd-Warshall**
3. Ha negatív összköltésgű körök is lehetnek akkor **Ford-Bellman**
