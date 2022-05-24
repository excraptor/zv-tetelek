
# 5. Véges automata és változatai, a felismert nyelv definíciója. A reguláris nyelvtanok, a véges automaták és a reguláris kifejezések ekvivalenciája. Reguláris nyelvekre vonatkozó pumpáló lemma, alkalmazása és következményei

## Alapfogalmak, jelölések
**Ábécé:** Szimbólumok egy tetszőleges véges, nemüres halmaza jele: $\Sigma$
-	$\Sigma^*$: Az összs szavak + $\epsilon$
- $\Sigma^+$: Az összes szavak, kivéve az $\epsilon$
- $\Sigma$ **ábécé feletti szó:** egy $a_1,...,a_k$ alakú sorozat.
- **Nyelv:** $\Sigma^*$ tetszőleges $L$ részhalmazát egy $\Sigma$ feletti **nyelvnek** nevezzük. Ha $L$ véges számú szóból áll, akkor **véges nyelvnek nevezzük*
- **Nyelvtan:** Könnyen leírható eszköz, amely alkalmas nyelvek megadására. Effektíve nyelveket tuduk vele reprezentálni.
	- PL Környezetfüggetlen: $G = (N, \Sigma, P, S)$, ahol
		- N egy ábécé
		- $\Sigma$ egy ábécé, terminális
		- $S\in N$ kezdő szimbólum
		- $P$ pedig egy $A\rightarrow \alpha$ alakú átírási szabály.
## Véges automata és változatai, a felismert nyelv definíciója

Lásd pdf

Egy nemdeterminisztikus automata determinizálása:
**Állapotai száma max 2^n lesz.**
- Elindulunk a kezdőállapotból és megnézzük, hogy az első betű hatására hova megy -> ezeket összevonjuk egy állapottá és oda vezetjük ezzel a betűvel.
- Ezután az új összevont állapot részeit nézzük meg, hogy onnan a betűk hova mennek.

Egy $\epsilon$ automata $\epsilon$-mentesítése.
- Lezártakat számolunk.
	- Azokat az állapotokat, ahova átlehet jutni $\epsilon$ átmenettel azokat egy lezártba vesszük.


## A reguláris nyelvtanok, a véges automaták és a reguláris kifejezések ekvivalenciája

### Reguláris nyelvtanok

- $N:$ nemterminális abc
- $\Sigma$: terminális abc
- $P$: szabályok halmaza
- $S$: eleme N, kezdő nemterminális
Egy $G=(N, \Sigma, P, S)$ nyelvtan reguláris (vagy jobblineáris), ha P-ben minden szabály

- $A -> xB$ vagy
- $A -> x$, alakú.

Azért jobblineáris, mert minden szabály jobb oldalán max. egy nemterminális állhat, és ez mindig a szó végén helyezkedik el. Levezetést csak A -> x alakú szabállyal fejezhetünk be, ahol $x \in \Sigma^*$. A reguláris nyelvtanok speciális környezetfüggetlen nyelvtanok.

Példa: S → aaS|abS|baS|bbS|ε, vagyis a páros hosszú szavakat generáló nyelvtan.


### Reguláris kifejezések

**Veszünk egy abc-t, és hozzáveszünk néhány szimbólumot, ezekből építünk reguláris kifejezéseket.**

A szigma feletti reguláris kifejezések halmaza a $(Σ∪{∅, ε,(,),+,∗})*$ halmaz legszűkebb olyan U részhalmaza, hogy 

- ∅, ε eleme U-nak
- minden a eleme Σ eleme U-nak
- ha R1, R2 eleme U, akkor R1+R2, R1R2, R1* is eleme U-nak

Prioritási sorrend: *, konkatenáció, +

**Jelentések:**

- **|R|, az R által reprezentált nyelv**
- R = ∅, |R| = ∅, azaz az üres nyelv
- R = ε, |R| = {ε}, azaz az epszilon szimbólum önmagában, mint nyelv
- R = a, |R| = {a}, azaz az a szimbólum önmagában, mint nyelv
- R = R1+R2, |R| = |R1| ∪ |R2|, azaz a két regex által generált nyelv uniója
- R = R1R2, |R| = |R1||R2|, azaz a két regex által generált nyelv konkatenációja
- R = R1*, akkor |R| = |R1|*, azaz a regex által generált nyelv iterációja, az összes szó összekonkatenálva egy másik nyelvbeli szóval az összes lehetséges módon

### Ekvivalencia

Tetszőleges $L \subseteq \Sigma^*$  nyelv esetén a következő három állítás ekvivalens:

