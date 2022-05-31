
# 13. LP alapfeladat, példa, szimplex algoritmus, az LP geometriája, generálóelem választási szabályok, kétfázisú szimplex módszer, speciális esetek (ciklizáció-degeneráció, nem korlátos feladat, nincs lehetséges megoldás)

## LP alapfeladat

@kép (LP_alapfeladat.JPG)

**LP alapfeladat:** Keressük adott lineáris célfüggvény, $\mathbb{R}^n$ értelmezési tartományú függvény szélsőértékét, értelmezési tartományának adott lineáris korlátokkal meghatározott részében.

**Lehetséges megoldás:** olyan $p$ vektor, hogy $p$-t behelyettesítve $x$-be kielégíti a feladat feltételrendszerét.

**Lehetséges megoldási tartomány:** az összes lehetséges megoldás (vektor) halmaza.

**Optimális megoldás:** egy olyan lehetséges megoldás, ahol a célfüggvény felveszi a maximumát/minimumát.

### LP felírása + példa
1. Válasszuk meg a **döntési változókat** ($x_1, x_2,...$)
2. Határozzuk meg a célt és a **célfüggvényt** (max/min pl: max $2x_1+5x_2$)
3. Írjuk fel a **korlátozó feltételeket**(lineáris egyenlötlenségek pl: $2x_1+5x_2 \ge 10$)
4. Határozzuk meg a **változók értelmezési tartományát** (előjel feltételek $x_1 \ge 0$) 

Példa:

Egy cég **Tardisokat** és **Dalekeket** akar árulni. A **Tardis** darabja 25 euró míg a **Dalek** darabja 20 euró protifot jövedelmez.
A következő két héten a termék összerakására **200 munkaóra** áll rendelkezésre. Tardis és a Dalek is 5óra/db.
A **Dalekhez** szükség van egy **speciális lézerhabverőre**, amiből csak **24 darab** van raktáron.
A cég raktározási helye **320 négyzetméter**, amiből a Tardis **10 négyzetmétert** a Dalek **5 négyzetmétert** foglal el.
A cég **maximalizálni** szeretne

1. $x1$ az összeszerelendő Tardisok száma, $x_2$ az összeszerelendő Dalekek száma.
2. **Célfüggvény felírása**
	- Tudjuk, hogy maximalizálni akar a cég, és tudjuk mennyi 1 darab Tardis és Dalek profitja. 
	- Tehát $25x_1 + 20x_2 = z$
3. **Korlátozó feltételek:** 
	- **Összeszerelés időigénye**: Mivel mindkettő összeszerelése 5 óra és csak 200 óra áll rendelkezésre ezért:
		- $5x_1+5x_2 \le 200$
	- **A dalek lézerhabverője is fontos**, amiből 24 darab van
		- $x_2 \le 24$ 
	 - **Raktározási feltétel is fontos**, Tardis: 10m^2 Dalek: 5m^2 és csak 320m^2 áll rendelkezésre.
		 - $10x_1 + 5x_2 \le 320$

Tehát: 
max $z = 25x_1 +20x_2$
$5x_1+5x_2 \le 200$
$x_2 \le 24$ 
$10x_1 + 5x_2 \le 320$
$x_1, x_2 \ge 0$


## Az LP geometriája

Ábrázolhatjuk pl. a lehetséges megoldások halmazát koordináta rendszerben, két változó esetén.

Minden feltétel egy egyenest határoz meg, ezeket berajzoljuk.
Ezzel valamilyen sokszöget kapunk meg, ennek a sokszögnek a csúcsainak a koordinátái lesznek a lehetséges megoldások.
@kép (LP_Geometria_1.JPG és LP_Geometria_2.JPG)

## Szimplex algoritmus

Ahhoz, hogy lecseréljük az **egyenlőtlenségeket egyenlőségekre** az LP alapfeladatban, adjunk hozzá minden egyenlőtlenség bal oldalához egy **mesterséges változót.**

Ezután **fejezzük ki a mesterséges változókat az egyenlet átrendezésével.**

A kapott egyenletrendszert hívjuk **szótár alak** nak.

**Terminológia**
- **Természetes (vagy döntési) változók:** Standard alakú feladatban szereplő változók ($x_1,x_2,..,x_n$)
- **Mesterséges változók:** A szótár felírásakor felvett új nemnegatív változók ($x_{n+1},...,x_{n+m}$)
- **Bázisváltozók**: A szótár feltétel egyenleteinek a bal oldalán álló változók
- **Nembázis változók:** A szótár jobb oldalán álló változók.
- **Szótár bázismegoldása:** Olyan $x$ vektor, amelyben a nembázis változók értéke 0, ezért a bázisváltozók értékei az öket tartalmazó egyenletek jobb oldali konstansai.
- **Lehetséges megoldás:** Olyan bázismegoldás, ami egyben lehetséges megoldás is, azaz a szótárra teljesül, hogy $b_i \ge 0$


**A szimplex algoritmus:**

- iteratív optimum keresés
- ismételt áttérés más szótárakra, a következő feltételek betartása mellett:
    - minden iteráció szótára ekvivalens az őt megelőzőével
    - minden iteráció bázismegoldásán a célfüggvény értéke nagyobb vagy egyenlő, mint az előző iterációban
    - minden iteráció bázismegoldása lehetséges megoldás

**Szimplex algoritmus menete:**
1. A szótárban $c_j \le 0$ minden $j = 1,2,..,n$-re?
	- Igen: Az aktuális bázismegoldás **optimális**
	- Nem: Folytatás 2. ponttal
