
# 8. Objektumok életciklusa, létrehozás, inicializálás, másolás, megszüntetés. Dinamikus, lokális és statikus objektumok létrehozása. A statikus adattagok és metódusok, valamint szerepük a programozásban. Operáció és operátor overloading a JAVA és C++ nyelvekben. Kivételkezelés

## Objektumok létrehozása

Az objektumokat Java-ban és C++ -ban is tárolhatjuk **statikusan** (az adatszegmensben), a **veremben** (lokálisan) vagy a **heapben** (dinamikusan).

Java-ban az objektumok mindig a heap-ben keletkeznek, kivéve a primitív típusokat. Az osztályok konstruktora fogja inicializálni az objektumot. A konstruktor neve meg kell egyezzen az osztály nevével. A konstruktornak nincs visszatérési értéke, de paraméterei lehetnek, amelyekkel meg lehet adni, hogy hogyan inicializáljuk az objektumot.

A **new** operátor:
- Szintaxis: new Osztály(args)
- Létrehozás lépései:
    - Lefoglalja a számára szükséges memóriát
    - Meghívja az osztály konstruktorát
    - Visszaadja az objektumra mutató referenciát

Egy osztályhoz készíthetünk több konstruktort, amelyek különböző paraméterlistával rendelkeznek.

**C++-ban is hasonlóan működik a konstruktor**: a konstruktor inicializálja az objektumot, azaz tölti fel az adattagjait értékekkel, több különböző paraméter listájú konstruktort lehet létrehozni egy osztályhoz, a konstruktor neve meg kell egyezzen az osztály nevével és visszaadott értéke nem lehet.

A paraméter nélküli konstruktor eljárás neve: alapértelmezett (default) konstruktor. Csak ős osztályokban kötelező, akkor ha az osztályból gyermek osztályokat szeretnének létrehozni öröklődéssel. Megvalósítható olymódon is, hogy egy nem default konstruktor minden paraméteréhez default eljárás paramétereket adunk (pl. Osztaly(int x = 1, int y = 2)).

Amennyiben egy gyermek osztály konstruálunk, akkor a konstruktor minden esetben meg kell hívja rekurzívan az ős osztály(ok) konstruktorait mielőtt elkezdené a saját eljárás törzsét végrehajtani. Java-ban ez impliciten megtörténik, ha az ősosztálynak van default konstruktora.

C++-ban a heapbeli objektumok létrehozása a new operátorral történik, megszüntetésük pedig a delete operátorral. A létrehozáshoz nem elegendő a memória megfelelő méretben történő lefoglalása, hanem a konstruktor eljárást is meg kell hívni. (Ezért nem lehet objektum példányt létrehozni malloc eljárással.) A new operátorral egyetlen objektum példányt vagy megadott méretű tömböt hozhatunk létre. A new operátor alkalmazásának eredménye mindig egy pointer a new operandusában megadott osztályra.

**Szintaxis:**
  
Tömbök foglalásakor a default konstruktor hívódik meg. Megszüntetésüknél az üres [] zárójelpár használata kötelező.

C++ban az objektum megszüntetése előtti takarítást, erőforrás felszabadítást a destruktor végzi. A neve meg kell egyezzen az osztály nevével, ami elé egy ~ (tilde) jelet is kell tenni. Paramétere és visszaadott értéke nem lehet. A destruktor már nem állíthatja meg az objektum megszüntetését. Amikor a destruktor véget ér, az objektumot a rendszer a memóriából törli. Mindig a gyerek osztály destruktora hívódik meg először, és azt követi rekurzívan az ős osztályok destruktorainak a meghívása.

Java-ban nincs szükség a heap-ben létrehozott objektumok manuális törlésére. A takarítást automatikusan elvégzi a garbage collector (szemétgyűjtő). Ez biztonságosabb, a programozónak nem kell emlékeznie, hogy fel kell szabadítani az erőforrásokat, viszont sokkal lassabb. A szemétgyűjtést kézzel is el lehet indítani, de ez nem egyenlő a destruktorral, kiszámíthatatlan, hogy mikor fog végrehajtódni.

### Objektum másolás

Akkor beszélünk klónozásról, ha egy objektum példányt két (vagy több) példányban sokszorosítunk úgy, hogy az egyes példányok adat tagjai azonosak lesznek.	

Klónozás lehetséges az „=” segítségével, viszont ilyenkor az objektumok ugyan lemásolódnak, de a referenciájuk ugyanarra a memóriaterületre fog mutatni, azaz, ha pl. az egyik másolt objektum egyik adattagját módosítjuk, az az eredeti objektumra is hatással lesz.

Java:
Valódi másolást Java-ban a clone() metódussal tudunk végrehajtani. Az osztálynak, amit szeretnénk klónozhatóvá tenni implementálnia kell a Cloneable interfészt és meg kell hívnia az ős clone() metódusát (super.clone()).

C++:
A valós klónozás megvalósítására szolgát a copy konstruktor. A copy konstruktor paramétereinek száma 1, ennek az egy paraméternek a típusa pedig a tartalmazó osztályra mutató referencia típus.
 
## Dinamikus, lokális és statikus objektumok létrehozása:

C++:
   
A **statikusan létrehozott objektum** az adott kód blokk végén megszűnik, amelyikben létre lett hozva.
**Lokális objektumokat** default paraméter vagy objektumokat tartalmazó kifejezésekben használhatunk. Szokás még objektum konstansnak is nevezni őket.
**Objektumokat dinamikusan** a new operátor segítségével tudunk létrehozni, amelynek törléséről a programozónak kell gondoskodnia.

