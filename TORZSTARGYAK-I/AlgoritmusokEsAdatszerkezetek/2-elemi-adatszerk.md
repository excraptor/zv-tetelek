
# 2. Elemi adatszerkezetek, bináris keresőfák, hasító táblázatok, gráfok és fák számítógépes reprezentációja

## Elemi adatszerkezetek

tömb, láncolt lista, sor, verem, gráf, map, kupac - saját vélemény

**Adatszerkezet**

- adatok tárolására és szervezésére szolgáló módszer
- lehetővé teszi a hatékony hozzáférést és módosításokat

**Leggyakoribb műveletek**
- *Módosító:*
	- beszúr 
	- töröl
- *Lekérdező:*
	- keres
	- min
	- max
	- előző
	- következő

Megfelelő adatszerkezet kulcs az implementáció futásidejéhez!

### Listák

Az adatok lineárisan követik egymást.
Egy érték többször is előfordulhat.
**Műveletek**: érték, értékad, keres, beszúr, töröl

1. **Közvetlen elérés**
- minden index közvetlen elérésű, közvetlenül írható/olvasható
- érték: O(1), keres: O(n)
- beszúr és töröl esetén **változik a méret**, át kell másolni az elemeket egy új helyre
- beszúr: O(n), töröl: O(n)
- ötlet: ha tele van a tömb, **duplázzuk meg a kapacitást**
- ha negyedére csökken, **felezzük a kapacitást**
- így nem kell mindig az egész tömböt másolni

2. **Láncolt lista**
minden érték mellé mutatókat tárolunk a következő/megelőző elemre.

- **egyszeresen láncolt:** következő elemre mutat
- **kétszeresen láncolt:** előző és következőre is mutat
- **ciklikus:** az utolsó az első elemre mutat
- **őrszem:** egy nil elem, ami a lista elejére (fej) mutat


Közvetlen elérés vs Láncolt lista

- **Közvetlen elérés:** ÉRTÉK() konstans, módosító lassú
- **Láncolt lista:** ÉRTKÉ()  lassú, módosító gyors, sok memória kell a mutatóknak

### Verem és sor (Stack, Queue)
Olyan listák, ahol a beszúrás és a törlés csak adott pozíción történhet

- *verem:* legutoljára beszúrt elemet vehetjük csak ki **(LIFO - Last In First Out)**
- *sor:* legkorábban beszúrt elemet vehetjük csak ki **(FIFO - First In First Out)**

Verem műveletek

- **push:** verem tetejére rakunk egy elemet
- **pop:** verem tetejéről levesszük
- $n$ verem méret esetén
	- Elérési idő: O(1), de csak a verem tetején lévő elemet tudjuk elérni (**pop**)
	- Beszúrás: O(1), mert mindig a tetejére pakolunk  (**push**)
	- Törlés: O(1), de csak a tetején lévő elemet tudjuk törölni (**pop**)


Sor műveletek:

- **enqueue:** sor végére rakunk
- **dequeue:** sor elejéről elveszünk
- $n$ sor méret esetén legrosszabb esetben:
	- Elérés: $\mathcal{O}(n)$ 
	- Beszúrás: $\mathcal{O}(1)$ 
	- Törlés: $\mathcal{O}(1)$
### Prioritási sor és kupac

**Prioritási sor**

- érkezés sorrendje lényegtelen, mindig a min/max elemet akarjuk kivenni

lehet mondjuk listával megvalósítani, veremmel vagy sorral nem érdemes, mert nem számít a sorrend

Prioritási sor hatékony megvalósítása: **kupac (heap)**

**Kupac**
- majdnem teljes bináris fa, minden csúcsa legalább akkora, mint a gyerekei -> max elem a gyökérben


## Bináris keresőfák

Keres, beszúr, töröl, min, max, következő, előző
**Mind legyen** $\mathcal{O}(logn)$

Bináris keresőfa

