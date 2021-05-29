# 11. Keresési feladat: feladatreprezentáció, vak keresés, informált keresés, heurisztikák. Kétszemélyes zéró összegű játékok: minimax, alfa-béta eljárás. Korlátozás kielégítési feladat

## Keresési feladat: feladatreprezentáció, vak keresés, informált keresés, heurisztikák

### Feladatreprezentáció

Tekintsünk egy diszkrét, statikus, determinisztikus és teljesen megfigyelhető feladatkörnyezetet. Tegyük fel, hogy a világ tökéletesen modellezhető a következőkkel:

- lehetséges állapotok halmaza
- egy kezdőállapot
- lehetséges cselekvések halmaza (állapotátmenet függvény, minden állapothoz hozzárendelünk egy (cselekvés, állapot) rendezett párokból álló halmazt, tehát egy állapotban milyen cselekvések hatására milyen állapotba juthat az ágensünk)
- állapotátmenet költségfüggvénye, minden lehetséges állapot-cselekvés-állapot hármashoz hozzárendelünk egy költséget, azaz egy állapotból egy (másik) állapotba jutásnak mekkora a költsége
- célállapotok halmaza, tehát hova szeretnénk, hogy eljusson az ágensünk

Ez egy súlyozott gráfot definiál, ez a gráf az állapottér

Feltesszük továbbá, hogy az állapotok száma véges, vagy megszámlálható. Úton állapotok cselekvésekkel összekötött sorozatát értjük, ennek van egy összköltsége is.

### Vak (informálatlan) keresés

#### Fakeresés

Adott kezdőállapotból találjunk minimális költségű utat egy célállapotba. Az állapottér nem mindig adott explicit módon, és végtelen is lehet.

Ötlet: keresőfa építése, a kezdőállapotból növesszünk fát a szomszédos állapotok hozzávételével, amíg célállapotot nem találunk. 
A keresőfa NEM azonos a feladat állapotterével, pl ha van két csúcs között oda-vissza él.

fakeresés
1 perem = { újcsúcs(kezdőállapot) }
2 while perem.nemüres()
3 csúcs = perem.elsőkivesz()
4 if csúcs.célállapot() return csúcs
5 perem.beszúr(csúcs.kiterjeszt())
6 return failure

A csúcs.kiterjeszt() létrehozza a csúcsból elérhető összes állapotból a keresőfa csúcsot. 
A perem egy prioritási sor, ettől függ a bejárási stratégia. 

A hatékonyságot növelhetjük, ha úgy szúrunk be csúcsokat a perembe, hogy abban az esetben, ha a peremben található már ugyanazzal az állapottal egy másik csúcs, akkor ha az új csúcs költsége kisebb, lecseréljük a régi csúcsot az újra, különben nem tesszük bele az újat.

#### Szélességi keresés

Fakeresés, ahol a perem egy FIFO perem.

- Teljes, minden, véges számú állapot érintésével elérhető állapotot véges időben elér
- Általában nem optimális, de pl akkor igen, ha a költség a mélység nem csökkenő függvénye
- időigény = tárigény O(b^{d+1})
    - b: szomszédok maximális száma
    - d: a legkisebb mélységű célállapot mélysége

#### Mélységi keresés

Fakeresés, LIFO perem

- Teljes, ha a keresési fa véges mélységű
- Nem optimális
- Időigény: legrosszabb esetben O(b^m) (nagyon rossz, lehet végtelen), tárigény legrosszabb esetben O(bm) (ez egész bíztató)

#### Iteratívan mélyülő keresés

Mélységi keresések sorozata 1, 2, 3 stb méylségre korlátozva, amíg célállapotot nem találunk.

- Teljesség és optimalitás a szélességivel egyezik meg
- időigény = O(b^d) (akár jobb is lehet, mint a szélességi), tárigény = O(bd) (jobb, mint a mélységi)

Ez a legjobb informálatlan kereső.

#### Egyenletes költségű keresés

A peremben a rendezés költség alapú, mindig először a legkisebb útköltségű csúcsot terjesztjük ki.

- Teljes és optimális, ha minden él költsége nagyobb mint nulla
- Idő és tárigény nagyban függ a költségfüggvénytől

#### Gráfkeresés

Ha nem fa az állapottér!

Fakeresés, de a perem mellett még tárolunk egy ún. zárt halmazt is. A zárt halmazba azok a csúcsok kerülnek, amiket már kiterjesztettünk. A perembe helyezés előtt minden csúcsra megnézzük, hogy már a zárt halmazban van-e. Ha igen, nem tesszük a perembe. Másrészt minden peremből kivett csúcsot a zárt halmazba teszünk. Így minden állapothoz a legelső megtalált út lesz tárolva.

## Informált keresés, heurisztikák

Itt már tudjuk, hogy "hova megyünk".

Heurisztika: minden állapotból megbecsüli, hogy mekkora az optimális út költsége az adott állapotból egy célállapotba: tehát értelmesebben tudunk következő szomszédot választani. Pl. légvonalbeli távolság a célig a térképen egy útvonal-tervezési problémához jó heurisztika.

h(n): optimális költség közelítése a legközelebbi célállapotba
g(n): tényleges költség a kezdőállapotból a jelenlegi állapotba

### Mohó

Fakeresés, peremben a rendezést h() alapján csináljuk, mindig a legkisebb értékű csúcsot vesszük ki.

