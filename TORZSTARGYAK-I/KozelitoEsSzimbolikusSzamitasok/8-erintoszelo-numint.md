# 8. Érintő, szelő, és húr módszer, a konjugált gradiens eljárás. Lagrange interpoláció. Numerikus integrálás

## Érintő, szelő, húrmódszer, konjugált gradiens eljárás

Mindegyik egyváltozós függvény zérushelyét keresi, iterációs módszerrel.

### Érintőmódszer

Más néven Newton-módszer

f(x)=0 egyenlet zérushelyét keressük, ez legyen x*

Ennek egy környezetében, ha f(x) differenciálható, válasszunk ebből a környezetből egy kezdőértéket

Az iteráció, amit használunk:

x_k+1 = x_k-f(x_k)/f'(x_k)

Magyarul, a következő megoldást úgy kapjuk, hogy az előző megoldásból kivonjuk a függvény x_k helyen felvett értékének és a függvény deriváltjának az x_k pontban felvett értékének a hányadosát.

Ha az f(x) függvény kétszer folytonosan differenciálható az x* egy környezetében, akkor van olyan pont, ahonnan indulva a Newton-módszer kvadratikusan konvergens sorozatot ad meg, aka gyorsan konvergál a megoldáshoz.

|x*-x_{k+1}| <= C|x*-x_k|^2

### Szelőmódszer

Legyen megint x* az f(x)=0 egyenlet egyszeres gyöke, és megint ezt keressük iterációval.

A függvény deriváltját nem mindig tudjuk, de a függvényt ki tudjuk értékelni minden helyen. Ekkor f' helyett használhatjuk az (f(x_k)-f(x_{k-1}))/(x_k-x_{k-1}) képletet.

Ekkor f' helyére a felső képletet behelyettesítve megkapjuk a szelőmódszer iterációs képletét:

x_{k+1} = x_k-f(x_k)*(x_k-x_{k-1})/(f(x_k)-f(x_{k-1}))

Azért szelőmódszer a neve, mert x_{k+1} az az (x_k, f(x_k})) és (x_{k-1}, f(x_{k-1})) pontokon átmenő egyenes és az x tengely metszéspontjának koordinátája.

Olyan x0, x1 kezdőértékekkel szokás indítani, amelyek közrefogják a gyököt, amit keresünk.

### Húrmódszer

A szelőmódszer egy változata.

Feltesszük, hogy a kezdeti x0, x1 pontokban az f(x) függvény ellentétes előjelű, és f(x_{k+1}) függvényében a megelőző két pontból azt választjuk, amivel ez a tulajdonság fennmarad.

### Konjugált gradiens eljárás

Szimmetrikus, pozitív definit mátrixú lineáris egyenletrendszerek megoldására alkalmas. Pontos számolásokkal véges sok lépésben megtalálná a megoldást, de a kerekítési hibák miatt iterációs eljárásnak veszik.

q(x) = 1/2x^TAx−x^Tb kvadratikus függvény minimumpontját keressük, mert ez ugyanaz, mint az eredeti egyenletrendszerünk megoldása, ha létezik.

Úgy keressük a következő közelítő megoldást, hogy van egy keresési irányunk, és egy lépésközünk, és az aktuális pontból lépünk ebbe az irányba ekkora lépésközzel egyet.

A negatív gradiensvektort nevezzük reziduális vektornak (erre csökken a függvényünk).
Ez lesz r = b-Ax.
A keresési irányban ott lesz a célfüggvény minimális ahol az új reziduális vektor merőleges az előző keresési irányra, szóval tudjuk pontosan, hogy hova kell lépnünk az adott irányban.

Tehát a konjugált gradiens módszer:

- meghatározzuk a lépéshosszt
- meghatározzuk az új közelítő megoldást (lépünk egyet az előző megoldásból az adott irányba az új lépéshosszal)
- ebből kiszámoljuk az új reziduális vektort
- és az új keresési irányt
- és kezdjük elölről

A megállási feltételünk lehet az, hogy az utolsó néhány iterált közelítés eltérése és a reziduális vektorok eltérése bizonyos kicsi határ alatt maradtak.

## Lagrange interpoláció

Függvényközelítéses módszer. Van pár alappontunk, és ezekre szeretnénk egy polinomot illeszteni. Ezek az alappontok legyenek páronként különbözőek.


Minden pontra felírunk egy egyenletet. Ahány alappontunk van, max annyiad fokú lesz a kapott polinomunk. Az egyenlet úgy fog kinézni, hogy ismerjük az x_i értéket, és mindenhova behelyettesítjük őket, és ezeknek az x_i^1, x_i^2, stb változóknak keressük az együtthatóját. Az egyenlet jobb oldalán pedig az f(x_i) értékek vannak.

Ebből kapunk egy lineáris egyenletrendszert, ahol az együtthatókat keressük. Ennek az egyenletrendszernek a mátrixa egy Vandermonde-mátrix lesz. Ebből következik, hogy pontosan egy polinom létezik, ami az adott pontokon áthalad.

A Lagrange-interpoláció az interpoláló polinomot a Szumma f(x_i)L_i(x) alakban adja meg.
L_i(x)-et úgy kapjuk, hogy egy nagy törtet veszünk - a számlálóban összeszorozzuk az összes x-x_j-t, ahol *j nem egyenlő i-vel*, tehát x-x_i szorzó kimarad belőle
A nevezőben pedig x_i-x_j-ket szorzunk össze, mindenhol, ahol j nem egyenlő i-vel szintén (különben nullával osztanánk).

## Numerikus integrálás

Határozott integrálokat akarunk közelíteni, úgynevezett kvadratúra formulákkal.

Q_n(f)-fel jelöljük, Q_n(f)=Szumma i=1-től n-ig w_i * f(x_i)

Általában feltesszük, hogy az összes x_i az \[a,b\] intervallumban van, ugye ebben az intervallumban keressük a határozott integrálját f-nek.
A w_i számokat pedig súlyoknak hívjuk.
Homogén és additív leképezés, azaz két függvény összegének a határozott integrálja a két függvény határozott integráljának az összege,
és egy függvény számszorosának határozott integrálja a függvény határozott integráljának számszorosa.

A határok szerinti additivitás fontos tulajdonság, tehát pl integrál a-tól b-ig az ugyanaz mint integrál a-tól c-ig plusz integrál c-től b-ig, ahol a < c < b

A kvadratúra-formula hibája a határozott integrál mínusz a kvadratúra formula kifejezéssel definiáljuk. Ha ez nulla, akkor pontos a kvadratúra formula.

Kvadratúra formula pontossági rendje az *r* természetes szám, ha az pontos az 1, x, x^2, x^3, ..., x^r hatványfüggvényekre, de nem pontos x^{r+1}-re. A rend meghatározása ekvivalens egy egyenletrendszer megoldásával. Ha az alappontokat (tehát x1, x2, stb) ismeretlennek tekintjük, akkor ez egy r+1 egyenletből álló egyenletrendszer (mert elmegyünk x^r-ig, plusz az x^0, azaz 1), amiben 2n változó van (n súly és n darab x).

Az n alappontos kvadratúra formula rendje legfeljebb 2n-1 lehet.
