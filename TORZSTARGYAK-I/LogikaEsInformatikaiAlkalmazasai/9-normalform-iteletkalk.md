# 9. Normálformák az ítéletkalkulusban, teljes rendszerek. Következtető módszerek: Hilbert-kalkulus és rezolúció

## Normálformák az ítéletkalkulusban

### Diszjunktív normálforma

A formula olyan alakja:

- a változók pozitívan vagy negatívan szerepelhetnek benne
- a zárójelekben lévő pozitív vagy negatív változók között éselés van
- a zárójelek között vagyolás van

### Nyílmentes formula

A nyilakat elimináljuk a formulából a következő szabályok alkalmazásával:

- F -> G == -F || G
- F <-> G == (F -> G) && (G -> F) == (-F || G) && (-G || F)

### NNF

A negációkat bevisszük teljesen a változók elé, hogy semmilyen zárójeles kifejezés előtt 
ne szerepeljen negáció. Ez a formula már nyílmentes is.
Ehhez a De Morgan szabályokat alkalmazzuk:

- -(F || G) == -F && -G
- -(F && G) == -F || -G

### CNF

A CNF alakban klózok vannak, és a klózok vannak összeéselve egymással. Egy klózban változók
vannak, negatívan vagy pozitívan, és ezek között vagyolás van. Úgy kapjuk, hogy egy már 
NNF-ben lévő formulában alkalmazzuk a disztribúciós szabályt:

- (F && G) || H == (F || H) && (G || H)
- (F && G) || (H && I) == (F || H) && (F || I) && (G || H) && (G || I)

## Teljes rendszerek

Logikai műveletek egy rendszerét akkor nevezzük teljesnek, ha egy, már korábban teljesnek
ítélt rendszer minden műveletét ki tudjuk fejezni ezen műveletekkel. A {-, &&, ||} rendszer
teljes, mert minden formulát CNF alakra tudunk hozni. Ezek alapján teljes még:

- {-, &&}
- - A negáció okés, az éselés okés, a vagyolást ki tudjuk fejezni: 
- - - p || q == -(-p && -q)
- {-, ||}
- - A negáció okés, a vagyolás okés, az éselést ki tudjuk fejezni:
- - - p && q == -(-p || -q)

A {-, ->} rendszer is teljes, mert tudjuk, hogy a {-, ||} rendszer teljes, és ki tudjuk fejezni
a műveleteit:

- negáció okés, vagyolás: 
- - p || q == (-p) -> q

A {->, lenyíl} rendszer is teljes, mert tudjuk, hogy a {-, ->} rendszer teljes, és ki tudjuk
fejezni a műveleteit:

- nyíl okés
- -p == p -> lenyíl

Ezt a rendszert nevezzük Hilbert rendszerének.

### Rezolúció

A rezolúciónál a formuláink CNF alakban vannak. A rezolúcióval logikai következményeket tudunk
bebizonyítani, pl. hogy egy formulahalmaznak logikai következménye egy formula.

Alapból a logikai következmény azt jelenti, hogy azoknak az értékadásonak a halmaza, amelyek kielégítik a jobboldali formulá(ka)t, részhalmaza a jobboldali formulákat kielégítő értékadások
halmazának. Ezzel az a baj, hogy az összes ilyen értékadást megtalálni nagyon hosszadalmas.

A rezolúciós algoritmus inputja klózoknak egy halmaza, és outputja egy igen vagy egy nem, attól függően, hogy kielégíthető vagy kielégíthetetlen ez a klózhalmaz. 
A baloldali formulák közé felvesszük először a jobboldali formula negáltját, hiszen ha 
az így kapott új formulahalmaz kielégíthetetlen (azaz Mod(Szigma) üreshalmaz), akkor
az eredeti logikai következmény fennáll. 

Ezután listát vezetünk a klózokról. Egy klóz felkerülhet a listára, ha 

- eleme a Szigmának
- két, korábban már a listán szereplő klóz rezolvense

Két klóznak akkor vehetjük a rezolvensét, ha a mindkettőben szerepel ugyanaz a változó, de az egyikben negatívan, a másikban pedig pozitívan. Ekkor a rezolvens egy olyan klóz lesz, ahol ez a változó már nem fog szerepelni, hanem csak a két klózban maradt összes többi változó.

Ha a listára valamelyik lépésben rákerül az üresklóz, az azt jelenti, hogy Szigma kielégíthetetlen, vagyis az eredeti logikai következmény fennáll. Ha sehogy sem tudjuk levezetni az üresklózt, az azt jelenti, hogy a Szigma kielégíthető, és az eredeti logikai következmény nem áll fenn.


### Hilbert-kalkulus

A Hilbert-kalkulusban Hilbert rendszerét használjuk. Az ilyen alakú formulákra is tudunk következtető rendszert építeni. A továbbiakban a formuláink mind Hilbert rendszeréből származnak. 

A következtető rendszerünkben az input szintén egy formulahalmaz, illetve egy formula, amiről be akarjuk látni, hogy logikai következménye a formulahalmazunknak. 

Ekkor a formulákról szintén listát vezetünk, ahol a listára felkerülhet egy formula, ha:

- benne van a Szigmában
- axiómapéldány
- modus ponense két, korábban a listán szereplő formulának

Háromféle axiómánk van:
Ax1: (F -> (G -> H)) -> ((F -> G) -> (F -> H))
Ax2: F -> (G -> F)
Ax3: ((F -> lenyíl) -> lenyíl) -> F

Két formulának vehetjük a modus ponensét, ha az egyik formula F, a másik pedig F -> G alakú. Ekkor a modus ponens pontosan G lesz.

Ezekkel a szabályokkal ha a listára kerül a logikai következmény jobb oldalán szereplő formula,
akkor igazoltuk a logikai következményt.

Érdemes még az algoritmus előtt a dedukció művelettel kezdeni. Ha a jobb oldali formula F -> G alakú, akkor F-et átvehetjük a Szigmába, és ezt mindaddig ismételhetjük, amíg a jobb oldal ilyen alakú.