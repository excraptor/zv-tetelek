# 5. Algoritmusok vezérlési szerkezetei és megvalósításuk C programozási nyelven. A szekvenciális, iterációs, elágazásos, és az eljárás vezérlés

## Algoritmusok vezérlési szerkezetei és megvalósításuk C nyelven

Algoritmus: bármilyen jól definiált számítási eljárást, amely bemenetként bizonyos értéket vagy értékeket kap és kimenetként bizonyos értéket vagy értékeket állít elő. Vizsgálhatjuk helyesség, idő- és tárigény szempontjából

Algoritmus vezérlése: Az az előírás, amely az algoritmus minden lépésére (részműveletére) kijelöli, hogy a lépés végrehajtása után melyik lépés végrehajtásával folytatódjon (esetleg fejeződjék be) az algoritmus végrehajtása. Az algoritmusnak, mint műveletnek a vezérlés a legfontosabb komponense.

Négy fő vezérlési módot különböztetünk meg:
- Szekvenciális: Véges sok adott művelet rögzített sorrendben egymás után történő végrehajtása. (sorban egymás után)
- Szelekciós: Véges sok rögzített művelet közül adott feltétel alapján valamelyik végrehajtása. (if, else, if else, switch)
- Ismétléses: Adott művelet adott feltétel szerinti ismételt végrehajtása. (for, while, do while)
- Eljárás: Adott művelet alkalmazása adott argumentumokra, ami az argumentumok értékének pontosan meghatározott változását eredményezi. (void func, int func, double func, …)

A vezérlési módok nyelvek feletti fogalmak.

A imperatív (algoritmikus) programozási nyelvekben ezek a vezérlési szerkezetek (közvetlenül vagy közvetve) megvalósíthatók.

## A szekvenciális, iterációs, elágazásos, és az eljárás vezérlés

### Szekvenciális vezérlés

Szekvenciális vezérlésről akkor beszélünk, amikor a P probléma megoldását úgy kapjuk, hogy a problémát P1,..., Pn részproblémákra bontjuk, majd az ezekre adott megoldásokat (részalgoritmusokat) sorban egymás után hajtjuk végre.

P1,..., Pn lehetnek elemi műveletek, vagy nem elemi részproblémák megnevezései.

### Eljárásvezérlés

Eljárásvezérlésről akkor beszélünk, amikor egy műveletet adott argumentumokra alkalmazunk, aminek hatására az argumentumok értékei pontosan meghatározott módon változnak meg.

Az eljárásvezérlés fajtái:

- Eljárásművelet
- Függvényművelet

C-ben kicsi a különbség a kettő között.

Függvényművelet

- A matematikai függvény fogalmának általánosítása
- Ha egy részprobléma célja egy érték kiszámítása adott értékek függvényében, akkor a megoldást megfogalmazhatjuk függvényművelettel.
- A függvényművelet specifikációja tartalmazza:
    - A művelet elnevezését
    - A paraméterek felsorolását
    - Mindegyik paraméter adattípusát
    - A művelet hatásának leírását
    - A függvényművelet eredménytípusát
- Minden függvényben szerepelnie kell legalább egy return utasításnak
- Ha a függvényben egy ilyen utasítást hajtunk végre, akkor a függvény értékének kiszámítása befejeződik. A hívás helyén a függvény a return által kiszámított értéket veszi fel

Eljárásművelet

- Ha eljárást szeretnénk készíteni C nyelven, akkor egy olyan függvényt kell deklarálni, melynek eredménytípusa void. Ebben az esetben a függvény definíciójában nem kötelező a return utasítás, illetve ha mégis van ilyen, akkor nem adható meg utána kifejezés

Megvalósítás

- csak bemenő módú argumentumok vannak
- pointerekkel lehet kezelni kimenő argumentumokként is

### Szelekciós vezérlés

Szelekciós vezérlésről akkor beszélünk, amikor véges sok rögzített művelet közül véges sok feltétel alapján választjuk ki, hogy melyik művelet kerüljön végrehajtásra.

Típusai: 

- Egyszerű szelekciós vezérlés
- Többszörös szelekciós vezérlés
- Esetkiválasztásos szelekciós vezérlés
- A fenti három „egyébként” ággal 

#### Egyszerű szelekciós vezérlés

- Egyszerű szelekció esetén egyetlen feltétel és egyetlen művelet van (ami persze lehet összetett). 
- A vezérlés bővíthető úgy, hogy a 3. pontban üres művelet helyett egy B műveletet hajtunk végre, ekkor beszélünk egyébként ágról.

Egyszerű szelekciós utasítás megvalósítása C nyelven:

if(F) {
    A;
}

#### Többszörös szelekciós vezérlés 

