# 13. LP alapfeladat, példa, szimplex algoritmus, az LP geometriája, generálóelem választási szabályok, kétfázisú szimplex módszer, speciális esetek (ciklizáció-degeneráció, nem korlátos feladat, nincs lehetséges megoldás)

## LP alapfeladat

@kép

LP alapfeladat: Keressük adott lineáris célfüggvény szélsőértékét, értelmezési tartományának adott lineáris korlátokkal meghatározott részében.
Lehetséges megoldás: olyan p vektor, hogy p-t behelyettesítve x-be kielégíti a feladat feltételrendszerét.
Lehetséges megoldási tartomány: az összes lehetséges megoldás halmaza.
Optimális megoldás: egy olyan lehetséges megoldás, ahol a célfüggvény felveszi a maximumát/minimumát.

Példa: 
@kép

## Szimplex algoritmus

Ahhoz, hogy lecseréljük az egyenlőtlenségeket egyenlőségekre az LP alapfeladatban, adjunk hozzá minden egyenlőtlenség bal oldalához egy mesterséges változót.

Ezután fejezzük ki a mesterséges változókat az egyenlet átrendezésével.

A kapott egyenletrendszert hívjuk *szótár alak*nak.

Természetes változók: az eredeti változók
Mesterséges változók: az újonan felvett nemnegatív változók
Bázisváltozók: a szótár alakban bal oldalt álló változók
Nembázis változók: a szótár alakban jobb oldalt álló változók
Szótár bázismegoldása: olyan x vektor, amelyben a szótár nembázis változóinak értéke nulla, így a bázisváltozók értéke a jobboldali konstans lesz
Lehetséges (fizibilis) bázismegoldás: olyan bázismegoldás, ami egyben lehetséges megoldás is

A szimplex algoritmus:

- iteratív optimum keresés
- ismételt áttérés más szótárakra, a következő feltételek betartása mellett:
    - minden iteráció szótára ekvivalens az őt megelőzőével
    - minden iteráció bázismegoldásán a célfüggvény értéke nagyobb vagy egyenlő, mint az előző iterációban
    - minden iteráció bázismegoldása lehetséges megoldás

Mi alapján térjünk át másik szótárra?
Hogyan térjünk át, hogy a feltételek teljesüljenek?
Honnan tudjuk, ha az aktuális bázismegoldás optimális?
Létezik-e minden LP feladatnak optimuma?

Pivot lépés: új szótár megadása egy bázis és nembázis változó szerepének felcserélésével
Belépőváltozó: az a nembázis változó, ami a következő szótárra áttéréskor bázisváltozóvá válik
Kilépő változó: az a bázisváltozó, ami a köv. szótárra áttéréskor nembázissá válik
Szótárak ekvivalenciája: két szótár ekvivalens, ha az általuk leírt egyenletrendszer összes lehetséges megoldása és a hozzájuk tartozó célfüggvényértekek rendre megegyeznek

Pivot lépés előtti és utáni szótárak ekvivalensek.

SZIMPLEX:

- ha adott szótárban minden célfüggvény együttható negatív, akkor az aktuális bázismegoldás optimális
- ha nem, válasszuk a nembázis változók közül belépőváltozónak valamely k.-at, amelyre a k. célfüggvény együttható pozitív
- ha ennek a változónak minden egyenletben az együtthatója negatív, a feladat nem korlátos, megállunk
- ha nem, akkor válasszuk az l. pozitív együtthatót, amelyre a konstans/együttható abszolút értéke minimális
- hajtsunk végre egy pivot lépést úgy, hogy xk legyen a belépőváltozó, és az l. feltétel bázisváltozója legyen a kilépő változó

## Generálóelem választási szabályok

Klasszikus szimplex pivot szabály:

- a lehetséges belépőváltozók közül válasszuk a legnagyobb c_k értékűt, több ilyen esetén a legkisebb indexűt
- a lehetséges kilépőváltozók közül válasszuk a legkisebb l indexű egyenlet változóját

