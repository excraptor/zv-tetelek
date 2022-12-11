
# 14. Primál-duál feladatpár, dualitási komplementaritási tételek, egész értékű feladatok és jellemzőik, a branch and bound módszer, a hátizsák feladat

## Primál-duál feladatpár



| Primál   | Duál      |
|----------|-----------|
| max $c^Tx$ | min $b^Ty$ |
| $Ax \le b$  | $A^Ty \ge c$ |
| $x \ge 0$    | $y \ge 0$      |

**A primál feladat**
- maximalizálunk
- $c^T$ a célfüggvény együtthatóinak a vektora
- $A$ az együtthatók mátrixa
- $b$ a konstansok vektora

**A duál feladat**
- minimalizálunk
- $b^T$ a célfüggvény együtthatóinak a vektora
- $A^T$ az együtthatók mátrixa
- $c$ a konstansok vektora
- <=-ket >=-re cseréljük

**A duál feladat duálisa az eredeti primál feladat**

Ahhoz, hogy duál feladatot megkapjuk a primálból a **következő lépéseket kell megtenni:**
- Transzponáljuk az A mátrixot
- *cseréljük fel* $b$ és $c$ vektorok szerepét
- cseréljük az egyenlőtlenségeket $\ge$-re
- Max helyett Min feladat

Gazdaásgi értelmezése: Tegyük fel, hogy az LP feladatunk **korlátozott erőforrások mellet maximális nyereséget célzó gyártási folyamat modellje**. 
A duál feladat megoldásában az $y_i^*$ a primál feladat $i$ erőforrásához tartozó piaci ár, amit **marginális ár / árnyék ár**-nak nevezünk.
- Ez az **errőforrás értéke** az LP megoldójának a szemszögéből
- Az $i$ erőforrás mennyiségénk az egységnyi növelésével éppen $y_i^*$ gal nő a nyereség.
- Viszont ha túl sok van egy erőforrásból, az nem érhet sokat.
- Továbbá $y_i^*$-nál többet **már nem érdemes fizetni az $i$ erőforrásért**, míg kevesebbet igen.


## Dualitási komplementaritási tételek

### Gyenge dualitás
Ha $x = (x_1,...,x_n)$ **lehetséges megoldása** a primál feladatnak és $y = (y_1,...,y_n)$ **lehetséges megoldása** a duál feladatnak, akkor 
$$c^Tx \le b^Ty$$
**Vagyis a duális feladat bármely lehetséges megoldása felső korlátot ad a primál bármely lehetséges megoldására.**


### Erős dualitás
Ha $x^* = (x_1^*,...,x_n^*)$ **optimális megoldása** a primál feladatnak, akkor a duál feladatnak is van **optimális megoldása** $y^* = (y_1^*,...,y_n^*)$, és a célfüggvényük megegyezik, azaz
$$c^Tx^* = b^Ty^*$$

Ha valamelyik i. feltétel egyenlet nem éles, azaz nem pontosan egyenlő a két oldal, akkor a kapcsolódó duál változó biztosan 0. Ha egy primál változó pozitív, akkor a kapcsolódó duális feltétel biztosan éles.

#### Korlátosság és megoldhatóság
**A korlátosság és a megoldhatóság nem függetlenek egymástól**

- Ha a **primál nem korlátos**, akkor a **duálnak nincs lehetséges megoldása és fordítva**.
- Lehet, hogy egyiknek sincs lehetséges megoldása.
- Ha mindkettőnek van, akkor mindkettő korlátos
- A primál és a duál feladat egyidejű optimalitása ellenőrizhető.

#### Komplementáris lazaság

Ha a primál-duál feladatpár
| max $c^Tx$| min $b^Ty$|
|----------|-----------|
| $Ax \le b$  | $A^Ty \ge c$ |
| $x \ge 0$    | $y \ge 0$      |

Akkor azt mondjuk, hogy $x = (x_1,..,x_n)$ és $y=(y_1,..,y_m)$ komplementárisak, ha $y^T(b-Ax) = 0$ és $x^T(A^T-c) = 0$

Vagyis: 
- Ha $y_i > 0$, akkor az $x$-et az $i$-edik egyenletbe helyettesítve egyenlőséget kapunk
- Ha $x_i >0$, akkor $y$-t a duális feladat $i$-edik egyenletébe helyettesítve az egyenlőség teljesül.

