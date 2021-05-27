# 5. Véges automata és változatai, a felismert nyelv definíciója. A reguláris nyelvtanok, a véges automaták és a reguláris kifejezések ekvivalenciája. Reguláris nyelvekre vonatkozó pumpáló lemma, alkalmazása és következményei

## Véges automata és változatai, a felismert nyelv definíciója

Lásd pdf

## A reguláris nyelvtanok, a véges automaták és a reguláris kifejezések ekvivalenciája

### Reguláris nyelvtanok

- N: nemterminális abc
- SZIGMA: terminális abc
- P: szabályok halmaza
- S: eleme N, kezdő nemterminális
Egy G=(N, SZIGMA, P, S) nyelvtan reguláris (vagy jobblineáris), ha P-ben minden szabály

- A -> xB vagy
- A -> x

alakú.

Azért jobblineáris, mert minden szabály jobb oldalán max. egy nemterminális állhat, és ez mindig a szó végén helyezkedik el. Levezetést csak A -> x alakú szabállyal fejezhetünk be, ahol x eleme  SZIGMA*. A reguláris nyelvtanok speciális környezetfüggetlen nyelvtanok.

Példa: S → aaS|abS|baS|bbS|ε, vagyis a páros hosszú szavakat generáló nyelvtan.


### Reguláris kifejezések

Veszünk egy abc-t, és hozzáveszünk néhány szimbólumot, ezekből építünk reguláris kifejezéseket.

A szigma feletti reguláris kifejezések halmaza a (Σ∪{∅, ε,(,),+,∗})* halmaz legszűkebb olyan U részhalmaza, hogy 

- ∅, ε eleme U-nak
- minden a eleme Σ eleme U-nak
- ha R1, R2 eleme U, akkor R1+R2, R1R2, R1* is eleme U-nak

Prioritási sorrend: *, konkatenáció, +

Jelentések:

- |R|, az R által reprezentált nyelv
- R = ∅, |R| = ∅, azaz az üres nyelv
- R = ε, |R| = {ε}, azaz az epszilon szimbólum önmagában, mint nyelv
- R = a, |R| = {a}, azaz az a szimbólum önmagában, mint nyelv
- R = R1+R2, |R| = |R1| ∪ |R2|, azaz a két regex által generált nyelv uniója
- R = R1R2, |R| = |R1||R2|, azaz a két regex által generált nyelv konkatenációja
- R = R1*, akkor |R| = |R1|*, azaz a regex által generált nyelv iterációja, az összes szó összekonkatenálva egy másik nyelvbeli szóval az összes lehetséges módon

### Ekvivalencia

Tetszőleges L részhalmaza szigmacsillag nyelv esetén a következő három állítás ekvivalens:

- 1. L generálható reguláris nyelvtannal
- 2. L felismerhető automatával
- 3. L reprezentálható reguláris kifejezéssel

3 -> 1

Ha L reprezentálható reguláris kifejezéssel, akkor generálható reguláris nyelvtannal.

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

1 -> 2

Ha L nyelv reguláris, akkor felismerhető automatával.

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


2 -> 3

Minden automatával felismert nyelv reprezentálható reguláris kifejezéssel. (Kleene tétele)
wtf bro