Bland szabály

- a lehetséges belépőváltozók közül válasszuk a legkisebb indexűt
- a lehetséges változók közül válasszuk a legkisebb indexűt

Legnagyobb növekmény


Lexikografikus szabály

- kiegészítjük epszilonokkal mesterségesen a szótárat
- a lehetséges belépőváltozók közül a legnagyobb c_k értékűt válasszuk, több ilyennél a legkisebb indexűt
- a lehetséges kilépőváltozók közül azt, amelynek l indexű egyenletére az együtthatókból álló vektor lexikografikusan a legkisebb

Véletlen pivot

- 1 valószínűséggel terminál

## Az lp geometriája

Ábrázolhatjuk pl a lehetséges megoldások halmazát koordináta rendszerben, két változó esetén.

Minden feltétel egy egyenest határoz meg, ezeket berajzoljuk.
Ezzel valamilyen sokszöget kapunk meg, ennek a sokszögnek a csúcsainak a koordinátái lesznek a lehetséges megoldások.

## Kétfázisú szimplex módszer

Ha minden konstans nemnegatív az LP feladatban, akkor mehet a szimplex

De mi van, ha vannak negatív konstansok is?

Vegyünk egy segédfeladatot

- bevezetünk egy új, x0 segédváltozót
- legyen w az új célfüggvény, w=-x0
- térjünk át szótár alakra
- vegyük a legnegatívabb jobboldalú egyenletet, és ebből fejezzük ki x0-t
- a többiből a mesterséges változókat
- ezután már egy lehetséges indulószótárat kapunk

A standard feladatnak csak akkor létezik lehetséges megoldása, ha w=0 a hozzá felírt segédfeladat optimuma.

Ha a segédfeladatot megoldjuk a szimplexszel, és annak optimuma 0, akkor a megoldás utolsó szótárából könynen felírhatunk egy olyan szótárat, amely az eredeti feladat szótára, és bázismegoldása lehetséges megoldás is egyben.

A szótár felírásának lépései:

- az x0 = 0 feltételt elhagyjuk
- ha x0 bázisváltozó, akkor az egyenletének jobb oldalán lévő nem 0 együtthatójú változók egyikével végrehajtunk egy pivot lépést
- elhagyjuk x0 megmaradt erőforrásait
- a célfüggvény egyenletét lecseréljük az eredeti célfüggvényre, amit átírunk az aktuális bázisváltozóknak megfelelően

A következő fázisban pedig az átírt szótáron futtatjuk a szimplex algoritmust

## Speciális esetek

### Ciklizáció

Degenerált iterációs lépés: olyan szimplex iteráció, amelyben nem változik a bázismegoldás
Degenerált bázismegoldás: olyan bázismegoldás, amelyben egy vagy több bázisváltozó értéke is 0

Ciklizáció: ha a szimplex algoritmus valamely iterációja után egy korábbi szótárat visszakapunk, akkor az a ciklizáció

Ha a szimplex algoritmus nem áll meg, akkor ciklizál!
A ciklizáció elkerülhető megfelelő pivot szabály alkalmazásával (lexikografikus, Bland szabály)
A ciklizáció oka a degeneráció, azaz a bázisváltozók 0-vá válása a bázismegoldásban

### Nem korlátos 

Ha az LP feladat maximalizálandó/minimalizálandó, és a célfüggvénye tetszőlegesen nagy/kicsi értéket felvehet, akkor nem korlátos a feladat.

### Nincs lehetséges megoldás

Ha a standard alakú LP feladatot kétfázisú szimplex módszerrel oldjuk meg, az első fázis eldönti, hogy van-e lehetséges megoldás.

Ha a felírt segédfeladatban az optimum értéke kisebb, mint nulla, akkor nincs lehetséges megoldás, ha 0, akkor van.