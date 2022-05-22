

# 9. Normálformák az ítéletkalkulusban, Boole-függvények teljes rendszerei. Következtető módszerek: Hilbert-kalkulus és rezolúció, ezek helyessége és teljessége
## Alapvető információk
- $Mod(F)$: Az $F$ formula **modelljei** (olyan értékadások amelyek mellett az $F$ igaz)
- $A \in Mod(F)$: az A **értékadás** F egy **modelje**
- $\vDash F$:  Az F formula **tautológia** (azaz minden értékadás mellett igaz)
- $F \vDash G$: Az F formulának **logikai következménye**  a G formula.

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
#### Boole függvények
**Boole függvények** egy $H$ rensdzere **teljes**, ha minden $n \ge 1$-változós Boole-függvény előáll:
- Projekciókból
- és H elemeiből
- alkalmas **kompocízióval**

#### Teljes rendszer
Olyan Boole függvények, amelyekkel kifejezhető az összes többi is.

Logikai műveletek (Boole függvények) egy rendszerét akkor nevezzük teljesnek, ha egy, már korábban teljesnek
ítélt rendszer minden műveletét ki tudjuk fejezni ezen műveletekkel. 
$\neg$, $\wedge$, $\lor$ stb.
**A {$\neg$, $\wedge$, $\lor$} rendszer teljes**, mert minden formulát CNF alakra tudunk hozni. Ezek alapján teljes még:
- {$\neg$, $\lor$}:
	- A negáció okés, az éselés okés, a vagyolást ki tudjuk fejezni: 
	- $p \lor q$ $\equiv$ $\neg(\neg p \wedge  \neg q)$
	
- {$\neg$, $\wedge$}
	- A negáció okés, a vagyolás okés, az éselést ki tudjuk fejezni:
	-  p $\lor$ q $\equiv$ $\neg$($\neg$p $\wedge$ $\neg$q)

**A {$\neg$,$\rightarrow$} rendszer is teljes, mert** tudjuk, hogy **a {$\neg$, $\lor$} rendszer teljes**, és ki tudjuk fejezni **a műveleteit:**
- $\neg$ okés, vagyolás: 
- p $\lor$ q $\equiv$ ($\neg$p) $\rightarrow$ q

**A {$\rightarrow$, $\downarrow$} rendszer is teljes, mert** tudjuk, hogy **a {$\neg$, $\rightarrow$} rendszer teljes**, és ki tudjuk
fejezni a műveleteit:
- $\rightarrow$ okés
- $\neg$p $\equiv$ p $\rightarrow$ $\downarrow$

Ezt a rendszert nevezzük Hilbert rendszerének.

### Rezolúció

A rezolúciónál a **formuláink CNF alakban** vannak. A rezolúcióval logikai következményeket tudunk
bebizonyítani, pl. hogy egy formulahalmaznak logikai következménye egy formula.

**Alapból a logikai következmény azt jelenti, hogy azoknak az értékadásonak a halmaza, amelyek kielégítik a jobboldali formulá(ka)t, részhalmaza a jobboldali formulákat kielégítő értékadások**
halmazának. Ezzel az a baj, hogy az összes ilyen értékadást megtalálni nagyon hosszadalmas.

**Formailag:**
**input**: Klózok $\Sigma$ halmaza
**output:** kielégíthetetlen-e $\Sigma$?
**Algoritmus:**:
Ezután listát vezetünk a klózokról. Egy klóz felkerülhet a listára, ha:
- eleme a $\Sigma$-nak
- két, korábban már a listán szereplő klóz rezolvense

Két klóznak akkor vehetjük a **rezolvensét**, ha a **mindkettőben szerepel ugyanaz a változó**, de az **egyikben negatívan**, a **másikban pedig pozitívan**. Ekkor a **rezolvens egy olyan klóz** lesz, **ahol ez a változó már nem fog szerepelni, hanem csak a két klózban maradt összes többi változó.**

Ha a listára valamelyik lépésben rákerül az **üresklóz**, az azt jelenti, hogy $\Sigma$ **kielégíthetetlen**, vagyis az eredeti logikai következmény fennáll. 
**Ha sehogy sem tudjuk levezetni az üresklózt,** az azt jelenti, hogy a $\Sigma$ **kielégíthető,** és az eredeti logikai következmény nem áll fenn.

**Helyesség:** Az algoritmus **kielégíthetetlen** válasszal áll meg, akkor az input $\Sigma$ **valóban kielégíthetetlen**).

