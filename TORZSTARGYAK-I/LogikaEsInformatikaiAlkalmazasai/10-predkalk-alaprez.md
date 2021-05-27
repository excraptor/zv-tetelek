# 10. Normálformák a predikátumkalkulusban. Egyesítési algoritmus. Következtető módszerek: Alap rezolúció, elsőrendű rezolúció

## Normálformák predikátumkalkulusban

Prenex alak

- elimináljuk a nyilakat
- kiigazítjuk a formulát (változókat átnevezzük, ha van változónév-ütközés)
- az összes kvantort kihozzuk a formula elejére, ha páratlan negálás scope-jában volt, akkor fordul, ha páros, nem

Skolem alak

- prenex alak
- a létezik kvantorhoz tartozó változókat lecseréljük új függvényekre, amik az előtte álló bármely-kvantált változóktól függnek

Zárt Skolem alak

- Skolem alak
- a szabad változókat lecseréljük konstansokra, pl minden x helyére cx-et írunk

## Egyesítési algoritmus

Ha F egy formula, akkor F\[x/t\] azt jelenti, hogy F-ben x összes előfordulását helyettesítjük t-vel.

Ha x1, x2, ..., xn változók, és t1, ..., tn termek, akkor az \[x1/t1\], ..., \[xn/tn\] helyettesítés azt jelenti, hogy először x1 helyére írunk t1-et, aztán az eredményben x2 helyére t2-t, stb.

Formulák halmazaira, pl klózokra is értelmezhetjük ezt.

Klóz végzett helyettesítésnél \[x/t\] azt jelenti, hogy minden klózra elvégezzük az x helyére t helyettesítést, és az eredményeket visszapakoljuk egy halmazba.
Ha C={l1, l2, ..., ln} literálok halmaza, akkor s a c egyesítője, ha l1\*s = ... = ln\*s.
C-re akkor mondjuk, hogy egyesíthető, ha van egyesítője.

Az s helyettesítés általánosabb az s' helyettesítésnél, ha van olyan s" helyettesítés, hogy s\*s" = s'.

Egyesítési algoritmus:

- input: C klóz
- output: C legáltalánosabb helyettesítője, ha egyesíthető, különben azzal tér vissza, hogy nem egyesíthető
- veszünk két literált, és keressük az első eltérést
- ha az egyik helyen egy x változó áll, a másikon egy t term, amiben nincs x, akkor x/t és vissza az előző pontra
- különben return nem egyesíthető

Nem egyesíthető pl

- ha f(x) és c a különbség a két literál azonos pontján
- ha x és f(x) a különbség
- ha g(x) és f(x) a különbség

## Alaprezolúció

- input: elsőrendű formulák egy szigma halmaza
- output: kielégíthetetlen véges sok lépésben, vagy kielégíthető véges sokban vagy végtelen ciklus
- szigma elemeit zárt skolem alakra hozzuk, a formula belsejét pedig CNF-re, ez legyen szigma'
- ekkor E(szigma') a klózok alappéldányainak a halmaza
- E(szigma')-n futtatjuk az ítéletkalkulusbeli rezolúciós algoritmust
- E(szigma') általában végtelen
- vegyük fel E(szigma') egy elemét, és rezolváljunk vele, amíg lehet
- ha kijön az üres klóz, akkor jók vagyunk, ha nem, generálunk tovább

## Elsőrendű rezolúció

- input: elsőrendű formulák egy szigma halmaza
- output: kielégíthetetlen-e?
- szigma zárt skolemre, mag cnfre, szigma'
- szigma' elemeit közvetlenül felvehetjük a listára
- ha kijön az üres klóz, kielégíthetetlen
- ha nem tudunk több klózt levezetni, kielégíthető


Rezolvensképzés:

- C1 és C2 klózokat akarjuk rezolválni
- átnevezzük a változókat úgy, hogy ne legyen közös változó C1-ben és C2-ben
- kiválasztunk C1-ből és C2-ből is literálokat, az egyikből pozitívokat, a másikból negatívokat
- ezeket pozitívan belepakoljuk egy C halmazba
- ha C egyesíthető egy s helyettesítéssel, akkor vehetjük a rezolvensét C1-nek és C2-nek
- elmentjük s-t
- vesszük C1-ből és C2-ből a maradék literálokat, és berakjuk egy halmazba
- ezen a halmazon elvégezzük az s helyettesítést, ez lesz a rezolvens



