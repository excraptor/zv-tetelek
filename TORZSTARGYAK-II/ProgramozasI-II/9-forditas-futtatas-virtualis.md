
# 9. Java és C++ programok fordítása és futtatása. Parancssori paraméterek, fordítási opciók, nagyobb projektek fordítása. Absztrakt-, interfész- és generikus osztályok, virtuális eljárások. A virtuális eljárások megvalósítása, szerepe, használata


## C++ fordítás, futtatás

### Előfordítás

Első lépésben az előfordító(preprocessor) a tényleges fordítóprogram futása előtt szövegesen átalakítja a forráskódot.
Az előfordító különböző szöveges változtatásokat hajt végre a forráskódon, előkészíti azt a tényleges fordításra.
Feladatai:
- **Header fájlok beszúrása. (*.hpp/.h)**
- A **forrásfájlban (*.cpp)** fizikailag több sorban elhelyezkedő forráskód logikailag egy sorbatörténő csoportosítása (ha szükséges).
- A kommentek helyettesítése whitespace karakterekkel.
- Az előfordítónak a programozó által megadott feladatok végrehajtása (szimbólumokbehelyettesítése, feltételes fordítás, makrók, stb.) 
A leggyakoribb műveletei a szöveghelyettesítés (#define), a szöveges állomány beépítése (#include) valamint a program részeinek feltételtől függő megtartása
- Az előfeldolgozó az #include direktíva hatására az utasításban szereplő szöveges fájl tartalmát beszúrja a programunkba, a direktíva helyére.

### Fordítás

Fordításkor a forrásfájlokból az első lépésben **tárgymodulok (*.o) keletkeznek**, önmagukban nem futóképesek. 
Ezt követően szükség van egy szerkesztőre, ami ezeket a modulokat összeszerkeszti.
Linux/Unix rendszerek esetén a fordító a **gcc**. Az alábbi módon tudjuk lefordítani a több forrásfájlból álló projektet: 
**gcc -o prog main.cpp class1.cpp class2.cpp**
Felsoroljuk azokat a fájlokat (a felsorolás sorrendje lényegtelen), amiket le szeretnénk fordítani. Fontos a main.cpp megadása hiszen ez a program belépési pontja.
A **-o prog**, megadásakor megadhatjuk a program nevét, ekkor prog néven hozza létre az .exe fájlt. Ha nem mondunk semmit, akkor az alapértelmezett exe fájl neve a.out lesz. Célszerű használni a -o kapcsolót. Az exe kiterjesztés csak Windows esetén van, Linux esetén csak futtatási jogú fájlt kapunk.
A fordító először mindegyiket lefordítja, melyek a .o kiterjesztésű tárgymodul fájlok lesznek, majd ezek összeszerkesztésre kerülnek

### Fordítási lehetőségek

- forrásfájlokból kiindulva: gcc -o prog class1.cpp class2.cpp
    - Ekkor modulonként létrejönnek a tárgymodulok .o kiterjesztéssel. 
    - Amennyiben több forrásfájl van, akkor megoldható: gcc -o prog *.cpp -ként is.
- tárgymodul és forrásfájl megadásával: Amely modulok nem változtak meg, azokat felesleges újrafordítani, tehát megadhatjuk tárgymodul és forrásfájl megadásával
    - F: gcc -o prog class1.o class2.cpp
- tárgymodulkönyvtár és forrásfájl felhasználásával:
    - a tárgymodulkönyvtár kiterjesztése .a
    - Tárgymodulkönyvtárat létrehozni (archiver) (-cr : create): ar -cr liba.a a.o
    - F: gcc -o prog b.cpp liba.a
- csak tárgymodulok felhasználásával: ekkor a -c kapcsolóval csak fordítást végzünk, szerkesztést nem.
    - F: gcc -c a.cpp b.cpp: Ekkor a.o és b.o tárgymodulokat kapunk
    - Ezt követően az ld nevű (link editor) szerkesztőprogrammal kell összeszerkeszteni a modulokat.
    - F: ld -o prog a.o b.o

### A gcc fordító fontosabb fordítási opciói

Szintaxis: gcc [kapcsolók] forrásfájlok
- **-Ob[szint]**: A gcc fordítónak a -Ob[szint] kapcsolóval tudjuk megmondani, hogy milyen optimalizálásokat alkalmazzon, a szint maximum 3 lehet (0,1,2), inline eljárások.
- **-c**: mint compile, lefordítja és összeállítja a forrást, linkelést nem végez.
- **-o**: lehetőségünk van megadni a futtatható állomány nevét, amennyiben nem adunk meg, az alapértelmezett az a.out lesz.
- **-Wall**: A figyelmeztetéseket írja ki.
- **-g**: engedélyezi a hibakeresési információk elhelyezését a programban, ami emiatt sokkal nagyobb lesz, de nyomon lehet követni a futását például a gdb programmal.
- **-Werror:** Forditás-idejű figyelmeztetéseket errorokká alakítja.

### C++ parancssori paraméterek

int main(int argc, char* argv[])

A C++ programok kezdő eljárása minden esetben a main() eljárás. A main függvény első két paramétere az argc, ami egy int és az argv tömb:
- az argc a parancssorban szereplő argumentumok száma,
- az argv a string alakban tárolt argumentumok címeit tároló tömb, az első argumentum címe argv[0], a másodiké argv[1], …, az utolsó argumentum után egy NULL pointer következik. Az argv[0] a program nevét és útvonalát tartalmazza. A paraméterek valójában az 1 indextől kezdődnek.

## Java fordítás, futtatás:

Ahhoz, hogy Java programokat tudjunk futtatni, illetve fejleszteni, szükségünk lesz egy fordító- és/vagy futtatókörnyezetre, valamint egy fordítóprogramra. A kész programunk futtatásához mindösszesen a JRE (Java Runtime Environment) szükséges, ami biztosítja a Java alkalmazások futtatásának minimális követelményeit, mint például a JVM (Java Virtual Machine)
Azonban a fejlesztéshez szükségünk lesz a JDK-ra (Java Development Kit) is. Ez tartalmazza a Java alkalmazások futtatásához, valamint azok készítéséhez, fordításához szükséges programozói eszközöket is (tehát a JRE-t nem kell külön letölteni, a JDK tartalmazza).
A fordítás folyamata az alábbiak alapján történik:

- Először a **.java** kiterjesztésű fájlokat a Java-fordító (compiler) egy közbülső nyelvre fordítja
- **Java bájtkódot kapunk eredményül** (ez a bájtkód hordozható). A java bájtkód a számítógép számára még nem értelmezhető. (kiterjesztése .class)
- Ennek a kódnak az értelmezését és fordítását gépi kódra a JVM (Java Virtual Machine) végzi el futásidőben.
 
**Fordítás:** javac filename.java
**Futtatás:** java filename

**Java fordítási opciók:**
- -g: debug információk generálása
- -s <könyvtár>: a generált fájlok könyvtárának megadása
- -sourcepath <path>: a forrásfájlok elérési útvonalát meg lehet adni
- -Werror: figyelmeztetés esetén megáll a fordítás
Java parancssori paraméterek
public static void main(String[] args)
A main függvény paramétere az args string tömb, amely tartalmazza a parancssori paramétereket. Ezen a tömbön valamilyen ciklus segítségével végig iterálhatunk és a parancsori paramétereket tetszés szerint kezelhetjük.

Nagyobb projektek esetén szokás build fájlokat alkalmazni: ant, gradle, makefile, stb.

## Virtuális eljárások

Egy virtuális eljárás címének meghatározása indirekt módon, futás közben történik.
Java-ban eleve csak virtuális eljárások vannak (kivéve a final metódusokat, amelyeket nem lehet felüldefiniálni és a private metódusokat, amelyeket nem lehet örökölni)

C++-ban a virtuális függvénytábla tartja nyilván a virtuális eljárások címeit. A VFT táblázat öröklődik, feltöltéséről a konstruktor gondoskodik. A származtatott osztály konstruktora módosítja a virtuális függvénytáblát, kijavítja az ősosztályból örökölt metóduscímeket. Amikor a konstruálási folyamat véget ér, a VFT táblázat minden sora értéket kap, mégpedig a ténylegesen létrehozott osztálynak megfelelő metódus címeket. A VFT táblázat sorai ezután már nem változnak meg.

- Virtuális eljárásokat a virtual kulcsszóval tudunk létrehozni. Az újrafelhasználás során nagy valószínűséggel módosításra kerülő eljárásokat a szülő osztályokban célszerű egyből virtuálisra megírni, mert ezzel jelentős munkát lehet megtakarítani a későbbiekben.
  
**Java:**

Absztrakt osztályok
- Az abstract kulcsszóval hozható létre. 
- Egy absztrakt osztályból nem hozható létre objektum.
- Tartalmazhat absztrakt metódusokat (absztrakt metódusnak nincs implementációja, azaz törzse), illetve nem absztraktokat
- Gyerek osztályban az abstract metódusokat felül KELL definiálni, ha példányosítható osztályt szeretnénk
- Ha egy osztály rendelkezik legalább egy absztrakt metódussal, akkor osztálynak is absztraktnak kell lennie
- Lehetnek adattagjai

Interfész
- Az interface kulcsszóval lehet létrehozni
- Egy speciális absztrakt osztály
- Nincsenek sem megvalósított metódusok, sem adattagok. Csupán metódus deklarációkat tartalmaz
- Gyerekosztályban az implements kulcsszóval lehet implementálni


C++:
Absztrakt osztályok:
A törzs nélküli virtuális eljárásokat pure virtual eljárásoknak nevezzük (pl.: virtual int getArea() = 0;). A pure virtual eljárás egy üres (NULL) bejegyzést foglal el a VFT (Virtual Function Table) táblázatban. Ha egy osztály ilyen eljárást tartalmaz, akkor azt absztrakt osztálynak nevezzük amiatt, mert ebből az osztályból objektum példányokat létrehozni nem lehet. A gyermek osztályokban minden pure virtual eljárást megfelelő törzzsel kell ellátni, ezt a fordító ellenőrzi. Amíg egyetlen pure virtual eljárás is marad, az osztály absztrakt lesz.

 
## Generikus osztályok

Az generikus programozás módszere a kód hatékonyságának növelése érdekében valósul meg. Az általános programozás lehetővé teszi a programozó számára, hogy általános algoritmust írjon, amely minden adattípussal működik. Nincs szükség több, különféle algoritmusok létrehozására, ha az adattípus egész szám, karakterlánc vagy karakter.

Java
Lehetőség nyílt az osztályok paraméterezésére más típusokkal.
Gyakorlatilag statikus polimorfizmusról van szó, egy típusparamétert adunk meg, mivel az osztály maga úgy lett megírva, hogy a lehető legáltalánosabb legyen, és ne kelljen külön IntegerList, StringList, AllatList, stb. osztályokat megírnunk, hanem egy általános osztályt, mint sablont használunk, és a tényleges típust a kacsacsőrök között mondjuk meg.
Primitív típussal nem lehet paraméterezni, az fordítási hibát okoz.
 
A típusparamétereket konvenció szerint egyetlen nagybetűvel szokás elnevezni, hogy egyértelműen megkülönböztethető legyen.
Gyakori elnevezések:
- E : Element (tárolók használatánál)
- K : Key
- N : Number
- T : Type
- V : Value

Néha szükség lehet, hogy a típusparaméterre valamilyen megszorítást tegyünk:

- public class NaturalNumber<T extends Integer>
- Wildcard-ok, ismeretlen típusok:
    - public void process(List<? extends Foo> list)
        - minden olyan listára, ami vagy a Foo, vagy annak leszármazottaiból áll
    - public void addNumbers(List<? super Foo> list)
        - minden olyan listára, ami vagy a Foo, vagy annak őseiből áll

C++
C++-ban generikus osztályokat sablonok (template) segítségével tudunk létrehozni.
A függvénysablonok speciális funkciók, amelyek genrikus típusokkal működhetnek. Ez lehetővé teszi számunkra, hogy létrehozzunk egy függvénysablont, amelynek funkcionalitása egynél több típushoz vagy osztályhoz igazítható anélkül, hogy megismételnénk az egyes típusok teljes kódját.

