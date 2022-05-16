
# 7. Objektum orientált paradigma és annak megvalósítása a JAVA és C++ nyelvekben. Az absztrakt adattípus, az osztály. Az egységbezárás, az információ elrejtés, az öröklődés, az újrafelhasználás és a polimorfizmus. A polimorfizmus feloldásának módszere


## Objektum orientált paradigma

Az objektum orientált paradigma az **objektumok** fogalmán alapuló programozási paradigma. Az objektumok egységbe foglalják az adatokat és a hozzájuk tartozó műveleteket. A program egymással kommunikáló objektumok összességéből áll melyek használják egymás műveleteit és adatait.

Az objektum-orientáltság három alapillére:

- Egységbezárás és adatelrejtés (Encapsulation & information hiding)
- Újrafelhasználás, polimorfizmus és öröklődés (Reusability, polymorphism & inheritence)
- Magasabb fokú absztrakció

### Egységbezárás és adatelrejtés 

Az egységbe zárás azt fejezi ki, hogy az összetartozó adatok és függvények, eljárások együtt vannak, egy egységbe tartoznak.
További fontos fogalom az **adatelrejtés**, ami azt jelenti, hogy kívülről csak az férhető hozzá közvetlenül, amit az objektum osztálya megenged.

Ha az objektum, illetve osztály elrejti az összes adattagját, és csak bizonyos metódusokon keresztül férhetnek hozzá a kliensek, akkor az egységbe zárás az absztrakciót és információelrejtés erős formáját valósítja meg

### Az osztály és objektum

**Absztrakt adattípus:** Az adattípus leírásának legmagasabb szintje, amelyben az adattípust úgy specifikáljuk, hogy az adatok ábrázolására és a műveletek implementációjára semmilyen előírást nem adunk.

**Osztály:** Egy absztrakt adattípus. Az adattagokból és a rajta elvégezhető műveleteket zárja egy egységbe. Egészen konkrétan objektumok csoportjának leírása, amelyeknek közös az attribútumaik, operációik és szemantikus viselkedésük van. Ugyanúgy viselkedik, mint minden egyéb primitív típus, tehát pl. változó (objektum) hozható létre belőlük.
- **Létrehozás:** Java-ban és C++-ban is a class kulcsszóval tudunk osztályokat definiálni. Az osztályokból tetszőleges mennyiségben létrehozhatunk példányokat, azaz objektumokat. 

**Objektum:** Egy változó, melynek típusa valamely objektumosztály, vagyis az osztály egy példánya amely rendelkezik állapottal, viselkedéssel, identitással. Az objektumok gyakran megfeleltethetők a való élet objektumainak vagy egyedeinek

- **állapot:** Egy az objektum lehetséges létezési lehetőségei közül (a tulajdonságok aktuális értéke, pl: lámpaBekapcsolva true vagy false)
- **viselkedés:** Az objektum viselkedése annak leírása, hogy az objektum hogy reagál más objektumok kéréseire. (metódusok, pl: lámpa.bekapcsol())
- **identitás:** Minden objektum egyedi, még akkor is, ha éppen ugyanabban az állapotban vannak, és ugyanolyan viselkedést képesek megvalósítani.

### Információ elrejtése

A láthatóságok segítségével tudjuk szabályozni adattagok, metódusok elérését, ugyanis ezeket az objektumorientált paradigma értelmében korlátozni kell, kívülről csak és kizárólag ellenőrzött módon lehessen ezeket elérni, használni.

Az adattagok, és metódusok láthatóságának vezérléséhez vannak kulcsszavak, amelyekkel megfelelően el tudjuk rejteni őket.

Láthatósági opciók

- **public:** mindenhonnan látható
- **protected:** csak az osztály scope-ján belül, illetve a később az adott osztályból származtatott gyerekosztályokon belül lehet hivatkozni.
- **private:** csak az adott osztályon belül lehet hivatkozni rá

(**Java-ban alapértelmezetten package private** (az adott packagen belül public, egyébként private) a láthatóság, míg **C++ -ban private**)

Törekedni kell a minél nagyobb adatbiztonságra és információ elrejtésre: az adat tagok láthatósága legyen private, esetleg indokolt esetben protected.

### Öröklődés

Osztályok között értelmezett viszony, amely segítségével egy általánosabb típusból (ősosztály) egy sajátosabb típust tudunk létrehozni (utódosztály). Az utódosztály adatokat és műveleteket örököl, kiegészíti ezeket saját adatokkal és műveletekkel, illetve felülírhat bizonyos műveleteket. A kód újrafelhasználásának egyik módja. **Megkülönböztetünk egyszeres és többszörös örökítést**.

A hasonlóság kifejezése az ős felé az általánosítás. A különbség a gyerek felé a specializálás.

**Java:** az ==extends== kulcsszóval tudjuk jelezni, hogy az adott osztály egy másik osztálynak a leszármazottja. Java-ban egyszeres öröklődés van, vagyis **egy osztály csak is egy ősosztályból származhat** (viszont több interfészt implementálhat)
- **super:** segítségével gyerekosztályból hivatkozhatunk szűlőosztály adattagjaira és metódusaira.

**C++:** Az ==osztály neve után vesszővel elválasztva== lehet megadni az ősosztályokat és velük együtt a láthatóságaikat. **Lehetőség van többszörös öröklődésre is.**
 
