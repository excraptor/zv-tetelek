
# 12. Teljes együttes eloszlás tömör reprezentációja, Bayes hálók. Gépi tanulás: felügyelt tanulás problémája, döntési fák, naiv Bayes módszer, modellillesztés, mesterséges neuronhálók, k-legközelebbi szomszéd módszere 

## Valószínűség
Problémák modellezésénél, megoldásánál szeretünk logikai változókat, és logikai következtetéseket használni. Ezzel problémák akadhatnak:

- Ha nem teljes a tudásunk
- Ha heurisztikai szabályokat vezetünk be, akkor a tapasztalat inkonzisztens lehet az elmélettel 

Vagyis a hiányos, részleges tudás kezelésére a logika nem optimális. A **tudás tökéletlenségének** a kezelésére a valószínűséget használjuk. Ilyenkor az **ismeretlen tényeket és szabályokat véletlen hatásként kezeljük.** 
Bayesi felfogásban a valószínűség a hit fokát, és nem az igazság fokát jelenti. (Szemben a fuzzy logikával, ahol pl: "ez a ház nagy" kijelentés folytonos igazságértéket vehet fel)  

**Véletlen változók:** 
- Van neve, és értékkészlete (domainje): logikai, diszkrét, folytonos. 
- **Elemi kijelentés:** $A$ vél.változó $D_A$ domainnel. Egy elemi kijelentés A értékének egy korlátozását fejezi ki (pl: $A = d$, ahol $d \in D_A$, amelyek a következő értékeket vehetik fel:
	- Logikai: Ekkor a Domain {Igaz, Hamis}
	- Diszkrét: Megszámlálható domain, pl {nap, eső, felhő, hó}
	- Folytonos: X véletlen változó, $D \subseteq \mathbb{R}$
- **Elemi esemény:** Minden véletlen változóhoz értéket rendel. Ha az $A_1 ...A_n$ véletlen változókat definiáltuk a $D_1 ... D_n$ domainekkel, akkor az elemi események (lehetséges világok) halmaza a $D_1 \times ... \times D_n$ halmaz. Vagyis egy "lehetséges világban" --- **elemi eseményben** az $A_i$ változó a hozzá tartozó $D_i$ ből **pontosan egy értéket vesz fel.**  

**Fenti definíciók pár következménye:**
1. Minden lehetséges világot pontosan egy **elemi esemény** írja le.
2. Egy **elemi esemény** természetes módon minden lehetséges **elemi kijelentéshez igazságértéket rendel**
3. Minden **kijelentés** logikailag ekvivalens a neki nem ellentmondó elemi eseményeket leíró kijelentések halmazával.

**Valószínűség, kijelentések:**  
 A valószínűség egy függvény, ami egy kijelentéshez egy valós számot rendel.  $P(a)$ az $a$ kijelentés valószínűsége. Minden kijelentés elemi események egy  halmazával  ekvivalens. **Egy kijelentés valószínűsége egyenlő a vele konzisztens elemi események valószínűségének az összegével.** (Ehhez kell a teljes együttes eloszlás, ami megadja az összes elemi esemény valószínűségét) 

**Feltételes valószínűség**
$$P(A|B) = \dfrac{P(A \cap B)}{P(B)}$$

**Kazualitás:**
Okszerűség, okozati kapcsolat
Pl: Fogfájás nem hat az időjárásra, tehát ott független, de az Időjárás hathat a Fogfájásra, ezért nem beszélhetünk mégsem függetlenségről $\Rightarrow$ a Fogfájás ténye adhat infót az Időjárásról.

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

$P(A_1,..., A_n) = P(A_1)...P(A_n)$

**Feltételes függetlenség**
Az abszolút függetlenség ritka. Ezért használhatunk feltételesen függetlenséget.
$a$ és $b$ kijelentések **feltételesen függetlenek** $c$ feltevésével, akkor és csak akkor, ha $P(a \wedge b | c) = P(a|c)*P(b|c)$. Tipikus eset, ha $a$ és $b$ közös oka $c$.
Pl: fogfájás és a beakadás közös oka a luk.


**Naiv-Bayes modell alakja**
Ha $A$ feltevése mellett $B_1,...,B_n$ kölcsönösen függetlenek, akkor 
$P(B_1, . . . , B_n|A) = \prod_{i=1}^{n} P(B_i|A)$. ha ez igaz, akkor ez a *Naiv-Bayes modell alakja*, ami a következőképp definiálható:
$P(B_1, . . . , B_n,A) = P(A)\prod_{i=1}^{n} P(B_i|A)$,
**Ezzel $O(n)$ tömörítés érhető el**

### Bayes szabály/tétel $a$ és $b$ kijelentésekre

$$P(a|b) = \dfrac{P(b|a)P(a)}{P(b)}$$
ez következik a feltételes valószínűség képletéből: 
$P(a|b) = \dfrac{P(a \cap b)}{P(b)}$ 
alapján
$P(a|b)P(b) = P(a\cap b) = P(b|a)P(a)$
amiből a P(b)-vel leosztva adódik a tétel.

### Bayes hálók

A feltételes függetlenség hasznos, mert tömöríthetjük a teljes együttes eloszlást.
A teljes együttes eloszlás feltételes függetlenségeit ragadja meg és ezekből egy **speciális gráfot** definiál. Ez tömör és intuitív reprezentációt tesz lehetővé.

Bayes háló esetén alkalmazunk **láncszabályt**, ami azt jelenti, hogy a **teljes együttes eloszlást** (amit majd tömöríteni szeretnénk) **feltételes eloszlások szorzataként** jeleníti meg.
Formailag:
$$P(X_1, . . . , X_n) = \prod_{i=1}^{n} P(X_i|X_{i+1},...,X_n)$$

Ezután az egyes feltételes valószínűségelből elhagyhatunk változókat, azaz minden $P(X_i | X_{i+1},..,X_n)$ tényezőre az $\{X_{i+1},..,X_n\}$ változókból vegyünk egy $Szulok(x_i)$.
Ebből tudunk tömöríteni, mivel a Szülők halmaz minimális.
$$P(X_1, . . . , X_n) = \prod_{i=1}^{n} P(X_i|\text{Szülő}(X_i))$$ (ez a bayes háló)
**Ez a teljes eloszlás tömörített reprezentációja.**
Ezt lehet egy gráf formájában vizualizálni.
Például az $X_i$ változókat fel lehet venni mint a gráf csomópontjai, a $Szulok(X_i)$ halmaz elemeiből pedig éleket lehet húzni az $X_i$ változó felé.
**Ez a gráf irányított körmentes gráf lesz.**  

"Tegyük fel" hogy nem érted a fenti matekot. Józan paraszti megmagyarázása a Bayes hálóknak:  
A Bayes hálóval változók egy halmazát, és a köztük lévő feltételes függőségeket reprezentáljuk egy irányított, körmentes gráffal. Ideális olyan feladatra, ahol egy bekövetkezett eseményből próbáljuk meg megbecsülni az ő "okát". Pl: Kap egy csomó tünetet, Bayes hálóval képesek vagyunk megbecsülni az őt okozható betegségeknek a valószínűségeit. 
Bayes háló $O(n*2^k)$ tud tömöríteni. ahol $k$ a szülők száma. $n$ pedig a node-ok száma, ellenben az $O(2^n)$ el szemben.

#### Bayes háló konstruálás
Sok esetben definiálva vannak a **változók** és a **hatások** a változók között, és szakértőkkel kitöltjük az empirikus tudás segítségével a változókhoz tartozó **feltételes eloszlásokat.** Ilyenkor nem az **eloszlásból**, hanem az intuitív reprezentáció adott, ami definiál egy **teljes együttes eloszlést**, amit felhasználhatunk következtetésre.

Fontos, hogy a **láncszabály** esetén rögzített változósorrendtől függ a Bayes háló alakja.

#### Függetlenség és Bayes háló
Ahhoz, hogy egy random node-ra megmondjuk, hogy milyey függetlenségi informáicója van, a **Markov-takarót** tudjuk használni.
Pl: $X$ markov takarója az a halmaz, amely $X$ szülőinek, $X$ gyerekeinek és $X$ gyerekei szülőinek az uniója. 

## Gépi tanulás: felügyelt tanulás problémája, döntési fák, naiv Bayes módszer, modellillesztés, mesterséges neuronhálók, k-legközelebbi szomszéd módszere

### Felügyelt tanulás problémája

Tapasztalati tények felhasználása arra, hogy egy racionális ágens teljesítményét növeljük.

#### Felügyelt tanulás
Egy $f: X \rightarrow Y$ függvényt keresünk, amely illeszkedik adott példákra. A **példák** $((x_1,f(x_1)),..,(x_n,f(x_n)))$ alakban adottak. ($x_i \in X$)
Pl. $X$: Emailek halmaza $Y$ {spam, -spam}


##### Modellillesztés (rész szerintem)
Mivel az $f$ függvényt általában nem ismerjük, ezért a feladat az, hogy **keresünk egy $h: X\rightarrow Y$ függvényt amely $f$-et közelíti**

A $h$ függvény **konzisztens** az adatokkal, ha $h(x_i) = f(x_i)$ minden példára. 
Ezt a $h$ függvényt mindig egy $H$ hipotézistérben keressük, azaz **egy függvényt mindig adott alakban keressük**.
Gyakorlatban elég, ha $h$ elég közel van a példákhoz, mivel sokszor hibás, vagy zajos a tanuló példa, ezért káros lehet $\rightarrow$ túltanulás következhet be pontos illeszkedés esetén.

Példa.
Az a $h$, amelyre $h(x) = f(x)$ minden példára, egyébént $h(x)=0$, az tökéletesen megtanulja a példákat, de lehető legrosszabban általánosít. Ez a **magolás**

A magolási probléma miatt **tömör reprezentációra** kell törekedni, lehetőleg tömörebb mint a példák listája. Ez az **Occam borotvája elv:** Ha más alapján nem tudunk választani, akkor a lehető legtömörebb leírást kell venni.
Tehát, hogy a fenti tulajdonságot elérjük fontos a $H$ hipotézistér gondos meghatározása.

 A **priori ismeretek fontossága:** A **tabula rasa** (tiszta lappal történő indulás) tanulás a fentiek szerint lehetetlen. A $H$ halmaz és az algoritmus maga a priori ismeretek alapján kerülnek megtervezésre.
### Döntési fák
**Induktív (felügyelt) tanulás konkrét példája.**
Feltesszük, hogy $x\in X$-ben diszkrét változók egy vektora van, $f(x)\in Y$-ban pedig szintén valami diszkrét változó egy értéke, pl $Y = \{igen, nem\}$

Mivel $Y$ véges halmaz, osztályozási feladatról beszélünk, ahol $X$ elemeit kell osztályokba sorolni, és az osztályok $Y$ értékeinek felelnek meg. (Ha $Y$ folytonos, akkor regresszióról beszélünk.)

*Tulajdonképpen osztályozás, $X$ **elemeit** kell $Y$ valamelyik **osztályába** sorolni.*

**Előnye**, hogy döntései megmagyarázhatók, mert emberileg értelmezhető lépésekben jutottunk el odáig.

**Kifejezőereje megegyezik az ítéletkalkuluséval.**
Mivel vannak valamilyen **ítéletek** (változó értékadások), egy **modell** (egy $x\in X$ változóvektor), és egy **formula** (döntési fából adódoan).
**Fa $\Rightarrow$ formula:** Vesszük az összes olyan levelet amelyen igen címke van, és az oda vezető utakban "és"-el összekötjük az éleket, és az utakat "vagy"-gyal összekötjük.

**Formula $\Rightarrow$ fa:** A logikai formula igazságtábláját fel lehet írni fa alakban, ha vesszük a változók $A_1,..,A_n$ felsorolását, az $A_1$ a gyökér, értékei az élek (i/h általában), és az $i$ edik szinten a fában minden pontban $A_i$ van. 

**Döntési fa építése:**
adottak **pozitív és negatív példák felcímkézve**, tipikusan több száz (pl: Vendégek = tele, Várakozás = 10-30, Éhes=igen)
1. vegyük a **gyökérbe** azt a változót, ami a **legjobban szeparálja** a pozitív és negatív **példákat**. A legjobban szeparáló attribútumot az információtartalma, azaz entrópiája segítségével választhatjuk ki
2. Aztán ezt folytassuk **rekurzív** módon a gyerekein, tehát **nem rögzített változókból** választunk egy gyökeret a következő **részfához**

Speciális esetek amik megállítják a **rekurziót:**
- ha **csak pozitív vagy negatív példa van**, akkor **levélhez értünk, felcímkézzük** ezzel a levelet
- ha **üreshalmaz**, akkor a **szülő szerint többségi szavazattal címkézünk**
- ha **nincs több változó, de vannak negatív és pozitív példák is** (valszeg zajjal terhelt az adat), akkor szintén **többségi szavazattal címkézhetjük a levelet**

**entrópia:** $- \Sigma_i \ p_i \ log\ p_i$, 
ahol $\Sigma_i\ p_i = 1$, amelynek minimuma 0, ami a maximális rendezettséget jelöli.


### Naiv Bayes módszer

**Statisztikai következtetési módszer**, amely adatbázisban található példák alapján ismeretlen példákat osztályoz. 

Például emaileket akarunk spam vagy nem spamként osztályozni. Az emailben lévő szavakra meghatározzuk, hogy milyen valószínűséggel fordul elő egy normális üzenetben, vagy egy spam-ban. Ezután meg kell határozni, hogy milyen valószínűséggel kapunk normális üzenetet, és milyennel spam-et.

Legyen $A$ és $B_1,...,B_n$ a nyelvünk változói. (pl $A$ lehet igaz, ha az email spam, hamis ha nem, illetve a $B_i$ változó pedig az i. szó előfordulását jelezheti.
Tehát a feladat $b_1,...,b_n$ konkrét email esetében meghatázorzni, hogy $A$ mely értékekre lesz a $P(A|b_1,..,b_n)$ **feltételes valószínűség maximális**
Ehhez a következő átalakításokat illetve függetlenségi feltevéseket tesszük:
$P(A|b_1,..,b_n) = \alpha P(A)P(b_1,...,b_n|A) \approx \alpha P(A)\prod_{i=1}^{n}P(b_i|A)$.
Itt az első egyenlőségjel a Bayes tétel alkalmazása, ahol $\alpha = 1/P(b_1,...,b_n)$. Mivel csak $A$ értékei közötti sorrendet keresünk, és $\alpha$ nem függ $A$-tól, az $\alpha$értéke nem érdekes.
A második pedig a naiv Bayes feltevést fogalmazza meg. Nem biztos, hogy teljesül az egyenlőség viszont könnyen tudunk adatbázisból valószínűségeket számolni.

Fontos kiemelni, hogy a szavakat nem nézzük milyen sorrendbe irjuk fel. pl a "Dear Friend" és a "Friend Dear" is ugyanakkora értéket fog kapni. **Nem tesz fel közöttük semmilyen függöséget.**

Ha akarunk **tesztelni egy adott kérdést**, hogy pl azok a szavak az adott levélben spam/nem spam, akkor felírjuk hozzá a fenti képlettel **mindkettő esetben** a valószínűséget, és **amelyikhez közelebb van oda fog kerülni**.
Amennyiben az egyik szó nincs a másik szótárában, akkor az automatikusan 0 valószínűséget fog felvenni, ezért néha adnak hozzá minden szó előforduláshoz egy $\alpha$ számot, tipikusan 1-et

### Modellillesztés

Sztem már leirtam fentebb szóval igazából a tanuló példákra illesztett $h$ függvény. Lásd felügylet tanulás

### Mesterséges neuronhálók

A mesterséges neuron a következőképpen épül fel
- **Bemenet**: $x = [x_1,...,x_n]$ vektor
- **Súlyok**: $w = [w_1,...,w_n]$ súlyvektor
- $w_0$ bias weight, eltolássúly
- $x_0$ pedig fix bemenet, mindig $-1$
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
2. $h(x)$ éréke ezen szomszédok $y$-jainak átlaga (esetleg távolságga súlyozva) ha $y$ folytonos, 
 ha diszkrét, akkor pl. többségi szavazás

A legközelebbi szomszédot többféleképpen is meglehet nézni.
1. Diszkrét esetben Hammington távolság: különböző jellemzők száma
2. Folytonos esetben eukildeszi távolság, vagy manhattan távolság.