- 1. L generálható reguláris nyelvtannal
- 2. L felismerhető automatával
- 3. L reprezentálható reguláris kifejezéssel

**3 -> 1:**
*Ha L reprezentálható reguláris kifejezéssel, akkor generálható reguláris nyelvtannal.*

Bizonyítás: L-et reprezentáló R reguláris kifejezés struktúrája szerinti indukcióval.

- R = ∅: ekkor L=|R|=∅, ekkor L generálható a G=(N, SZIGMA, ∅, S) nyelvtannal.
- R = a: a eleme SZIGMA, vagy a=epszilon, ekkor L=|R|={a}, ami generálható a G=(N, SZIGMA, {S -> A}, S) nyelvtannal
- INDUKCIÓ R = R1+R2, ekkor L=|R|=L1 unió L2, L1=|R1|, L2=|R2|
    - ekkor tegyük fel, hogy Li generálható egy Gi= (Ni,Σ,Pi,Si) (i=1,2) reguláris nyelvtannal
    - ekkor L generálható egy G= (N1∪N2∪{S},Σ,P1∪P2∪{S→S1,S→S2},S) nyelvtannal, ahol S egy új szimbólum
    - aka vesszük az összes nemterminálist, az abc-t, az összes korábbi szabályt
    - továbbá egy új kezdőszimbólumot
    - és az új kezdőszimbólumból elérhető a régi kettő kezdőszimbólum, aka kiválaszthatjuk, melyik nyelvből származó szót akarjuk generálni
    - ahhoz, hogy elérhető legyen a régi két kezdőszimbólum, felveszünk két új szabályt értelemszerűen a régiek közé
- INDUKCIÓ R = R1R2, ekkor L=|R|=L1L2, L1=|R1|, L2=|R2|
    - ekkor tegyük fel, hogy Li generálható egy Gi= (Ni,Σ,Pi,Si) (i=1,2) reguláris nyelvtannal
    - Akkor L generálható a G = (N1∪N2,Σ,P,S1) nyelvtannal, ahol P:
        - belevesszük az összes szabályt az első nyelvet generáló nyelvtanból, a befejező szabályok végére odaírjuk a második nyelvtan kezdőszimbólumát
        - a második nyelvtan összes szabályát is belevesszük
- INDUKCIÓ R = R1*, ekkor L=|R|=L1*, ahol L1=|R1|
    - ekkor tegyük fel, hogy L1 generálható egy G1= (N1,Σ,P1,S1) nyelvtannal
    - ekkor L generálható egy G= (N1∪{S},Σ,P,S) nyelvtannal, ahol S egy új szimbólum
    - a szabályokat úgy módosítjuk, hogy:
        - S-ből elérhető az üresszó és az eredeti kezdőszimbólum
        - a nem "befejező" szabályokat felvesszük úgy, ahogy voltak
        - a "befejező" szabályok jobb oldalára odaírjuk az S-t

**1 -> 2:**
*Ha L nyelv reguláris, akkor felismerhető automatával.*

Bizonyítás: legyen L egy reguláris nyelv, és L=L(G), ahol G egy reguláris nyelvtan.

Minden G= (N,Σ,P,S), reguláris nyelvtanhoz megadható vele ekvivalens G′= (N′,Σ,P′,S) reguláris nyelvtan, ́ugy hogy P′-ben minden szabály A→B, A→aB vagy A→ε alakú, ahol A,B ∈ N ́es a ∈ Σ.

Bizonyítás

- amelyik szabály már alapból ilyen alakú, azokat felvesszük P'-be
- az A -> a1a2a3...anB alakú szabályokat szétdaraboljuk
    - lesz belőle A -> a1A1, A1 -> a2A2 -> ... An-1 -> anB
- az A -> a1a2a3...an szabályokat feladarboljuk
    - lesz belőle A -> a1A1, A1 -> a2A2 -> ... -> An -> epszilon

az új nemterminálisokat felvesszük N-be


Minden olyan G= (N,Σ,P,S) reguláris nyelvtanhoz, melynek csak A→B, A→aB vagy A→ε alakú szabályai vannak megadható olyan M= (Q,Σ, δ,q0,F) nemdeterminisztkius ε-automata, amelyre L(M) =L(G).

Bizonyítás

- Q = N, azaz a nemterminálisokból lesznek az állapotok
- q0 = S, a kezdőszimbólumból lesz a kezdőállapot
- azokból a B nemterminálisokból lesz végállapot, amikből van B -> epszilon szabály
- minden A -> aB kinézetű szabályból pedig legyen egy átmenet A-ból B-be a hatására