- Ha több feltételünk és több műveletünk van, akkor többszörös szelekcióról beszélünk.
- A többszörös szelekció is bővíthető egyébként ággal úgy, hogy egy nemüres B műveletet hajtunk végre a 3. lépésben. 
- Legyenek Fi logikai kifejezések, Ai (és B) pedig tetszőleges műveletek. Az Fi feltételekből és Ai  (és B) műveletekből képzett többszörös szelekciós vezérlés a következő vezérlési előírást jelenti: 
    - Az Fi feltételek sorban történő kiértékelésével adjunk választ a következő kérdésre: Van-e olyan i amelyre teljesül, hogy az Fi feltétel igaz és az összes Fj feltétel hamis? 
    - Ha van ilyen i, akkor hajtsuk végre az Ai műveletet és fejezzük be az összetett művelet végrehajtását. 
    - Egyébként, vagyis ha minden Fi feltétel hamis, akkor (hajtsuk végre B-t és) fejezzük be az összetett művelet végrehajtását. 

Többszörös szelekciós utasítás megvalósítása C nyelven:

if(F1) {
    A1;
} else if (F2) {
    A2;
}...

- C nyelvben nincs külön utasítás a többszörös szelekció megvalósítására, ezért az egyszerű szelekció ismételt alkalmazásával kell azt megvalósítani. 
- Ez azon az összefüggésen alapszik, hogy a többszörös szelekció levezethető egyszerű szelekciók megfelelő összetételével. 
  
  
#### Esetkiválasztós szelekciós vezérlés

Ha a többszörös szelekciós vezérlésben minden Fi feltételünk K ∈ Hi alakú, akkor esetkiválasztásos szelekcióról beszélünk. 

- Legyen K egy adott típusú kifejezés, legyenek Hi ilyen típusú halmazok, Ai (és B) pedig tetszőleges műveletek. A K szelektor kifejezésből, Hi kiválasztó halmazokból és Ai (és B) műveletekből képzett esetkiválasztásos szelekciós vezérlés a következő vezérlési előírást jelenti: 
    - Értékeljük ki a K kifejezést és folytassuk a 2.) lépéssel. 
    - Adjunk választ a következő kérdésre: Van-e olyan i (1<=i<=n), amelyre teljesül, hogy a kiszámolt érték eleme a Hi halmaznak és nem eleme az összes Hj (1<=j<i) halmaznak?
    - Ha van ilyen i, akkor hajtsuk végre az Ai műveletet és fejezzük be az összetett művelet végrehajtását. 
    - Egyébként, vagyis ha K nem eleme egyetlen Hi halmaznak sem, akkor (hajtsuk végre B-t és) fejezzük be az összetett művelet végrehajtását.
 
- A kiválasztó halmazok megadása az esetkiválasztásos szelekció kritikus pontja. 
- Algoritmusok tervezése során bármilyen effektív halmazmegadást használhatunk, azonban a tényleges megvalósításkor csak a választott programozási nyelv eszközeit alkalmazhatjuk. 

A switch utasítás: Ha egy kifejezés értéke alapján többféle utasítás közül kell választanunk, a switch utasítást használhatjuk. Megadhatjuk, hogy hol kezdődjön és meddig tartson az utasítás-sorozat végrehajtása. 
A switch utasítás szintaxisa C-ben:

switch(kifejezés) {
    case konstans1:
        A;
        break;
    case konstans2:
        B;
        break;
    default:
        D;
}
 
- A szelektor kifejezés és a konstansok típusának meg kell egyeznie. Egy konstans legfeljebb egy case mögött és a default kulcsszó is legfeljebb egyszer szerepelhet egy switch utasításban. 
- A default cimke olyan, mintha a szelektor kifejezés lehetséges értékei közül minden olyat felsorolnánk, ami nem szerepel case mögött az adott switch-ben. 
- A cimkék (beleértve a default-ot is) sorrendje tetszőleges lehet, az nem befolyásolja, hogy a szelektor kifejezés melyik cimkét választja. 
- A szelektor kifejezés értékétől csak az függ, hogy melyik helyen kezdjük el végrehajtani a switch magját. Ha a végrehajtás elkezdődik, akkor onnantól kezdve az első break (vagy return) utasításig, vagy a switch végéig sorban hajtódnak végre az utasítások. Ebben a fázisban a további case és default cimkéknek már nincs jelentőssége. 
- A Hi halmazok elemszáma tetszőleges lehet, viszont a case-ek után csak egy-egy érték állhat. 


### Ismétléses vezérlések

Ismétléses vezérlésen olyan vezérlési előírást értünk, amely adott műveletnek adott feltétel szerinti ismételt végrehajtását írja elő. 

Az algoritmustervezés során a leginkább megfelelő ismétléses vezérlési formát használjuk, függetlenül attól, hogy a megvalósításra használt programozási nyelvben közvetlenül megvalósítható-e ez a vezérlési mód. 

