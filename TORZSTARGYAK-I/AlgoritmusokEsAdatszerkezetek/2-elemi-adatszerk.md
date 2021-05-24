# 2. Elemi adatszerkezetek, bináris keresőfák, hasító táblázatok, gráfok és fák számítógépes reprezentációja

## Elemi adatszerkezetek

tömb, láncolt lista, sor, verem, gráf, map, kupac - saját vélemény

Adatszerkezet

- adatok tárolására és szervezésére szolgáló módszer
- lehetővé teszi a hatékony hozzáférést és módosításokat

Leggyakoribb műveletek

- beszúr
- keres
- töröl
- min
- max
- előző
- következő

Megfelelő adatszerkezet kulcs az implementáció futásidejéhez!

### Listák

Az adatok lineárisan követik egymást.
Egy érték többször is előfordulhat.

Műveletek: érték, értékad, keres, beszúr, töröl

Közvetlen elérés

- minden index közvetlen elérésű, közvetlenül írható/olvasható
- érték: O(1), keres: O(n)
- beszúr és töröl esetén változik a méret, át kell másolni az elemeket egy új helyre
- beszúr: O(n), töröl: O(n)
- ötlet: ha tele van a tömb, duplázzuk meg a kapacitást
- ha negyedére csökken, felezzük a kapacitást
- így nem kell mindig az egész tömböt másolni

Láncolt lista

minden érték mellé mutatókat tárolunk a következő/megelőző elemre

- egyszeresen láncolt: következő elemre mutat
- kétszeresen láncolt: előző és következőre is mutat
- ciklikus: az utolsó az első elemre mutat
- őrszem: egy nil elem, ami a lista elejére (fej) mutat

Közvetlen elérés vs Láncolt lista

- KÉ: érték konstans, módosító lassú
- LL: érték lassú, módosító gyors, sok memória kell a mutatóknak

### Verem és sor

Stack, Queue

Olyan listák, ahol a beszúrás és a törlés csak adott pozíción történhet

- verem: legutoljára beszúrt elemet vehetjük csak ki (LIFO - Last In First Out)
- sor: legkorábban beszúrt elemet vehetjük csak ki (FIFO - First In First Out)

Verem műveletek

- push: verem tetejére rakunk egy elemet
- pop: verem tetejéről levesszük

Sor műveletek:

- enqueue: sor végére rakunk
- dequeue: sor elejéről elveszünk

### Prioritási sor és kupac

Prioritási sor

- érkezés sorrendje lényegtelen, mindig a min/max elemet akarjuk kivenni

lehet mondjuk listával megvalósítani, veremmel vagy sorral nem érdemes, mert nem számít a sorrend

Prioritási sor hatékony megvalósítása: kupac (heap)

Kupac

- majdnem teljes bináris fa, minden csúcsa legalább akkora, mint a gyerekei -> max elem a gyökérben


## Bináris keresőfák

Keres, beszúr, töröl, min, max, következő, előző
Mind legyen O(logn)

Bináris keresőfa

- minden csúcsnak max két gyereke van
- balra vannak a kisebb elemek
- jobbra a nagyobbak
- keresés O(h) idejű (h a fa magassága)

