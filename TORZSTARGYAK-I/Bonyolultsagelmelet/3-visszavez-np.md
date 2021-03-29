# 3. Hatékony visszavezetés. Nemdeterminizmus. A P és NP osztályok. NP-teljes problémák

## Hatékony visszavezetés

Visszavezetésnek nevezzük azt, mikor ha van egy problémánk, amit nem tudjuk, hogy kéne megoldanunk, és egy problémánk, amit tudjuk hogy oldjunk meg, és a nem ismert probléma inputjaiból
elkészítjük az ismert probléma egy inputját, és így oldjuk azt meg.

- Az átalakításnak tartnaia kell a választ
- Mindenre jó outputot kell adnia

Hatékonynak akkor nevezhetjük, ha ez az *inputkonverzió* polinomidejű. Ezt Turing-visszavezetésnek
is hívják. 

## Nemdeterminizmus

Egy algoritmus *nemdeterminisztikus*, ha egy ponton úgymond szétválik a futása, és többféle eredménye is lehet a futás végére. 

## P és NP osztályok

A *P* osztályban azok a problémák vannak, amelyek determinisztikusan polinomidőben megoldhatók.

Az *NP* osztályban azok a problémák vannak, amelyek nemdeterminisztikusan polinomidőben megoldhatók.

## NP teljes problémák

Egy probléma akkor *NP*-teljes, ha *NP*-beli és *NP*-nehéz.
- *NP*-beli, ha nemdeterminisztikusan tudunk tanúkat generálni hozzá, amik igen példányai a
problémának
- *NP*-nehéz, ha minden más *NP*-beli problémát hatékonyan vissza tudunk vezetni rá.

### Példák
SAT, Hátizsák, Hamilton-út, Hamilton-kör, Euler-kör, ILP, Részletösszeg, Partíció