**Teljes**: Ha $\Sigma$ **kielégíthetetlen,** akkor az algoritmus mindig a **kielégíthetetlen** válasszal áll meg.

Példa:
Igazoljuk rezolúcióval, hogy kielégithetetlen:
$(((p→q) ∧ ¬q) ∨ ((r→¬p) ∧ r)) ∧ s ∧ (s→p)$

1. CNF-re hozás
	1. Nyilak eliminálása:
	$(((¬p∨q) ∧ ¬q) ∨ ((¬r∨¬p) ∧ r)) ∧ s ∧ (¬s∨p)$ 
	2. Negáció bevitele: Ez itt kész
	3. Disztributivitás:
	$((¬p ∨ q ∨ ¬r ∨ ¬p) ∧ (¬p ∨ q ∨ r) ∧ (¬q ∨ ¬r ∨ ¬p) ∧ (¬q ∨ r)) ∧ s ∧ (¬s ∨ p)$
2. Rezolúció:
$\Sigma = {\{¬p, q, ¬r\}, \{¬p, q, r\}, \{¬p, ¬q, ¬r\}, \{¬q, r\}, \{s\}, \{p, ¬s\}}$
MELLÉKLET KÉP (Rezolucio.JPG)

### Hilbert-kalkulus
**Hilbert rendszere (egy deduktív rendszer)**: 
- **Az input a $\Sigma$ összes következményét lehet vele levezetni.**

Ebben a rendszerben **csak** a $\rightarrow$ és a $\downarrow$ logikai konstanst használhatjuk az **ítéletváltozókon kívűl**
**Minden formulát ilyen alakra lehet hozni, mivel $\{\rightarrow, \downarrow\}$ teljes rendszer.**

A Hilbert-kalkulusban Hilbert rendszerét használjuk. Az ilyen alakú formulákra is tudunk következtető rendszert építeni. A továbbiakban a formuláink mind Hilbert rendszeréből származnak. 

**Hilbert rendszere:**
**Input:** Egy $\Sigma$ formulahalmaz és egy $F$ célformula
**Output:** Igaz-e, hogy $\Sigma \vDash F$
**Lépések:** Listát vezetünk a formulákról. A listákra a következő elemek kerülhetnek fel:
- $\Sigma$ elemei
- Axiómapéldányok ízlés szerint.
- *Modus ponens:* ha $F$ és $F \rightarrow G$ is megvan a listán, akkor felvehetjük $G$. Gyakorlatilag levágjuk a nyilnál.

**Háromféle axiómánk van:**
- Ax1: (F $\rightarrow$ (G $\rightarrow$ H)) $\rightarrow$ ((F $\rightarrow$ G) $\rightarrow$ (F $\rightarrow$ H))
- Ax2: F $\rightarrow$ (G $\rightarrow$ F)
- Ax3: ((F $\rightarrow$ $\downarrow$) $\rightarrow$ $\downarrow$) $\rightarrow$ F


Példa:
Mutassuk meg dedukcióval, hogy $\vdash \downarrow \rightarrow p$

Ha alkalmazzuk a dedukciót akkor egyből az új feladat: $\downarrow$$\vdash p$
KÉPET IDE

- **Helyesség és teljesség:**
**Formailag:**
Ha $\Sigma \vdash F$, akkor $\Sigma \vDash F$, AZAZ, ha valakit letudok vezetni az input $\Sigma$-ból akkor az következménye is a $\Sigma$-nak.
Tehát van valami $F_1,...,F_n$ levezetés $\Sigma$ felett, És akiket felveszünk a listára az követmezménye lesz a $\Sigma$-nak.



- **+ infók, ez már bizonyítás szint talán idk**:
1. **dedukciós tétel**:
	$\Sigma \vdash (F \rightarrow G) \Leftrightarrow \Sigma \cup \{F\} \vdash G$, 
	Tehát a $\Sigma$ formulahalmazból akkor tudunk **levezetni egy implikációt** $(F\rightarrow G)$, ha annak a **bal oldalát átrakjuk** $\Sigma$-ba ($\Sigma \cup \{F\}$), és ebből a **formulahalmazból le lehet vezetni a jobboldalt** ($G$)-t
2. **H-konszistencia:**
Egy $\Sigma$ formulahalmazt H-konsztizensnek nevezünk, ha **nem** igaz, hogy $\Sigma \vdash \downarrow$.
Azaz **Hilbert rendszerben nem tudjuk bebizonyítani, hogy a formulahalmaz nem kielégíthető (van modelje).**
	