- Teljes, de csak ha a keresési fa véges mélységű
- Nem optimális
- időigény, tárigény O(b^m)

### A*

A peremben a rendezést f()=h()+g() alapján végezzük, a legkisebb csúcsot vesszük ki. f() a teljes út költségét becsüli a kezdőállapotból a végállapotba. Ha h = 0, és gráfkeresést alkalmazunk, akkor a Dijkstra-t kapjuk.

Egy h heurisztika elfogadható, ha nem ad nagyobb értéket, mint a tényleges optimális érték.
Fakeresést feltételezve, ha h elfogadható és a keresési fa véges, akkor A* optimális.

Egy h heurisztika konzisztens, ha h(n) <= mint a valódi költség n egyik bármely, plusz a szomszéd heurisztikája.
Gráfkeresést feltételezve, ha h konzisztens és az állapottér véges, akkor A* optimális.

Az A* optimálisan hatékony, de a tárigénye általában exponenciális, és nagyon nagyban függ h-tól. Az időigény szintén nagyon nagyban függ h-tól.

### Heurisztikák

A relaxált probléma optimális megoldása pl jó heurisztika lehet.

Relaxált probléma: elhagyunk feltételeket az eredeti problémából.
Kombinálhatunk több heurisztikát is.
Készíthetünk mintaadatbázisokat, ahol részproblémák egzakt költségét tároljuk.


## Kétszemélyes zeró összegű játékok: miminax, alfa-béta eljárás

### Kétszemélyes, lépésváltásos, determinisztikus, zéró összegű játék

- lehetséges állapotok halmaza
- egy kezdőállapot
- lehetséges cselekvések halmaza, és egy állapotátmenet függvény
- célállapotok
- hasznosságfüggvény


Két ágens van, felváltva lépnek. Az egyik maximalizálni akarja a hasznosságfüggvényt (MAX játékos), a másik minimalizálni (MIN játékos).
Konvenció szerint MAX kezd. Az első célállapot elérésekor a játéknak definíció szerint vége.

Zéró összegű játék: A MIN játékos minimalizálja a hasznosságot, ami ugyanaz, mint maximalizálni a negatív hasznosságot. Ez a negamax formalizmus. Itt a két játékos nyereségének az összege a végállapotban mindig nulla, innen a zéró összegű elnevezés.

### Minimax algoritmus, alfa-béta vágás

Mindkét játékos ismeri a teljes játékgráfot, bármilyen komplex számítást képes elvégezni és nem hibázik (tökéletes racionalitás). A minimax algoritmus alapján lehet megvalósítani a legjobb stratégiát tökéletes racionalitás esetén.

Minimax:

maxÉrték(n)
1 if végállapot(n) return hasznosság(n)
2 max = -végtelen
3 for a in n szomszédai
4 max = max(max, minÉrték(a))
5 return max

minÉrték(n)
1 if végállapot(n) return hasznosság(n)
2 min = +végtelen
3 for a in n szomszédai
4 min = min(min, maxÉrték(a))
5 return min

Ha n végállapot, visszaadja a hasznosságát. Különben a max-nál n szomszédaira kiszámolja a maximális értéket, ami vagy az aktuális maximum, vagy nézi, hogy a másik játékos mit lépne. 
Csak elméleti jelentőségű, a minimax algoritmus nem skálázódik. Az összes lehetséges állapot kiszámolása rettentő sok idő lenne pl sakknál.

Alfa-béta vágás

Ha tudjuk, hogy pl MAX-nak már van egy olyan stratégiája, ahol biztosan egy 10 értékű hasznosságot el tud érni az adott csúcsban, akkor a csúcs további kiértékelésekor nem kell vizsgálni olyan csúcsokat, ahol MIN ki tud kényszeríteni <= 10 hasznosságot, mert ennél már MAX-nak van jobb stratégiája

minÉrték és maxÉrték hívásakor átadjuk az alfa és béta paramétereket is a függvénynek.

Alfa jeletése: MAXnak már felfedeztünk egy olyan stratégiát, amely alfa hasznosságot biztosít, ha ennél kisebbet találnánk, azt nem vizsgáljuk
Béta jelentése: MINnek már felfedeztünk egy olyan stratégiát, amely béta hasznosságot biztosít, ha ennél nagyobbat találnánk, azt nem vizsgáljuk

A gyakorlatban a minimax és az alfa-béta vágásos algoritmusokat is csak meghatározott mélységig vizsgáljuk, illetvve heurisztikákat is alkalmazhatunk. A csúcsok bejárási sorrendje is nagyon fontos, mert pl alfa béta vágásnál egy jó rendezés mellett nagyon sok csúcsot vághatunk le.

## Korlátozás kielégítési feladat

A feladat az állapottérrel adott keresési problémák és az optimalizálási problémák jellemzőit ötvözi. Az állapotok és célállapotok speciális alakúak.

Lehetséges állapotok halmaza: a feladat állapotai az n db változó lehetséges kombinációi
Célállapotok: a megengedett állapotok, adottak különböző korlátozások, és azok az állapotok a célállapotok, amik minden korlátozást kielégítenek.

Az út a megoldásig lényegtelen, és gyakran célfüggvény is értelmezve van az állapotok felett, ilyenkor egy optimális célállapot megtalálása a cél. 