
# 8. Érintő, szelő, és húr módszer, a konjugált gradiens eljárás. Lagrange interpoláció. Numerikus integrálás

## Érintő, szelő, húrmódszer, konjugált gradiens eljárás

Mindegyik egyváltozós függvény zérushelyét keresi, iterációs módszerrel.

### Érintőmódszer

Más néven Newton-módszer

$f(x)=0$ egyenlet zérushelyét keressük, ez legyen $x*$

Ennek egy környezetében, ha $f(x)$ differenciálható, válasszunk ebből a környezetből egy kezdőértéket

Az iteráció, amit használunk:

$x_{k+1} = x_k - \dfrac{f(x_k)}{f'(x_k)}$

Magyarul, a következő megoldást úgy kapjuk, hogy **az előző megoldásból kivonjuk a függvény $x_k$ helyen felvett értékének és a függvény deriváltjának az $x_k$ pontban felvett értékének a hányadosát.** $\rightarrow$ Ezzel képezzük az adott ponthoz húzott *érintőt*.

Ha az $f(x)$ függvény kétszer folytonosan differenciálható az $x^*$ egy környezetében, akkor van olyan pont, ahonnan indulva a Newton-módszer **kvadratikusan konvergens** sorozatot ad meg, **aka gyorsan konvergál a megoldáshoz**.

$|x*-x_{k+1}| <= C|x*-x_k|^2$

### Szelőmódszer
A Newton módszer hátránya, hogy szükség van a **deriváltak** kiszámítására $\rightarrow$ költséges.

Legyen megint $x^*$ az $f(x)=0$ egyenlet egyszeres gyöke, és megint ezt keressük numerikus iterációval.

A függvény deriváltját nem mindig tudjuk, de a függvényt ki tudjuk értékelni minden helyen. Ekkor $f'(x_k)$ helyett használhatjuk az numerikus deriváltat. 
$f'(x_k)$ =$\dfrac{f(x_k)-f(x_{k-1})}{x_k-x_{k-1}}$

Ekkor $f'$ helyére a felső képletet behelyettesítve megkapjuk a szelőmódszer iterációs képletét:

$x_{k+1} = x_k- \dfrac{f(x_k)*(x_k-x_{k-1})}{f(x_k)-f(x_{k-1})}$

Azért szelőmódszer a neve, mert $x_{k+1}$ az az $(x_k, f(x_k))$ és $(x_{k-1}, f(x_{k-1}))$ **pontokon átmenő egyenes és az x tengely metszéspontjának koordinátája.**

Olyan $x_0, x_1$ **kezdőértékekkel szokás indítani, amelyek közrefogják a gyököt,** amit keresünk.

### Húrmódszer

A szelőmódszer egy változata.

Feltesszük, hogy a kezdeti $x_0, x_1$ pontokban az $f(x)$ függvény ellentétes előjelű, és $f(x_{k+1})$ függvényében a megelőző két pontból azt választjuk, amivel ez a tulajdonság fennmarad.

### Konjugált gradiens eljárás
Az eljárás olyan lineáris ($Ax = b$ alakú) egyenletrendszerek megoldására alkalmaz, ahol az $A$ **együtthatómátrix szimmetrikus** ($A = A^T$), **pozitív definit** ($\forall x \ne 0$ $x^T Ax > 0$) és **valós** ($A \in \mathbb{R}^{n*n}$). 
Pontos számolásokkal véges sok lépésben megtalálná a megoldást, de a **kerekítési hibák miatt iterációs eljárásnak veszik**.

**Gradiens:** Változók parciális deriváltjai vektorba rendezve. Van iránya és nagysága.
Ismert, hogy a többváltozós függvények gradiensvektorával ellentétes irányban csökken a leggyorsabban.

$q(x) = \dfrac{1}{2}x^TAx−x^Tb$ kvadratikus függvény minimumpontját keressük, mert ez ugyanaz, mint az eredeti egyenletrendszerünk megoldása, ha létezik.

Úgy keressük a következő közelítő megoldást, hogy van egy **keresési irányunk ($s_k$)**, és egy **lépésközünk ($\alpha$)**, és az aktuális pontból lépünk ebbe az irányba ekkora lépésközzel egyet.

A **negatív gradiensvektort** nevezzük **reziduális vektornak** (erre csökken a függvényünk).
**Ez lesz $r = b-Ax$.**
A keresési irányban ott lesz a **célfüggvény minimális ahol az új reziduális vektor merőleges az előző keresési irányra**, szóval tudjuk pontosan, hogy hova kell lépnünk az adott irányban.

**Tehát a konjugált gradiens módszer:**
- meghatározzuk a lépéshosszt
- meghatározzuk az **új közelítő megoldást** (lépünk egyet az előző megoldásból az adott irányba az új lépéshosszal ($\alpha$))
- ebből kiszámoljuk az új reziduális vektort
- Kiszámolunk egy segédváltozót
- és az új keresési irányt a segédváltozóval
- és kezdjük elölről

A megállási feltételünk lehet az, hogy az utolsó néhány iterált közelítés eltérése és a reziduális vektorok eltérése bizonyos kicsi határ alatt maradtak.

## Lagrange interpoláció

**Függvényközelítéses módszer.** Van pár alappontunk, és ezekre szeretnénk egy polinomot illeszteni. Ezek az **alappontok legyenek páronként különbözőek.**

Minden pontra felírunk egy egyenletet. **Ahány alappontunk van, max annyiad fokú lesz a kapott polinomunk**. Az egyenlet úgy fog kinézni, hogy ismerjük az $x_i$ értéket, és mindenhova behelyettesítjük őket, és ezeknek az $x_i^1, x_i^2$, stb változóknak keressük az együtthatóját. Az egyenlet jobb oldalán pedig az $f(x_i)$ értékek vannak.

Ebből kapunk egy lineáris egyenletrendszert, ahol az együtthatókat keressük. Ennek az egyenletrendszernek a mátrixa egy Vandermonde-mátrix lesz. Ebből következik, hogy pontosan egy polinom létezik, ami az adott pontokon áthalad.

A Lagrange-interpoláció az interpoláló polinomot a $\sum_{i=1}^n f(x_i)L_i(x)$ alakban adja meg.
$L_i(x)$-et úgy kapjuk, hogy egy nagy törtet veszünk - a **számlálóban összeszorozzuk** az összes $x-x_j$-t, ahol *j nem egyenlő i-vel*, tehát $x-x_i$ szorzó kimarad belőle
A **nevezőben pedig $x_i-x_j$-ket szorzunk össze**, mindenhol, ahol j nem egyenlő i-vel szintén (különben nullával osztanánk).

## Numerikus integrálás
**Határozatlan integrál:**
$\int f(x) = F(x)dx$,
ahol $F'(x) = f(x)$ (deriválás megfordítása). **$F(x)$-et primitív függvénynek nevezzük.**

**Határozott integrál:** Célja, hogy egy adott $f(x)$ függvénynek adott $[a,b]$ intervallumon szeretnénk a **görbe alatti (előjeles) területét** kiszámítani.
$\int_a^b f(x)dx=F(b)-F(a).$ (Newton-Leibnz formula)

A fenti formula közelítése a cél, tehát **adott egy $f(x)$ függvény határozott integrálját szeretnénk megközelíteni az $[a,b]$ intervallumon**

### **Kvadratúra formulák:**

$Q_n(f)$-fel jelöljük, $Q_n(f)=\sum_{i = 1}^nw_i f(x_i)$ azaz, ==**az alappontokon felvett függvényérték $w_i$ szerinti súlyozott összege.**==

- Veszünk $x_1,..,x_n$ alappontokat, általában feltesszük, hogy az összes $x_i$ az \[a,b\] intervallumban van, ugye ebben az intervallumban keressük a határozott integrálját f-nek.
- A $w_i$ számokat pedig súlyoknak hívjuk, amiket minden $x_i$ alapponthoz hozzárendelünk.

**Téglalap szabály:**
Amennyibe **csak egy alappontot** veszünk, az $x_1 = \dfrac{a+b}{2}$ felezőpontot és a hozzárendelt $w_i$ súly az intervallum mérete, azaz $b-a$ lesz

**Tétel:** A $Q_n$ $n$ alappontos kvadratúra-formula rendje legfeljebb 2n-1 lehet

### **Interpolációs kvadratúra-formulák:**
**A téglalap szabálynál veszünk egy $x_1$ alappontot és erre illesztünk egy polinomot, és ennek a polinomnak a határozott integrálják vesszük.**

amennyiben, ha egy kvadratúra formula megkapható a következő alakban:
- Meghatározzuk a módszertól függően az $x_1,...,x_n$ alappontokat,
- A kvadratúra-formula értéke az $(x_i,f(x_i))$ pontokra illesztett Lagrange-interpolációs polinom $[a,b]$-n vett integrálja.

**Lagrange-interpolációs polinom:** Az $(x_i, f(x_i))$ pontokra illesztett polinomok előállnak a következő alakban: $\sum_{i=1}^n f(x_i)L_i(x)$, ahol $L_i(x)$ az i-edik Lagrange-alappolinom.

A súlyok: $w_i = \int_a^b L_i(x)dx$

### Newton-Cotes formulák
Ha az $[a,b]$ intervallumot elosztjuk **ekvidisztánsan** (egyforma méretű intervallumokra), és ezek végpontjait választjuk alappontoknak.
Ezek a Newton-Cotes formulák. Lehet **nyitott** és **zárt** attól függően, hogy $a$ és $b$ alappontok lehetnek-e.
**Nyitott esetén:** n+1 egyenlő részre kell osztani az intervallumot
**Zárt esetén:** n-1 egyenlő részre kell osztani az intervallumot

**Trapéz szabály:**
pl: A legegyszerűbb esetben két alappontunk van és erre a két alappontra egy elsőfokú polinomot tudunk majd illeszteni.
Felvesszük a pontokat (pl: $x_1$ = $a$  $x_2$ = $b$), meg a súlyt ami $w_1 = w_2 = \dfrac{b-a}{2}$, azaz $(f(a)+f(b))*\dfrac{b-a}{2}))$

### Összetett kvadratúra-szabályok
Az $[a,b]$ intervallumokat felbontják $n$ egyforma részre, és ezekre külön-külön csinálnak egy kvadratúra formulát.
