# 7. Eliminációs módszerek, mátrixok trianguláris felbontásai. Lineáris egyenletrendszerek megoldása iterációs módszerekkel. Mátrixok sajátértékeinek és sajátvektorainak numerikus meghatározása


## Eliminációs módszerek

### Gauss-elimináció

- Ax=b alakú lineáris egyenletrendszerek megoldásához tudjuk használni
- az Ax=b egyenletrendszernek pontosan akkor van egy megoldása, ha det(A) nem 0
- ekkor x = A^-1b
    - de az inverzet kiszámolni túl lassú lenne

A Gauss-eliminációval az A mátrixot felső háromszögmátrixszá alakítjuk, és ha ez sikerül, akkor abból visszahelyettesítésekkel megkaphatjuk x-et. Műveletigénye O(n^2/2).

A felső háromszögmátrixot ún. eliminációs mátrixok segítségével kapjuk meg. Egy eliminációs mátrix dolga, hogy kinullázza az A mátrix egyik oszlopában a főátló alatti elemeket. Ha az összes ilyen eliminációs mátrixot összeszorozzuk balról egymással, akkor kapjuk az M mátrixot. Ekkor az MA szorzás eredménye lesz a kívánt felső trianguláris mátrix.

### LU felbontás

Az LU felbontás lényege, hogy az A mátrixot egy alsó és egy felső háromszögmátrixra bontjuk. A Gauss eliminációhoz nagyon hasonlít, ott az MA szorzás eredménye egy U felső trianguláris mátrix volt. Ha mindkét oldalt megszorozzuk balról M^-1-gyel, akkor azt kapjuk, hogy A = M^-1U. Legyen M^-1=L, mert M^-1 egy alsó trianguláris mátrix. Ezzel elvégeztük az A mátrix LU felbontását.

Ekkor az Ax=b egyeletrendszer megoldását a következőképpen kaphatjuk:

- Ax=b
- LUx=b
- y = Ux
- Ly=b
- y = L^-1b
- L^-1b = Ux

### Cholesky felbontás

Ha az A mátrix

- szimmetrikus
- pozitív definit
    - minden sajátértéke pozitív

akkor felbontható a következőképpen: A=LL^T, tehát U az most pont L transzponáltja lesz.

### QR felbontás

Ha az A mátrix

- négyzetes
- valós
- reguláris (det(A) nem  0)

akkor létezik QR felbontása.

Q egy úgynevezett ortogonális mátrix (és négyzetes is). Ez azt jelenti, hogy Q^TQ = QQ^T = I.
R egy felső háromszögmátrix

Bizonyítás:
A^TA pozitív definit, így létezik R^TR Cholesky felbontása.

Legyen ekkor Q egyenlő A^R-1-gyel.

Igazoljuk, hogy Q ortogonális.

Q^TQ = (AR^-1)^T\*(A^R^-1) = (R^-1)^T\*A^T\*A\*R^-1 = (R^-1)^T\*R^T\*R\*R^-1 = I\*I = I
        behelyettesítés     transzponálásos azonosság  A^TA=R^TR           inverzek kiütik egymást

Tehát Q valóban ortogonális.

## Lineáris egyenletrendszerek megoldása iterációs módszerekkel

### Jacobi iteráció

Átrendezzük úgy az egyenletrendszert, hogy a baloldalon egy-egy változót kifejezünk

Választunk valami indulóvektort, ami ilyen kezdő megoldás kb
A vektor elemeit behelyettesítjük a jobboldalra, és ebből kapunk egy új vektort a baloldalon, ezzel folytatjuk.

Csak akkor konvergál, ha a mátrix *szigorúan diagonálisan domináns*, vagyis az összes főátlóbeli elem abszolút értéke a legnagyobb az adott sorban.

### Gauss-Sediel iteráció

Ugyanaz, mint a Jacobi, csak ha már egy változó új értékét kiszámoltuk, akkor a következő sorokban már azt az új értéket használjuk. 

## Mátrixok sajátértékeinek és sajátvektorainak numerikus meghatározása

### Sajátérték, sajátvektor

Ax = lambda x

x a sajátvektor, lambda a sajátérték

A sajátérték olyan szám, amivel ha megszorozzuk a hozzá tartozó sajátvektort, akkor ugyanazt az eredményt kapjuk, mintha azt a vektort a mátrixszal szoroztuk volna meg.

Meghatározása: det(A - lambdaI) = 0
tehát, a főátló minden eleméből kivonunk lambdát, és ennek a mátrixnak keressük a determinánsát
ez egy polinomot fog eredményezni, amiben lambdák a változók, és ennek a polinomnak a gyökei lesznek a sajátértékek

Ezt a polinomot nevezzük a mátrix *karakterisztikus polinomjának*.
Valós mátrixnak is lehetnek komplex sajártértékei!

A mátrix sajártértékeinek a halmazát a mátrix *spektrumának* hívjuk.

### Hatványmódszer

A hatványmódszer a legnagyobb abszolútértékű sajátérték meghatározására szolgál.
Iterációs módszer.

y^k = Ax^k
x^(k+1) = y^k/||y^k||

a kiindulási x vektor ne legyen a nullvektor, és nem lehet merőleges a legnagyobb abszolútértékú sajátértékhez tartozó sajátvektorra.

A k betűk a kitevőben a k. iterációt jelentik, nem k. hatványt.

### Inverz hatványmódszer

Ay=x^k
x^(k+1) = y/||y||

Az inverz hatványmódszer azon a felismerésen alapul, hogy ha az A mátrix sajátértéke lambda, és a hozzá tartozó sajátvektor x, akkor A^-1 egy sajátértéke lambda^-1, és a hozzá tartozó sajátvektor x.


