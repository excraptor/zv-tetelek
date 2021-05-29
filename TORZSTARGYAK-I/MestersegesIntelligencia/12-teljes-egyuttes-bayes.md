# 12. Teljes együttes eloszlás tömör reprezentációja, Bayes hálók. Gépi tanulás: felügyelt tanulás problémája, döntési fák, naiv Bayes módszer, modellillesztés, mesterséges neuronhálók, k-legközelebbi szomszéd módszere

## Teljes együttes eloszlás tömör reprezentációja, Bayes hálók

### Teljes együttes eloszlás

Minden lehetséges eseményre tudjuk annak a valószínűségét. Pl van 3 logikai típusú véletlen változónk, akkor összesen 2^3=8-féle eset lehet ezekre. A teljes együttes eloszlásnál mind a 8 esetnek tudjuk a valószínűségét.

### Tömör reprezentáció

A kijelentések függetlensége a legfontosabb tulajdonság a teljes együttes eloszlás tömöríthetőségéhez. Van függetlenség, és feltételes függetlenség.

Függetlenség
a és b kijelentések függetlenek, ha P(a és b) = P(a)*P(b)

A függetlenség struktúrát takar. Ha pl n logikai változónk van, amik két független részhalmazra oszthatók m és k mérettel, akkor a 2^n valószínűség tárolása helyett elég 2^m+2^k valószínűséget tárolni, ami sokkal kevesebb lehet.

Extrém esetben, ha pl. az A1,..., An diszkrét változók kölcsönösen függetlenek (tetszőleges két részhalmaz független), akkor csak O(n) értéket kell tárolni, mivel ez esetben

P(A1,..., An) = P(A1)...P(An)

Feltételes függetlenség
a és b kijelentések feltételesen függetlenek c feltevésével, akkor és csak akkor, ha P(a és b | c) = P(a|c)*P(b|c). Tipikus eset, ha a és b közös oka c.

Naiv-Bayes szabály
Ha A feltevése mellett B1,...,Bn kölcsönösen függetlenek, akkor 
P(B1, . . . , Bn|A) = Produktum^n_i=1 P(Bi|A)

### Bayes hálók

A feltételes függetlenség hasznos, mert tömöríthetjük a teljes együttes eloszlást.


## Gépi tanulás: felügyelt tanulás problémája, döntési fák, naiv Bayes módszer, modellillesztés, mesterséges neuronhálók, k-legközelebbi szomszéd módszere

### Felügyelt tanulás problémája

Tapasztalati tények felhasználása arra, hogy egy racionális ágens teljesítményét növeljük.

Felügyelt tanulás: 

- van az adatok mögött valami f: X -> Y függvény, ezt nem ismerjük
- adottak tanulópéldák, amik rendezett párok (x, f(x))
- egy h: X -> Y, függvényt keresünk, ami illeszkedik a példákra, és közelíti f-et
- egy példában az első elem pl egy email, a második pedig egy valamilyen címke, pl spam
- h konzisztens az adatokra, ha h(x)==f(x) minden x tanulópéldára
- a h függvényt mindig valami H hipotézistérben keressük, vagyis valamilyen "alakban"
- a tanulás realizálható, ha van olyan h eleme H, amire h konzisztens
- a gyakorlatban elég, ha h közel van a példákhoz, mert a példák zajt is tartalmazhatnak, amit kifejezetten káros lenne, ha megtanulna az ágens (túltanulás)
- egy olyan h-t keresünk, ami a tanulópéldákon kívül is jól általánosít
- nem szabad a tanulópéldákat bemagolni
- occam borotvája: mindig a legtömörebb leírást kell venni
- a priori ismeretek fontosak, a nulláról való tanulás kb lehetetlen
- számítási szempontból egyszerű reprezentáció is fontos

### Döntési fák

Induktív (felügyelt) tanulás konkrét példája.

Feltesszük, hogy X-ben diszkrét változók egy vektora van, Y-ban pedig szintén valami diszkrét változó egy értéke, pl igen-nem

Tulajdonképpen osztályozás, X elemeit kell Y valamelyik osztályába sorolni.

Előnye, hogy döntései megmagyarázhatók, mert emberileg értelmezhető lépésekben jutottunk el odáig.

Kifejezőereje megegyezik az ítéletkalkuluséval.

Döntési fa építése

- adottak pozitív és negatív példák felcímkézve, tipikusan több száz
- vegyük a gyökérbe azt a változót, ami a legjobban szeparálja a pozitív és negatív példákat
- ezt folytassuk rekurzív módon
- ha csak pozitív vagy negatív példa van, akkor levélhez értünk, felcímkézzük ezzel a levelet
- ha üreshalmaz, akkor a szülő szerint többségi szavazattal címkézünk
- ha nincs több változó, de vannak negatív és pozitív példák is, akkor szintén többségi szavazattal címkézhetjük a levelet

A legjobban szeparáló attribútumot az információtartalma, azaz entrópiája segítségével választhatjuk ki. 

### Naiv Bayes módszer

Statisztikai következtetési módszer, amely adatbázisban található példák alapján ismeretlen példákat osztályoz. 