2. Válasszuk a nembázis változók közül **belépőváltozónak** valamely $x_k$-t amelyre $c_k \gt 0$ (*Pozitív célfüggvény együttható*)
3. $a_{ik} \ge 0$ minden $i=1,2,3,..,m$-re?
	- Igen: Az LP feladat **nem korlátos**
	- Nem: folyatás 4. ponttal
4. Legyen $l$ valamely index, amelyre $|\dfrac{b_l}{a_{lk}}|$ minimális és $a_{lk} \lt 0$
5. Hajtsunk végre egy **pivot lépést** úgy, hogy $x_k$ legyen a belépőváltozó és az $l.$ feltétel bázisváltozója legyen a kilépő. Folyataás 1. ponttal

**Pivot lépés:** új szótár megadása egy bázis és nembázis változó szerepének felcserélésével
**Belépőváltozó:** az a nembázis változó, ami a következő szótárra áttéréskor bázisváltozóvá válik
**Kilépő változó:** az a bázisváltozó, ami a köv. szótárra áttéréskor nembázissá válik
**Szótárak ekvivalenciája:** két szótár ekvivalens, ha az általuk leírt egyenletrendszer összes lehetséges megoldása és a hozzájuk tartozó célfüggvényértekek rendre megegyeznek


Pivot lépés előtti és utáni szótárak ekvivalensek.


## Generálóelem választási szabályok


**Klasszikus szimplex algoritmus pivot szabály:** (Nem biztosan áll meg)
- A lehetséges belépőváltozók közül válasszuk a legnagyobb $c_k$ értékűt. Több ilyen esetben a legkisebbet.
- A lehetséges **kilépőváltozók** közül válasszuk a legkisebb $l$ indexű egyenlet változóját.

**Bland szabály** (Biztosan megáll)
- **Oszlop:** a lehetséges belépőváltozók közül válasszuk a legkisebb indexűt
- **Sor:** A lehetséges változók közül válasszuk a legkisebb indexűt

**Legnagyobb növekmény** (Nem biztosan áll meg)
- $max(c_i * min(|\dfrac{b_i}{a_{ij}}|))$, 
*@kép (Legnagyobb_novekmeny.JPG)

**Lexikografikus szabály**
- **kiegészítjük epszilonokkal mesterségesen a szótárat**
	- a lehetséges belépőváltozók közül a legnagyobb $c_k$ értékűt válasszuk, több ilyennél a legkisebb indexűt
	- a lehetséges kilépőváltozók közül azt, amelynek l indexű egyenletére az együtthatókból álló vektor lexikografikusan a legkisebb

Véletlen pivot

- 1 valószínűséggel terminál


## Kétfázisú szimplex módszer

Ha van **negatív konstans**, akkor alkalmazható a kétfázisú szimplex módszer.

**Vegyünk egy segédfeladatot**
- bevezetünk egy új, **x0 mesterséges segédváltozót**
- legyen **w az új célfüggvény:**  $w=-x_0$
- térjünk át szótár alakra
- vegyük a **legnegatívabb jobboldalú egyenletet**, és ebből fejezzük ki $x_0$-t
- a többiből a mesterséges változókat
- **ezután már egy lehetséges indulószótárat kapunk**

A standard feladatnak csak akkor létezik lehetséges megoldása, ha $w=0$ **a hozzá felírt segédfeladat optimuma.**

Ha a segédfeladatot megoldjuk a szimplexszel, és annak optimuma 0, akkor a megoldás utolsó szótárából könynen felírhatunk egy olyan szótárat, amely az eredeti feladat szótára, és bázismegoldása lehetséges megoldás is egyben.

**A szótár felírásának lépései:**
- az $x_0 = 0$ feltételt elhagyjuk
- ha $x_0$ **bázisváltozó**, akkor az egyenletének jobb oldalán lévő nem 0 együtthatójú változók egyikével végrehajtunk **egy pivot lépést**
- **elhagyjuk x0 megmaradt erőforrásait***
- a **célfüggvény egyenletét lecseréljük az eredeti célfüggvényre**, amit átírunk az aktuális bázisváltozóknak megfelelően

A következő fázisban pedig az átírt szótáron futtatjuk a szimplex algoritmust

## Speciális esetek

### Ciklizáció

**Degenerált iterációs lépés:** olyan szimplex iteráció, amelyben nem változik a bázismegoldás
Degenerált bázismegoldás: olyan bázismegoldás, amelyben egy vagy több bázisváltozó értéke is 0

Ciklizáció: ha a szimplex algoritmus valamely iterációja után egy korábbi szótárat visszakapunk, akkor az a ciklizáció

Ha a szimplex algoritmus nem áll meg, akkor ciklizál!
A ciklizáció elkerülhető megfelelő pivot szabály alkalmazásával (lexikografikus, Bland szabály)
A ciklizáció oka a degeneráció, azaz a bázisváltozók 0-vá válása a bázismegoldásban

### Nem korlátos 

Ha az LP feladat maximalizálandó/minimalizálandó, és a célfüggvénye tetszőlegesen nagy/kicsi értéket felvehet, akkor nem korlátos a feladat.
Más szóval, ha tudunk oszlopot választani, de mikor sort választanánk minden együttható pozitív $\rightarrow$ nem korlátos.
*@kep(Nem_korlatos.JPG)*
### Nincs lehetséges megoldás

Ha a standard alakú LP feladatot kétfázisú szimplex módszerrel oldjuk meg, az első fázis eldönti, hogy van-e lehetséges megoldás.

Ha a felírt segédfeladatban az optimum értéke kisebb, mint nulla, akkor nincs lehetséges megoldás, ha 0, akkor van.