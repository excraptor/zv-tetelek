# 14. Primál-duál feladatpár, dualitási komplementaritási tételek, egész értékű feladatok és jellemzőik, a branch and bound módszer, a hátizsák feladat

## Primál-duál feladatpár

A primál feladat

- maximalizálunk
- c^T a célfüggvény együtthatóinak a vektora
- A az együtthatók mátrixa
- b a konstansok vektora

A duál feladat

- minimalizálunk
- b^T a célfüggvény együtthatóinak a vektora
- A^T az együtthatók mátrixa
- c a konstansok vektora
- <=-ket >=-re cseréljük

A duál feladat duálisa az eredeti primál feladat

TFH az LP feladatunk egy korlátozott erőforrások mellett maximális nyereséget célzó gyártási folyamat modellje.
A duál feladat megoldásában az optimális megoldás a primál feladat i. erőforrásához tartozó marginális ár/árnyékár, azaz az erőforrás értéke az LP megoldójának szemszögéből
Ha túl sok van egy erőforrásból, az nem érhet túl sokat
Továbbá y_i*-nál többet nem érdemes fizetni az i. erőforrásért, kevesebbet igen

## Dualitási komplementaritási tételek

### Gyenge dualitás

Ha x egy lehetséges megoldása a primál feladatnak, és y egy lehetséges megoldása a duál feladatnak, akkor a duális feladat bármely lehetséges megoldása felső korlátja a primál bármely lehetséges megoldásának (azaz az optimális megoldásnak is) (azaz a duális feladat bármely lehetséges megoldása nagyobb vagy egyenlő a primál bármely lehetséges megoldásánál)

A korlátosság és a megoldhatóság nem függetlenek egymástól

Ha a primál nem korlátos, akkor a duálnak nincs lehetséges megoldása és fordítva.
Lehet, hogy egyiknek sincs lehetséges megoldása.
Ha mindkettőnek van, akkor mindkettő korlátos
A primál és a duál feladat egyidejű optimalitása ellenőrizhető.

### Erős dualitás

Ha x* egy optimális megoldása a primálnak, és y* egy optimális megoldása a duál feladatnak, akkor c^Tx* = b^Ty*.

Ha valamelyik i. feltétel egyenlet nem éles, azaz nem pontosan egyenlő a két oldal, akkor a kapcsolódó duál változó biztosan 0. Ha egy primál változó pozitív, akkor a kapcsolódó duális feltétel biztosan éles.

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
Ha xi értéke xi*, akkor xi <= floor(xi*) és xi>= ceil(xi*) feltételeket vesszük hozzá egy egy részfeladatunkhoz

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
Egészértékűnél még rosszabb, 2^Mn, ahol M a lehetséges egészek száma egy változóra
