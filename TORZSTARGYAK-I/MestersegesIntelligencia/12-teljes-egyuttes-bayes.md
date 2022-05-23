# 12. Teljes együttes eloszlás tömör reprezentációja, Bayes hálók. Gépi tanulás: felügyelt tanulás problémája, döntési fák, naiv Bayes módszer, modellillesztés, mesterséges neuronhálók, k-legközelebbi szomszéd módszere
## Teljes együttes eloszlás tömör reprezentációja, Bayes hálók

### Teljes együttes eloszlás

Minden lehetséges eseményre tudjuk annak a valószínűségét. Pl van 3 logikai típusú véletlen változónk, akkor összesen 2^3=8-féle eset lehet ezekre. A teljes együttes eloszlásnál mind a 8 esetnek tudjuk a valószínűségét. $\rightarrow$ **az összes elemi esemény valószínűségét megadja.**
Viszont nyilván ez miatt nem skálázódik jól.

### Tömör reprezentáció

A **kijelentések függetlensége** a legfontosabb tulajdonság a teljes együttes eloszlás tömöríthetőségéhez. Van **függetlenség, és feltételes függetlenség**.

**Függetlenség**
a és b kijelentések **függetlenek**, ha $P(a \wedge b) = P(a)*P(b)$

**A függetlenség struktúrát takar**. Ha pl $n$ logikai változónk van, amik két független részhalmazra oszthatók  $m$ és $k$ mérettel, akkor a $2^n$ valószínűség tárolása helyett elég $2^m+2^k$ valószínűséget tárolni, ami sokkal kevesebb lehet.

Extrém esetben, ha pl. az A1,..., An diszkrét változók kölcsönösen függetlenek (tetszőleges két részhalmaz független), akkor csak O(n) értéket kell tárolni, mivel ez esetben

P(A1,..., An) = P(A1)...P(An)

**Feltételes függetlenség**
Az abszolút függetlenség ritka. Ezért használhatunk feltételesen függetlenséget.
$a$ és $b$ kijelentések **feltételesen függetlenek** $c$ feltevésével, akkor és csak akkor, ha $P(a \wedge b | c) = P(a|c)*P(b|c)$. Tipikus eset, ha $a$ és $b$ közös oka $c$.
Pl: fogfákás és a beakadás közös oka a luk.

**Naiv-Bayes modell alakja**
Ha $A$ feltevése mellett $B_1,...,B_n$ kölcsönösen függetlenek, akkor 
$P(B1, . . . , Bn|A) = \prod_{i=1}^{n} P(B_i|A)$. ha ez igaz, akkor ez a *Naiv-Bayes modell alakja*, ami a következőképp definiálható:
$P(B1, . . . , Bn,A) = P(A)\prod_{i=1}^{n} P(B_i|A)$,
**Ezzel $O(n)$ tömörítés érhető el**

**Bayes szabály $a$ és $b$ kijelentésekre**
$P(a|b) = \dfrac{P(b|a)P(a)}{P(b)}$,
ez következik a feltételes függetlenség képletéből: 
P$(a \wedge b) = P(a|b)P(b) = P(b|a)P(a)$

### Bayes hálók

A feltételes függetlenség hasznos, mert tömöríthetjük a teljes együttes eloszlást.
A teljes együttes eloszlás feltételes függetlenségeit ragadja meg és ezekből egy **speciális gráfot** definiál. Ez tömör és intuitív reprezentációt tesz lehetővé.

Bayes háló esetén alkalmazunk **láncszabályt**, ami azt jelenti, hogy a **teljes együttes eloszlást** (amit majd tömöríteni szeretnénk) **feltételes eloszlások szorzataként** jeleníti meg.
Formailag:
$$P(X1, . . . , Xn) = \prod_{i=1}^{n} P(X_i|X_{i+1},...,X_n)$$

Ezután az egyes feltételes valószínűségelből elhagyhatunk változókat, azaz minden $P(X_i | X_{i+1},..,X_n)$ tényezőre az $\{X_{i+1},..,X_n\}$ változókból vegyünk egy $Szulok(x_i)$.
Ebből tudunk tömöríteni, mivel a Szülők halmaz minimális.
$$P(X1, . . . , Xn) = \prod_{i=1}^{n} P(X_i|\text{Szülő}(X_i))$$ (ez a bayes háló)
**Ez a teljes eloszlás tömörített reprezentációja.**
Ezt lehet egy gráf formájában vizualizálni.
Például az $X_i$ változókat fel lehet venni mint a gráf csomópontjai, a $Szulok(X_i)$ halmaz elemeiből pedig éleket lehet húzni az $X_i$ változó felé.
**Ez a gráf irányított körmentes gráf lesz.**





## Gépi tanulás: felügyelt tanulás problémája, döntési fák, naiv Bayes módszer, modellillesztés, mesterséges neuronhálók, k-legközelebbi szomszéd módszere

### Felügyelt tanulás problémája

Tapasztalati tények felhasználása arra, hogy egy racionális ágens teljesítményét növeljük.

Felügyelt tanulás: 

