

# 9. Normálformák az ítéletkalkulusban, Boole-függvények teljes rendszerei. Következtető módszerek: Hilbert-kalkulus és rezolúció, ezek helyessége és teljessége
## Ítéletkalkulus
- Vannak **változók** ezeket $(p,q,r)$ szoktuk jelölni, és a ${0,1}$ halmazból kapnak igazságértéket. 
- A formulák változókból épülnek fel itéletlogikai összekötő jelekkel (**konnektíva**) pl $\neg$, $\wedge$, $\lor$ stb.

## Normálformák az ítéletkalkulusban
Klózok éselése **Konjukció**
Literálok vagyolása **Diszjunkció**

### DNF (Diszjunktív normálforma)

A formula olyan alakja:
- a változók pozitívan vagy negatívan szerepelhetnek benne
- a zárójelekben lévő pozitív vagy negatív változók között éselés van
- a zárójelek között vagyolás van

### Nyílmentes formula

A nyilakat elimináljuk a formulából a következő szabályok alkalmazásával:

- F -> G == -F || G
- F <-> G == (F -> G) && (G -> F) == (-F || G) && (-G || F)


### CNF (Konjunktív normállforma) 
diszjunkciók konjunkciója

A CNF alakban klózok vannak, és a klózok vannak összeéselve egymással. Egy klózban változók
vannak, negatívan vagy pozitívan, és ezek között vagyolás van. Úgy kapjuk, hogy egy már 
NNF-ben lévő formulában alkalmazzuk a disztribúciós szabályt:

- (F && G) || H == (F || H) && (G || H)
- (F && G) || (H && I) == (F || H) && (F || I) && (G || H) && (G || I)

## Teljes rendszerek

Logikai műveletek (Boole függvények) egy rendszerét akkor nevezzük teljesnek, ha egy, már korábban teljesnek
ítélt rendszer minden műveletét ki tudjuk fejezni ezen műveletekkel. 
$\neg$, $\wedge$, $\lor$ stb.
A {$\neg$, $\wedge$, $\lor$} rendszer
teljes, mert minden formulát CNF alakra tudunk hozni. Ezek alapján teljes még:


- {$\neg$, $\lor$}
- - A negáció okés, az éselés okés, a vagyolást ki tudjuk fejezni: 
- - - $p \lor q$ $\neg(\neg p \wedge  \neg q)$
- {$\neg$, $\wedge$}
- - A negáció okés, a vagyolás okés, az éselést ki tudjuk fejezni:
- - - p $\lor$ q == $\neg$($\neg$p $\wedge$ $\neg$q)

A {$\neg$,$\rightarrow$} rendszer is teljes, mert tudjuk, hogy a {$\neg$, $\lor$} rendszer teljes, és ki tudjuk fejezni
a műveleteit:

- negáció okés, vagyolás: 
- - p $\lor$ q == ($\neg$p) $\rightarrow$ q

A {$\rightarrow$, $\downarrow$} rendszer is teljes, mert tudjuk, hogy a {$\neg$, $\rightarrow$} rendszer teljes, és ki tudjuk
fejezni a műveleteit:
- nyíl okés
- $\neg$p == p $\rightarrow$ $\downarrow$

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
Formailag:
**input**: Klózok $\Sigma$ halmaza
**output:** kielégíthetetlen-e $\Sigma$?
**Algoritmus:**:
Ezután listát vezetünk a klózokról. Egy klóz felkerülhet a listára, ha
- eleme a $\Sigma$-nak
- két, korábban már a listán szereplő klóz rezolvense


Két klóznak akkor vehetjük a **rezolvensét**, ha a **mindkettőben szerepel ugyanaz a változó**, de az **egyikben negatívan**, a **másikban pedig pozitívan**. Ekkor a **rezolvens egy olyan klóz** lesz, **ahol ez a változó már nem fog szerepelni, hanem csak a két klózban maradt összes többi változó.**