**2 -> 3:**
*Minden automatával felismert nyelv reprezentálható reguláris kifejezéssel. (Kleene tétele)*

Bizonyítás: legyen L=(M), ahol M egy determinisztikus automata. Megadunk egy olyan reguláris kifejezést, ami L-et reprezentálja.

Tételezzük fel, hogy Q={1,2,3,...,n}, és q0=1.
Minden 0 kisebbegyenlő k, azaz k darab állapot, és 0 kisebbegyenlő i, j kisebbegyenlő n esetén definiáljuk az L^(k)_i,j nyelvet a következőképpen:

Nézzük úgy az automatát, mintha az i. állapotból indulnánk, és a j.-be akarnánk eljutni, de csak az {1,...,k} állapotokat érinthetjük. Az L^(k)_i,j nyelv azokat a szavakat tartalmazza, amelyeket ez a "kisebb" automata felismer.

Ezután vegyük észre azt, hogy az L nyelv tulajdonképpen úgy áll elő, hogy venni kell az összes olyan L^(n)_1,j nyelvet, ahol j egy végállapot!
Tehát vegyük az összes olyan nyelvet, ahol az első állapotból akarunk elindulni, és az utolsóba eljutni, és használhatjuk az összes állapotát M-nek (mind az n darabot). Tehát ezen L^(n)_1,j nyelvek uniója lesz L.

Ezért elég az L^(n)_1,j-ket reprezentáló reguláris kifejezéseket megadnunk (R^(n)_1,j).

Ehhez meg kell adnunk az R^(k)_i,j reguláris kifejezéseket k szerinti indukcióval.

k=0 azt jelenti, hogy 0 közbülső állapotból kell eljutnunk az i állapotból a j állapotba. Ez lehet úgy, hogy valamilyen szimbólum hatására átmegyünk, vagy ha i=j, akkor hurokéllel helyben maradunk, vagy epszilonnal nem csinálunk semmit.

Az indukciós feltevésünk az, hogy minden i,j-re megadtuk az R^(k)_i,j-t

k+1-hez ÉSZREVESSZÜK (ja ugye tök triviális lmao)

L^(k+1)_i,j egyenlő azzal, hogy 

- vagy amúgyis eljutunk k köztes állapottal is i-ből j-be
- vagy belevesszük a k+1. állapotot is a levesbe, elmegyünk az 1-estől a k+1. állapotba, ott körözünk akármeddig, és utána k+1-ből pedig eljutunk j-be

Ekkor, mivel az L^(k)_i,j nyelvekhez az indukciós feltevés miatt tudtunk megfelelő regexet adni, ezekre elvégezve az előző azonosságot, megkapjuk az R^(k+1)_i,j-t is, ezzel pedig meg tudjuk kapni az összes regexet, ami a kezdőállapotból a végállapotokba visz, ezeket uniózva pedig az egész nyelvhez tartozó regexet.

## Reguláris nyelvekre vonatkozó pumpáló lemma, alkalmazása és következményei

### Pumpáló lemma

Minden L reguláris nyelv esetén megadható egy L-től függő k>0 szám, melyre minden $w \in L$ esetén, ha $|w| \ge k$, akkor van olyan $w = w_1w_2w_3$ felbontás, hogy

- $0 \le |w_2|$ és $|w_1w_2| \le k$
- minden $n \ge 0$ $w_1w_2^nw_3 \in L$

Fordítva, ha egy nyelvhez nem adható meg ilyen k szám, akkor a nyelv nem reguláris.

Kb a lényeg, hogy ha egy nyelv reguláris, akkor a k-nál hosszabb szavak felbonthatók három részre, és a középső rész ismétlődhet akármeddig

### Alkalmazása

Pl bebizonyíthatjuk vele egy nyelvről, hogy nem reguláris.
$a^nb^n$, $n \ge 0$ nyelv nem reguláris

tegyük fel, hogy van ilyen k, amivel felbontható
a feltételek miatt w2-ben csak a betűk vannak
ha ezt pumpáljuk, több a betű lesz benne, mint b - rossz

### Következményei

Van olyan környezetfüggetlen nyelv, amelyik nem reguláris.
1. Minden reguláris nyelvtan környezetfüggetlen. (A REG nyelvek speciális CF nyelvek--jobblineárisak)  
2. CF - REG != Üreshalmaz, mivel pl az {$a^nb^n$ | n >= 0} nyelv CF beli (S -> aSb | $\epsilon$), viszont nem teljesül rá a pumpáló lemma --> nem REG nyelv! 