Ismétléses vezérlés képzését ciklusszervezésnek is nevezik, így az ismétlésben szereplő műveletet ciklusmagnak hívjuk. 

Az ismétlési feltétel szerint ötféle ismétléses vezérlést különböztetünk meg: 

- Kezdőfeltételes
- Végfeltételes
- Számlálásos 
- Hurok 
- Diszkrét 

#### Kezdőfeltételes ismétléses vezérlés

Kezdőfeltételes vezérlésről akkor beszélünk, ha a ciklusmag (ismételt) végrehajtását egy belépési (ismétlési) feltételhez kötjük. 

- Legyen F logikai kifejezés, M pedig tetszőleges művelet. Az F ismétlési feltételből és az M műveletből (a ciklusmagból) képzett kezdőfeltételes ismétléses vezérlés a következő vezérlési előírást jelenti: 
    - Értékeljük ki az F feltételt és folytassuk a 2.) lépéssel. 
    - Ha F értéke hamis, akkor az ismétlés és ezzel együtt az összetett művelet végrehajtása befejeződött. 
    - Egyébként, vagyis ha az F értéke igaz, akkor hajtsuk végre az M műveletet, majd folytassuk az 1.) lépéssel. 

- A feltétel ellenőrzése a művelet előtt történik
- Ha az F értéke kezdetben hamis, az összetett művelet végrehajtása befejeződik anélkül, hogy az M művelet egyszer is végrehajtásra kerülne 
- Ha az F értéke igaz, és az M művelet nincs hatással az F feltételre, akkor F igaz is marad, tehát az összetett művelet végrehajtása nem tud befejeződni. Ilyenkor végtelen ciklus végrehajtását írtuk elő.
- Fontos tehát, hogy az M művelet hatással legyen az F feltételre.

A while utasítás: Ha valamilyen műveletet mindaddig végre kell hajtani, amíg egy feltétel igaz, a while utasítás használható. 
   
while(F) {
    M;
}

#### Végfeltételes ismétléses vezérlés

A végfeltételes ismétléses vezérlés alapvetően abban különbözik a kezdőfeltételes ismétléses vezérléstől, hogy a ciklusmag legalább egyszer végrehajtódik.
Végfeltételes vezérlésről akkor beszélünk, ha a ciklusmag elhagyását egy kilépési feltételhez kötjük. 

- Legyen F logikai kifejezés, M pedig tetszőleges művelet. Az F kilépési feltételből és az M műveletből (a ciklusmagból) képzett végfeltételes ismétléses vezérlés a következő vezérlési előírást jelenti: 
    - Hajtsuk végre az M műveletet majd folytassuk a 2.) lépéssel.
    - Értékeljük ki az F feltételt és folytassuk a 3.) lépéssel. 
    - Ha F értéke igaz, akkor az ismétléses vezérlés és ezzel együtt az összetett művelet végrehajtása befejeződött. 
    - Egyébként, vagyis ha az F értéke hamis, akkor folytassuk az 1.) lépéssel. 
- Ha az F értéke kezdetben hamis, és az M művelet nincs hatással F-re, akkor végtelen ciklust kapunk. Ha az F értéke kezdetben igaz, M legalább egyszer akkor is végrehajtásra kerül. 
- A kezdő és végfeltételes vezérlések kifejezhetőek egymás segítségével. 

A do while: utasítás Ha valamilyen műveletet mindaddig végre kell hajtani, amíg egy feltétel igaz, a do while utasítás használható. A művelet végrehajtása szükséges a feltétel kiértékeléséhez. A feltétel ellenőrzése a művelet után történik, így ha a feltétel kezdetben hamis volt, a műveletet akkor is legalább egyszer végrehajtjuk. 

do {
    M;
} while (!F);
    

#### Számlálásos ismétléses vezérlések

Számlálásos ismétléses vezérlésről akkor beszélünk, ha a ciklusmagot végre kell hajtani sorban minden olyan értékére (növekvő vagy csökkenő sorrendben), amely egy adott intervallumba esik. 

Legyen a és b egész érték, i egész típusú változó, M pedig tetszőleges művelet, amelynek nincs hatása a, b és i értékére. 

Növekvő számlálásos ismétléses vezérlések:

- Az a és b határértékekből, i ciklusváltozóból és M műveletből (ciklusmagból) képzett növekvő számlálásos ismétléses vezérlés az alábbi vezérlési előírást jelenti: 
    - Legyen i = a és folytassuk a 2.) lépéssel. 
    - Ha b < i (i nagyobb mint a intervallum végpontja), akkor az ismétlés és ezzel együtt az összetett művelet végrehajtása befejeződött. 
    - Egyébként, vagyis ha i ≤ b, akkor hajtsuk végre az M műveletet, majd folytassuk a 4.) lépéssel. 
    - Növeljük i értékét 1-gyel, és folytassuk a 2.) lépéssel. 

 