Ha a listára valamelyik lépésben rákerül az **üresklóz**, az azt jelenti, hogy $\Sigma$ **kielégíthetetlen**, vagyis az eredeti logikai következmény fennáll. 
**Ha sehogy sem tudjuk levezetni az üresklózt,** az azt jelenti, hogy a $\Sigma$ **kielégíthető,** és az eredeti logikai következmény nem áll fenn.

**Helyesség:** Az algoritmus **kielégíthetetlen** válasszal áll meg, akkor az input $\Sigma$ **valóban kielégíthetetlen**)

**Teljes**: Ha $\Sigma$ **kielégíthetetlen,** akkor az algoritmus mindig a **kielégíthetetlen** válasszal áll meg.

### Hilbert-kalkulus
**Hilbert rendszere (egy deduktív rendszer)**: Az input a $\Sigma$ **összes** következményét lehet vele levezetni.
Ebben a rendszerben **csak** a $\rightarrow$ és a $\downarrow$ logikai konstanst használhatjuk az ítéletváltozókon kívűl

A Hilbert-kalkulusban Hilbert rendszerét használjuk. Az ilyen alakú formulákra is tudunk következtető rendszert építeni. A továbbiakban a formuláink mind Hilbert rendszeréből származnak. 

A következtető rendszerünkben az input szintén egy formulahalmaz, illetve egy formula, amiről be akarjuk látni, hogy logikai következménye a formulahalmazunknak. 

Ekkor a formulákról szintén listát vezetünk, ahol a listára felkerülhet egy formula, ha:

- benne van a $\Sigma$
- axiómapéldány
- modus ponense két, korábban a listán szereplő formulának

Háromféle axiómánk van:
Ax1: (F $\rightarrow$ (G $\rightarrow$ H)) $\rightarrow$ ((F $\rightarrow$ G) $\rightarrow$ (F $\rightarrow$ H))
Ax2: F $\rightarrow$ (G $\rightarrow$ F)
Ax3: ((F $\rightarrow$ $\downarrow$) $\rightarrow$ $\downarrow$) $\rightarrow$ F

**Két formulának vehetjük a modus ponensét**, ha az egyik formula F, a másik pedig F $\rightarrow$ G alakú. Ekkor a **modus ponens** pontosan G lesz.

Ezekkel a szabályokkal ha a listára kerül a logikai következmény jobb oldalán szereplő formula,
akkor igazoltuk a logikai következményt.

Érdemes még az algoritmus előtt a dedukció művelettel kezdeni. Ha a jobb oldali formula F -> G alakú, akkor F-et átvehetjük a $\Sigma$, és ezt mindaddig ismételhetjük, amíg a jobb oldal ilyen alakú.

- **Helyesség és teljesség:**
**Formailag:**
$\Sigma \vdash F \Leftrightarrow \Sigma \vDash F$
Ha $\Sigma \vdash F$, akkor $\Sigma \vDash F$, AZAZ, ha valakit letudok vezetni az input $\Sigma$-ból akkor az következménye is a $\Sigma$-nak.
Tehát van valami $F_1,...,F_n$ levezetés $\Sigma$ felett, És akiket felveszünk a listára az követmezménye lesz a $\Sigma$-nak.



- **+ infók, ez már bizonyítás szint talán idk**:
1. **dedukciós tétel**:
	$\Sigma \vdash (F \rightarrow G) \Leftrightarrow \Sigma \cup \{F\} \vdash G$, 
	Tehát a $\Sigma$ formulahalmazból akkor tudunk **levezetni egy implikációt** $(F\rightarrow G)$, ha annak a **bal oldalát átrakjuk** $\Sigma$-ba ($\Sigma \cup \{F\}$), és ebből a **formulahalmazból le lehet vezetni a jobboldalt** ($G$)-t
2. **H-konszistencia:**
Egy $\Sigma$ formulahalmazt H-konsztizensnek nevezünk, ha **nem** igaz, hogy $\Sigma \vdash \downarrow$.
Azaz **Hilbert rendszerben nem tudjuk bebizonyítani, hogy a formulahalmaz nem kielégíthető (van modelje).**
	