**Tétel**
Tegyük fel, hogy $x$ a primál feladat optimális megoldása.
- Ha $y$ a duál optimális megoldása, akkor $x$ és $y$ komplementáris.
- Ha $y$ lehetséges megoldása a duálisnak és komplementáris $x$-szel, akkor $y$ optimális megoldása a duálnak
- Létezik olyan lehetséges $y$ megoldása a duálnak, hogy $x$ és $y$ komplementáris

**Ergo, ha van ilyen $x$ és $y$ vektor, amik a fenti "Vagyis"-ra teljesülnek, akkor az fixen optimális megoldása a primál-duál feladatpárnak**
## Egész értékű feladatok és jellemzőik

Tiszta egészértékű feladat (Integer Programming)

- Minden változónak egésznek kell lennie a megoldásban.

Vegyes egésztértékű programozási feladat (Mixed Integer Programming)

- Csak néhány változóra követeljük meg, hogy egész legyen 

0-1 IP

- minden változó értéke csak vagy 0 vagy 1 lehet

LP lazítás

Egészértékű programozási feladat LP lazítása az az LP, amelyet úgy kapunk, hogy a változókra tett minden egészértékűségi vagy 0-1 megkötést eltörlünk.

- Bármelyik IP lehetséges megoldáshalmaza része az LP lazítás lehetséges megoldástartományának
- Maximalizálásnál az LP lazítás optimum értéke nagyobbegyenlő, mint az IP optimumértéke
- Ha az LP lazítás lehetésges megoldáshalmazának minden csúcspontja egész, akkor van egész optimális megoldása, ami az IP megoldása is egyben
- Az LP lazítás optimális megoldása bármilyen messze lehet az IP megoldásától.

## Branch and bound módszer

1. lépés

Megoldjuk az LP lazítást, ha a megoldás egészértékű, akkor done

2. lépés

Ha van lezáratlan részfeladatunk, akkor azt egy xi nem egész változó szerint két részfeladatra bontjuk.
Ha $x_i$ értéke $x_i^*$, akkor $x_i \le floor(x_i^*)$ és $x_i \ge ceil(x_i^*)$ feltételeket vesszük hozzá egy egy részfeladatunkhoz

- a részproblémákat egy fába rendezzük
- a gyökér az első részfeladat, az LP lazítás
- a leszármazottai az ágaztatott részproblémák
- a hozzávett feltételeket az éleken adjuk meg
- a csúcsokban jegyezzük az LP-k optimális megoldásait

Lehet, hogy olyan részproblémát kapunk, aminek nincs lehetséges megoldása, ekkor ezt a levelet elhagyjuk
Találhatunk megoldásjelölteket is, ezek alsó korlátok az eredeti IP optimális értékére.
Ha találunk korábbi megoldásjelöltnél jobb megoldást, akkor a rosszabbat elvetjük.

Egy csúcs felderített/lezárt, ha 

- nincs lehetséges megoldása
- megoldása egészértékű
- felderítettünk már olyan egész megoldást, ami jobb a részfeladat megoldásánál

Egy részfeladatot kizárunk, ha

- nincs lehetséges megoldása
- felderítettunk már olyan egész megoldást, ami jobb a részfeladat megoldásánál

## A hátizsák feladat

Egy olyan IP-t, amiben csak egy feltétel van, hátizsák feladatnak nevezünk.
Van egy hátizsákunk egy fix kapacitással, és tárgyaink, értékekkel és súlyokkal megadva.

Maximalizálni akarjuk a táskába rakott tárgyak értékét, úgy hogy a benne lévő tárgyak nem haladhatják meg a hátizsák kapacitását persze.
0-1 IP feladat, egy tárgyat viszünk vagy nem

Az LP lazítás könnyen számítható, a relatív hasznosság szerint tesszük a tárgyakat a táskába, vagyis az érték/súly hányadosuk szerint.
Branch and bound módszerrel ez is megoldható

Legrosszabb esetben 2^n részfeladatot kell megoldani, NP nehéz a feladat.
Egészértékűnél még rosszabb, $2^{Mn}$, ahol M a lehetséges egészek száma egy változóra