- van az adatok mögött valami $f: X \rightarrow Y$ függvény, ezt nem ismerjük
- adottak tanulópéldák, amik rendezett párok $(x, f(x))$
- egy $h: X \rightarrow Y$, függvényt keresünk, ami illeszkedik a példákra, és közelíti $f$-et
- egy példában az első elem pl egy email, a második pedig egy valamilyen címke, pl spam, $\neg$spam
- $h$ **konzisztens az adatokra, ha** $h(x)==f(x)$ minden $x$ tanulópéldára
- a $h$ függvényt mindig valami $H$ hipotézistérben keressük, vagyis **valamilyen "alakban"**
- a tanulás **realizálható**, ha van olyan $h \in H$, amire $h$ konzisztens
- a gyakorlatban elég, ha h közel van a példákhoz, mert a példák zajt is tartalmazhatnak, amit kifejezetten káros lenne, ha megtanulna az ágens (túltanulás)
- egy olyan h-t keresünk, ami a tanulópéldákon kívül is jól általánosít
- nem szabad a tanulópéldákat bemagolni
- **occam borotvája:** mindig a legtömörebb leírást kell venni
- a priori ismeretek fontosak, a nulláról való tanulás kb lehetetlen
- számítási szempontból egyszerű reprezentáció is fontos

### Döntési fák
**Induktív (felügyelt) tanulás konkrét példája.**

Feltesszük, hogy $x\in X$-ben diszkrét változók egy vektora van, $f(x)\in Y$-ban pedig szintén valami diszkrét változó egy értéke, pl igen-nem

Tulajdonképpen osztályozás, $X$ **elemeit** kell $Y$ valamelyik **osztályába** sorolni.

Előnye, hogy döntései megmagyarázhatók, mert emberileg értelmezhető lépésekben jutottunk el odáig.

**Kifejezőereje megegyezik az ítéletkalkuluséval.**
Mivel vannak valamilyen **ítéletek** (változó értékadások), egy **modell** (egy $x\in X$ változóvektor), és egy **formula** (döntési fából adódoan)

**Döntési fa építése:**

- adottak **pozitív és negatív példák felcímkézve**, tipikusan több száz
- vegyük a **gyökérbe** azt a változót, ami a **legjobban szeparálja** a pozitív és negatív **példákat**
- ezt folytassuk rekurzív módon
- ha **csak pozitív vagy negatív példa van**, akkor **levélhez értünk, felcímkézzük** ezzel a levelet
- ha **üreshalmaz**, akkor a **szülő szerint többségi szavazattal címkézünk**
- ha **nincs több változó, de vannak negatív és pozitív példák is**, akkor szintén **többségi szavazattal címkézhetjük a levelet**

A legjobban szeparáló attribútumot az információtartalma, azaz entrópiája segítségével választhatjuk ki. 

### Naiv Bayes módszer

**Statisztikai következtetési módszer**, amely adatbázisban található példák alapján ismeretlen példákat osztályoz. 

Például emaileket akarunk spam vagy nem spamként osztályozni. Az emailben lévő szavakra meghatározzuk, hogy milyen valószínűséggel fordul elő egy normális üzenetben, vagy egy spam-ban. Ezután meg kell határozni, hogy milyen valószínűséggel kapunk normális üzenetet, és milyennel spam-et.

Legyen $A$ és $B_1,...,B_n$ a nyelvünk változói. (pl $A$ lehet igaz, ha az email spam, hamis ha nem, illetve a $B_i$ változó pedig az i. szó előfordulását jelezheti.
Tehát a feladat $b_1,...,b_n$ konkrét email esetében meghatázorzni, hogy $A$ mely értékekre lesz a $P(A|b_1,..,b_n)$ **feltételes valószínűség maximális**

Ezután, ha pl kíváncsiak vagyunk, hogy egy szókombinációt tartalmazó email spam vagy nem spam, a szókombinációban előforduló szavak valószínűségét össze kell szorozni, majd megszorozni azzal, hogy milyen valószínűséggel kaptunk normális emailt, és milyennel spam-et. Amelyik valószínűségre nagyobb értéket kapunk, abba az osztályba soroljuk a szókombinációt tartalmazó üzenetet.


### Modellillesztés

Lineáris regresszió?

### Mesterséges neuronhálók

A mesterséges neuron a következőképpen épül fel
- **Bemenet**: $x = [x_1,...,x_n]$ vektor
- **Súlyok**: $w = [w_1,...,w_n]$ súlyvektor
- $w_0$ bias weight, eltolássúly
- először minden bemeneti értéket megszorozza a hozzá tartozó súllyal, ezeket összeadja, majd kivonja belőle az eltolássúlyt
- majd a kapott értéken alkalmazzuk az **aktivációs függvényt**

Az aktivációs függvény célja, hogy 1-hez közeli értéket adjon, ha jó input érkezik, és 0-hoz közelit, ha rossz.

Példa aktivációs függvények:

- **küszöbfüggvény**: 0, ha az input <= mint 0, 1, ha nagyobb (perceptron)
- **szigmoid függvény:** $g(x) = 1/(1 +e^{-x})$
- **Rectifier aktiváció:** $g(x) = max(0, x)$ (ReLU)

Neuronokból hálózatokat szokás építeni. Egy hálózatnak lehet több rétege is. Van egy input, egy output és lehet több rejtett rétege is. Egy rétegen belül a neuronok között nincs kapcsolat, csak a rétegek között (előrecsatolt hálózatok). 

### k-legközelebbi szomszéd módszere
Adottak $(x_1,y_1),..,(x_n,y_n)$ példák.
Adott $x$-re az $y$-t az $x$-hez "közeli" példák alapján határozzuk meg. **Hogyan?**
1. Keressük meg $x$ ***k* legközelebbi szomszédját**
	- Leghasonlóbbakat nézzük a predikálandó egyedhez (hasonlósági függvény maximuma/távolság függvény minimuma).
	- Majd a *k* legközelebbi szomszéd osztálycímkéiből kiválasztja a leggyakoribbat és azt predikálja.