- minden csúcsnak max két gyereke van
- balra vannak a kisebb elemek
- jobbra a nagyobbak
- keresés **O(h)** idejű (h a fa magassága)
- min/max is **O(h)**: vagy teljesen jobbra, vagy teljesen balra kell lemennünk
- következő/előző szintén **O(h)** - amíg jobb/bal gyerek, addig megyünk max
- beszúr szintén **O(h)** - mindig levélként szúrunk be, úgy, hogy kb megkeressük a helyét
- töröl is **O(h)**, levelet simán törlünk, egy gyerekeset úgy, hogy a gyereket linkeljük a szülőhöz, két gyerekeset pedig a **következővel** helyettesítjük

**EZ NEM TUDOM KELL-E SZABIVANHOZ LEHET**

**AVL fák:**
- AVL-fa, ha $T$ egy nemüres bináris fa:
	- $T_L$ és $T_R$ magasság-kiegyensúlyozottak
	- $|h_L-h_R| \le 1$, ahol $h_L$ és $h_R$ rendre a T left és right magasságai.
	- **Egyensúlyfaktora** a $h_L - h_R$. Ez mindegyik -1, 0 vagy 1 lehet, ellenben forgatni kell.

Minden művelete szinte: $\mathcal{O}{(logn)}$


## Hasító táblák

### Halmaz és szótár

Halmaz

- egy elem legfeljebb egyszer szerepelhet benne
- keres helyett **tartalmaz-e**
- beszúr, töröl
- metszet, unió

Szótár

- kulcs érték párok halmaza
- minden kulcs legfeljebb egyszer szerepelhet
- egy érték tetszőleges számban előfordulhat

Asszociatív tömb

- egészek helyett bármilyen típussal indexelhetünk

Map

- kulcs->érték leképezés

### Hasítótáblák

- Halmazok és szótárak hatékony megvalósítása
- Keres, beszúr, töröl legyen hatékony 
	-	Átlagos esetben: $\mathcal{O}(1)$

Hasítótábla olyan szótár, amikor egy hash függvény segítségével állapítjuk meg, hogy melyik kulcshoz milyen érték tartozzon

példa: **h(k) = k mod m**
ahol $m$ a hasító tábla mérete
lehetnek ütközések! **cél: az ütközések minimalizálása**

#### **Ütközések minimalizálása**
**Láncolt listás megoldás:**
1. Az adott cellában egy láncolt listát tartunk számon
	2. A rövid láncok a legjobbak
	3. **Load factor:** vödrök száma / elemek száma

**Nyílt címzés**
Listák helyett tömbben "egymás után" tároljuk a megegyező hasított értékű elemeket. $\rightarrow$ Nincs szükség mutatókra.

*Lineáris próba:*
- Addig próbálgatjuk berakni a tömbe, amíg nem látunk üres  helyet, mindig 1-et lépünk előre.
- $H(k,i,n) = H(k,n)+i$ $(mod n)$, ahol $k$ a kulcs, $n$ a tábla mérete, $i$ a kipróbált hely.

*Négyzetes/Quadratikus próba:*
- Két kipróbált hely között a távolságot egy másodfokú polinom adja.
- $H(k,i,n) = H(k,n) +c_1i+c_2i^2$ $(modn)$, ahol $k$ a kulcs, $n$ a tábla mérete, $i$ a kipróbálás helye, $c_1$ és $c_2$ pedig egy valami függvényre jellemző konstans.

## Gráfok és fák számítógépes reprezentációja
#### Gráfok reprezentációja
1. **Szomszédsági mátrix**
	- minden csúcshoz hozzárendelünk egy számot
	- ha a és b között van él, akkor matrix\[a\]\[b\] = 1 és matrix\[b\]\[a\] = 1
	- ha nincs, akkor 0

2. **Szomszédsági lista**
	- minden listaelem egy csúcs, ami szintén egy lista
	- minden csúcshoz tartozó listában tároljuk a vele szomszédos csúcsokat

#### Fák reprezentációja:
- Csúcsokat és éleiket reprezentáljuk
- Maga a fa egy mutató a gyökérre.

1. gyerek éllista
	- Kulcs
	- Szülő
	- Gyereklista
2. Első fiú, apa, testvér
	- Kulcs
	- Szülő
	- Első gyerek
	- Testvér
3. Bináris fa
	- Kulcs
	- Szülő
	- Jobb és bal gyerek.   