Java:
Java-ban minden objektum dinamikusan jön létre a heap-ben.

### A statikus adattagok és metódusok

A statikus adattagok és metódusok hasonlóan működnek Java-ban és C++-ban. Mindkét nyelven a static módosítóval tudjuk jelezni, hogy az adott member statikus lesz.

Az ilyen adattagok és metódusok csak egy példányban jönnek létre és az osztálynak lesznek a tagjai, amelyet az objektumok közösen használhatnak.

A statikus metódusok nem lehetnek virtuálisak, nem hivatkozhatnak az adott objektumra (this-re).

Az ilyen adattagok, metódusok példányosítás nélkül is használhatóak.

Olyan esetekben lehetnek hasznosak, amikor az adott adattag, metódus független az objektumoktól, és mindenhol megegyezne az implementáció. Például van egy statikus adattagunk, amely a diákok számát tárolja és egy statikus metódus, amely visszaadja ennek a statikus adattagnak az értékét.

 
## Operáció és operátor overloading

### Operáció kiterjesztés

Az operáció kiterjesztés mind Java, mind C++ nyelven támogatott és hasonló módon működik. A lényege, hogy azonos nevű függvények többször vannak implementálva melyek paraméterei eltérő számúak és típusúak lehetnek. Ilyenek a változó paraméterű konstruktorok is többek között.

A fordító a kiterjesztett metódusokat a paraméterlistájuk alapján különbözteti meg

```
void sum(int a,int b){ System.out.println(a+b); }
void sum(int a,int b,int c){ System.out.println(a+b+c); }
```

### Operátor kiterjesztés

Java-ban nincs lehetőség az operátorok kiterjesztésére. 
A C++ programozási nyelv lehetőséget biztosít arra, hogy az osztályokra kiterjesszük a nyelvben definiált bináris és unáris operátorokat. A kiterjesztésre vonatkozóan több megszorítás is van, ennek ellenére ez a szolgáltatás jelentős lépés az absztrakció növelésének irányába.

- A kiterjesztés CSAK osztályok esetén lehetséges (ebben benne van a class, struct és a union), viszont nem működik tömbökre, pointerekre.
- Bizonyos elemi operátorok kiterjesztésére nincs lehetőség, ilyenek a . (member selection), :: (scope resolution), ? : (ternary), .* (pointer to member), # és ## a preprocesszorból. Kiterjeszthető viszont a (typecast) operátor!
- Az operátorok precedenciája nem változtatható meg.
- Az operátor eljárások öröklődnek (kivéve az „=” operátor).
- Az operátorok egyik operandusa osztály (vagy osztályra mutató referencia típus) kell legyen. Ettől függetlenül lehet a két operandus különböző. 
  
## A friend osztályok és eljárások

Az operátor eljárások implementációjakor szükség lehet objektumok private és protected adattagjainak elérésére. Az adattagok elérésére használhatunk segéd eljárásokat, azonban itt egy speciális esetről van szó, ahol számításba jöhet egy ”barát” eljárás alkalmazása is (talán szándékaink szerint metódussal szerettük volna megvalósítani az operátor eljárást, csak valamiért ez nem volt megengedett).

- A friend eljárást az osztály belsejében kell deklarálni.
- Nemcsak eljárás lehet friend, hanem másik osztály is!
- A friend eljárások nem lesznek az osztály tagjai! 
- Abban az osztályban kell őket deklarálni, amelynek a tagjait el kívánják érni.
- A friend eljárásokat a global scope-ban kell megvalósítani. 

## Kivételkezelés

A kivétel a program futása során előálló rendellenes állapot, amely közbeavatkozás nélkül a program futásának abnormális megszakadását eredményezheti. A kivételes helyzetek kezelésének elmulasztása például a hálózati a kommunikáció, vagy az adatbázis tranzakció félbeszakadásával járhat úgy, hogy mindeközben meghatározatlan állapotba kerül a rendszer.
A lényeg, hogy amikor egy hiba megjelenik a programban, azaz egy kivételes esemény történik, a program normális végrehajtása megáll, és átadódik a vezérlés a kivételkezelő mechanizmusnak.

A Java kivételkezelése a C++ kivételkezelésére alapul.
A kivételkezelés eszköze a try és a catch utasítás, míg a manuális kivétel kiváltásra szolgál a throw utasítás. A kivételkezelő blokk végén a finally mindenképpen lefut.
 
A program azon részeit, ahol a kivételek keletkezhetnek, és amiket utána kivétel kezelő részek követnek, a program védett régióinak nevezzük.
A kivétel bekövetkezésekor a throwbeli kifejezés típusának megfelelő catch blokk hívódik meg, ezt a veremben visszafelé haladva keresi meg a rendszer. A verem tartalmát az adott pontig kiüríti a rendszer, végrehajtja a catch blokkot, majd a try utáni sorral folytatja a végrehajtást.
 
### Kivétel létrehozása

Beépített kivétel osztályok mellett létrehozhatunk sajátokat is.
Java:
Ha akarunk, akár saját kivételeket is hozhatunk létre bármely kivétel osztály specializálásával. Ekkor egy osztályt az Exception osztályból kell származtatni és meg kell hívni az ősosztály konstrukturát.
 
C++:
```
class MyException : public std::exception { 
      std::string _msg; 
      public:
         MyException(const std::string& msg) : _msg(msg){} 
         virtual const char* what() const noexcept override { 
               return _msg.c_str(); 
         } 
};
```