- Az öröklődés során lehetőség van az ős osztály tagjainak láthatósági opcióján változtatni. Ezt az ős osztályok felsorolásakor kell definiálni. Az változtatás csak szigorítást (korlátozást) jelenthet. Az alábbi táblázat a gyermek osztálybeli láthatóságot mutatja be az ős osztálybeli láthatóság és a módosítás függvényében:
 
### Virtuális öröklődés 

Többszörös öröklődésnél előfordulhat olyan eset, amikor egy-egy ős osztály az öröklődési hierarchia különböző pontján ismét megjelenik. Ekkor a gyermek osztályban ennek az ős osztálynak több példánya jelenhet meg. Erre néhány esetben nincs szükség, például ha az ős osztály csak egy eljárás-erőforrás, akkor minden esetben elegendő egyetlen előfordulás a gyermek osztályokban.
 
A virtuális ős osztályt az őröklődésnél az ős osztályok felsorolásakor **virtual módosítóval** kell jelezni.
 
(Ha nem adom meg a virtual módosító szót, akkor az A osztály többször fog megjelenni a D osztály példányaiban. Hivatkozásnál mindig meg kell mondani, hogy az A melyik példányáról van szó: C::A::m_iN, B::A::m_iN.)

 
### Újrafelhasználás, Polimorfizmus:

Az újrafelhasználhatóság az OOP egyik legfontosabb előnye.

Az a jelenség, hogy egy változó nem csak egyfajta típusú objektumra hivatkozhat a polimorfizmus.

A polimorfizmus lehetővé teszi számunkra, hogy egyetlen műveletet különböző módon hajtsunk végre. Más szavakkal, a polimorfizmus lehetővé teszi egy interfész definiálását és több megvalósítást. Az objektumok felcserélhetőségét biztosítja. Az objektumok őstípusai alapján kezeljük, így a kód nem függ a specifikus típusoktól. 

Polimorfizmusra két lehetőség van:

- **statikus polimorfizmus (korai hozzárendelés)** - a hívott metódus nevének és címének összerendelése szerkesztéskor történik meg. A futtatható programban már fix metóduscímek találhatók. (statikus, private, final metódusok)
- **dinamikus polimorfizmus (késői hozzárendelés)** - metódus nevének és címének hozzárendelése a hívás előtti sorban történik, futási időben

### Virtuális eljárások

Egy virtuális eljárás címének meghatározása indirekt módon, futás közben történik.

Java-ban eleve **csak virtuális eljárások** vannak (**kivéve** a **final metódusokat**, amelyeket nem lehet felüldefiniálni és a **private metódusokat, amelyeket nem lehet örökölni**)

C++ -ban a **virtuális függvénytábla** tartja nyilván a virtuális eljárások címeit. A VFT táblázat öröklődik, feltöltéséről a konstruktor gondoskodik. A származtatott osztály konstruktora módosítja a virtuális függvénytáblát, kijavítja az ősosztályból örökölt metóduscímeket. Amikor a konstruálási folyamat véget ér, a VFT táblázat minden sora értéket kap, mégpedig a ténylegesen létrehozott osztálynak megfelelő metódus címeket. A VFT táblázat sorai ezután már nem változnak meg.

- Virtuális eljárásokat a **virtual kulcsszóval** tudunk létrehozni. Az újrafelhasználás során nagy valószínűséggel módosításra kerülő eljárásokat a szülő osztályokban célszerű egyből virtuálisra megírni, mert ezzel jelentős munkát lehet megtakarítani a későbbiekben.
 
### Absztrakt osztály, interfész

**Java:
Absztrakt osztályok:**
- Az abstract kulcsszóval hozható létre. 
- Egy absztrakt osztályból nem hozható létre objektum.
- Tartalmazhat absztrakt metódusokat (absztrakt metódusnak nincs implementációja, azaz törzse), illetve nem absztraktokat
- Gyerek osztályban az abstract metódusokat felül KELL definiálni, ha példányosítható osztályt szeretnénk
- Ha egy osztály rendelkezik legalább egy absztrakt metódussal, akkor osztálynak is absztraktnak kell lennie
- Lehetnek adattagjai

**Interfész**
- Az interface kulcsszóval lehet létrehozni
- Egy speciális absztrakt osztály
- Nincsenek sem megvalósított metódusok, sem adattagok. Csupán metódus deklarációkat tartalmaz (Újabb javaban lehet **public static final** lesz mindegyik adattag)
- Gyerekosztályban az **implements** kulcsszóval lehet implementálni

**C++:
Absztrakt osztályok:**

A törzs nélküli virtuális eljárásokat **pure virtual** eljárásoknak nevezzük (pl.: virtual int getArea() = 0;). A pure virtual eljárás egy üres (NULL) bejegyzést foglal el a VFT (Virtual Function Table) táblázatban. Ha egy osztály ilyen eljárást tartalmaz, akkor azt absztrakt osztálynak nevezzük amiatt, mert ebből az osztályból objektum példányokat létrehozni nem lehet. A gyermek osztályokban minden pure virtual eljárást megfelelő törzzsel kell ellátni, ezt a fordító ellenőrzi. Amíg egyetlen pure virtual eljárás is marad, az osztály absztrakt lesz.