Csökkenő számlálásos ismétléses vezérlések:

- Az a és b határértékekből, i ciklusváltozóból és M műveletből (ciklusmagból) képzett csökkenő számlálásos ismétléses vezérlés az alábbi vezérlési előírást jelenti: 
    - Legyen i = b és folytassuk a 2.) lépéssel. 
    - Ha i < a, akkor az ismétlés és ezzel együtt az összetett művelet végrehajtása befejeződött. 
    - Egyébként, vagyis ha a ≤ i, akkor hajtsuk végre az M műveletet, majd folytassuk a 4.) lépéssel. 
    - Csökkentsük i értékét 1-gyel, és folytassuk a 2.) lépéssel. 

 

A for utasítás: Ha valamilyen műveletet sorban több értékére is végre kell hajtani, akkor a for utasítás használható.

for (i = a; i <=b; i++) {
    M;
}
for (kif1; kif2; kif3) {
    M;
}

C-ben a for utasítás általános alakja:
- A kif1 és kif3 többnyire értékadás vagy függvényhívás, kif2 pedig relációs kifejezés. 
- Bármelyik kifejezés elhagyható, de a pontosvesszőknek meg kell maradniuk
- kif2 elhagyása esetén a feltételt konstans igaznak tekintjük, ekkor a break vagy return segítségével lehet kiugrani a ciklusból. 


#### Hurok ismétléses vezérlés

Amikor a ciklusmag ismétlését a ciklusmagon belül vezéreljük úgy, hogy a ciklus különböző pontjain adott feltételek teljesülése esetén a ciklus végrehajtását befejezzük, hurok ismétléses vezérlésről beszélünk. 

- Legyenek Fi logikai kifejezések, Ki és Mj pedig tetszőleges (akár üres) műveletek 1≤i≤n és 0≤j≤n értékekre. Az Fi kijárati feltételekből, Ki kijárati műveletekből és az Mi műveletekből képzett hurok ismétléses vezérlés a következő előírást jelenti: 
    - Az ismétléses vezérlés következő végrehajtandó egysége az M0 művelet. 
    - Ha a végrehajtandó egység az Mj művelet, akkor ez végrehajtódik. j = n esetén folytassuk az 1.) lépéssel, különben pedig az Fj+1 feltétel végrehajtásával a 3.) lépésben. 
    - Ha a végrehajtandó egység az Fi feltétel (1 ≤ i ≤ n), akkor értékeljük ki. Ha Fi igaz volt, akkor hajtsuk végre a Ki műveletet, és fejezzük be a vezérlést. Különben a végrehajtás az Mi művelettel folytatódik a 2.) lépésben. 
- A kezdő- és végfeltételes ismétléses vezérlések speciális esetei a hurok ismétléses vezérlésnek. 
- A C nyelvben a ciklusmag folyamatos végrehajtásának megszakítására két utasítás használható: 
- break: Megszakítja a ciklust, a program végrehajtása a ciklusmag utáni első utasítással folytatódik. Használható a switch utasításban is, hatására a program végrehajtása a switch utáni első utasítással folytatódik. 
- continue: Megszakítja a ciklusmag aktuális lefutását, a vezérlés a ciklus feltételének kiértékelésével (while, do while) illetve az inkrementáló kifejezés kiértékelésével (for) folytatódik. 
    

#### Diszkrét ismétléses vezérlés:

Diszkrét ismétléses vezérlésről akkor beszélünk, ha a ciklusmagot végre kell hajtani egy halmaz minden elemére tetszőleges sorrendben. 
- Legyen x egy T típusú változó, H a T értékkészletének részhalmaza, M pedig tetszőleges művelet, amelynek nincs hatása x és H értékére. A H halmazból, x ciklusváltozóból és M műveletből (ciklusmagból) képzett diszkrét ismétléses vezérlés az alábbi vezérlési előírást jelenti: 
    - Ha a H halmaz minden elemére végrehajtottuk az M műveletet, akkor vége a vezérlésnek. 
    - Egyébként vegyük a H halmaz egy olyan tetszőleges e elemét, amelyre még nem hajtottuk végre az M műveletet, és folytassuk a 3.) lépéssel. 
    - Legyen x = e és hajtsuk végre az M műveletet, majd folytassuk az 1.) lépéssel. 
- A H halmaz számossága határozza meg, hogy az M művelet hányszor hajtódik végre. Ha a H az üres halmaz, akkor a diszkrét ismétléses vezérlés az M művelet végrehajtása nélkül befejeződik. 
- A diszkrét ismétléses vezérlésnek nincs közvetlen megvalósítása a C nyelvben. 

   
  

