# 3. Hatékony visszavezetés. Nemdeterminizmus. A P és NP osztályok. NP-teljes problémák

## Alapvető információk:
**Időigény:** Adott futásidejű algoritmus adott számítási kapacitású architektúrán mekkora inputra fut le.

**Az input mérete:** Az $a_1,..,a_n$ input **mérete** az $a_i$ számok **bináris reprezentáció** hosszának összege.

**A gép időkorlátja:** $M$ Ram gép időkorlátja az $f(n) : \N \rightarrow \N$ függvény, ha tetszőleges $n$ méretű inputon legfeljebb $f(n)$ lépésben megáll.

## Hatékony visszavezetés
**Visszavezetésnek** nevezzük azt, mikor ha van egy problémánk, amit nem tudjuk, hogy kéne megoldanunk, és egy problémánk, amit tudjuk hogy oldjunk meg, és a nem ismert probléma inputjaiból
elkészítjük az ismert probléma egy inputját, és így oldjuk azt meg.

Hatékonynak akkor nevezhetjük, ha ez az **inputkonverzió polinomidejű**. Ezt Turing-visszavezetésnek is hívják. 

**Formailag:**
	Legyenek $A$ és $B$ eldöntési problémák, azt mondjuk, hogy $A$ (**hatékonyan**) visszavezethető $B$-re, ha van olyan $f$ (**polinomidejű**) inputkonverzió, ami:
	- $A$ inputjaiból $B$ inputjait készíti
	- **Tartja a választ:** $A(x) = B(f(x))$
**Jele:** $A \le_p B$ ($B$ legalább olyan nehéz mint $A$)

## Nemdeterminizmus

Egy algoritmus *nemdeterminisztikus*, ha egy ponton úgymond szétválik a futása, és többféle eredménye is lehet a futás végére. 

## P és NP osztályok

A *P* osztályban azok a problémák vannak, amelyek determinisztikusan polinomidőben megoldhatók.

Az *NP* osztályban azok a problémák vannak, amelyek nemdeterminisztikusan polinomidőben megoldhatók.


## NP teljes problémák

**Nehézség, teljesség:**
$A$ egy **probléma** $C$ pediga problémák egy **osztálya**
	1. **C-nehéz:** Minden $C$-beli probléma visszavezethető $A$-ra
	2. **C-teljes:** $A$ probléma ráadásul $C$-ben van


Egy probléma akkor *NP*-teljes, ha *NP*-beli és *NP*-nehéz.

- **NP-beli**, ha nemdeterminisztikusan tudunk tanúkat generálni hozzá, amik igen példányai a
problémának.
- **NP-nehéz**, ha minden más *NP*-beli problémát hatékonyan vissza tudunk vezetni rá.
- **NP-teljes**, Vegyünk egy ismerten NP-teljes problémát és **vezessük ezt** az új problémára vissza

### Példák
Pár képen ott van.
SAT, Hátizsák, Hamilton-út, Hamilton-kör, Euler-kör, ILP, Részletösszeg, Partíció
