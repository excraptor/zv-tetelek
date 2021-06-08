# 15. Processzusok, szálak/fonalak, processzus létrehozása/befejezése, processzusok állapotai, processzus leírása. Ütemezési stratégiák és algoritmusok kötegelt, interaktív és valós idejű rendszereknél, ütemezési algoritmusok céljai. Kontextus-csere

## Operációs rendszer

A számítógépeknek azt az alapprogramját, mely közvetlenül kezeli a hardvert, és egy egységes környezetet biztosít a számítógépen futtatandó alkalmazásoknak, op.rendszernek nevezzük.
Egy moder számítógép a következőkből áll:

- egy vagy több processzor
- memória
- lemezek
- I/O eszközök
- …

Ezen komponensek kezelése egy szoftver réteget igényel – Ez az op. rendszer
Feladatai:

- felhasználó kényelmének, védelmének biztosítása
- egy egységes környezetet biztosít a számítógépen futtatandó alkalmazásoknak
- a rendszer hatékonyságának, teljesítményének maximalizálása = erőforrások kezelése
- a programok végrehajtását vezérli
- biztosítja a felhasználó és a számítógépes rendszer közötti kommunikációt

Felépítése:

- Rendszerhéj (shell)
    - Feladata a parancsértelmezés.
    - Lehet a shell parancssoros ( CLI - Command Line Interface - mint, pl. DOS), vagy grafikus felületű
    - Kapcsolattartás a felhasználóval
- Alacsony szintű segédprogramok
    - felhasználói "élményt" fokozó kiegészítő programok (pl szövegszerkesztők, fordítóprogramok), amelyek nem képzik a rendszer elválaszthatatlan részét
- Kernel
    - az operációs rendszer alapja (magja), amely felelős a hardver erőforrásainak kezeléséért)
    - közvetlenül a hardverrel áll kapcsolatban.
    - Ki- és bemeneti eszközök kezelése (billentyűzet, monitor stb.)
    - Programok, folyamatok futásának kezelése
        - Indítás, futási feltételek biztosítása, leállítás
        - Memória-hozzáférés biztosítása
        - Processzor idejének elosztása

### Az operációs rendszerek csoportosítása

- Felhasználók száma szerint:
    - egy felhasználós pl.: DOS, Win 9x
    - több felhasználós pl. Linux, Win NT
- Hardver mérete szerint:
    - kisgépes (UNIX)
    - nagygépes (Main Frame, Cray - szuper számítógép)
    - mikrogépes (DOS, WIN 9X, UNIX)
- Processzorkezelés szerint:
    - egy feladatos (DOS)
    - több feladatos (WIN 9X, WIN NT, UNIX)
- Cél szerint: 
    - általános (DOS, WIN 9X, WIN NT, UNIX)
    - speciális (folyamatvezérlő operációs rendszerek)
- Operációs rendszer felépítése szerint:
    - monolitikus
        - A monolitikus operációs rendszer (mint például a UNIX) magja egyetlen programból áll. Ebben a programban az eljárások szabadon hívhatják egymást, a köztük levo kommunikáció eljárásparamétereken és globális változókon keresztül zajlik.
        - 
    - réteges szerkezetű (WIN NT, UNIX)
        - A rétegzett szerkezetu operációs rendszer magja több modulból áll, és a modulok között egy export-import hierarchia figyelheto meg: minden modul kizárólag a hierarchiában alatta levo modul interfészét használja.
    - kliens/szerver felépítésű - Hálózati operációs rendszer
        - a szerveren fut, és lehetővé teszi a szervernek az adatok, felhasználók, csoportok, alkalmazások, a hálózati biztonság és egyéb hálózati funkciók kezelését.
        - A kliens/szerver hálózati operációs rendszerek lehetővé teszik funkciók és alkalmazások központosítását egy vagy több dedikált szerveren. A szerver a rendszer központja, engedélyezi az erőforrásokhoz való hozzáférést és biztonságos kapcsolatot nyújt
    - vegyes
    - virtuális gépek
        - A virtuális gépeken alapuló operációs rendszerben központi részen helyezkednek el a virtuális gépeket menedzselo (hypervisor) rendszerrutinok. Ez a program lehetové teszi a hardver eroforrásainak (CPU, diszk, perifériák, memória, ...) több operációs rendszer közötti hatékony elosztását. A hypervisor leggyakrabban a számítógép hardverét "többszörözi meg" úgy, hogy a rajta futó operációs rendszerek azt higgyék, hogy övéké az egész gép (pedig "csak" egy virtuális gépen futnak)
- A felhasználói felület szerint:
    - szöveges (DOS, UNIX)
    - grafikus (WINDOWS)

### Op. rendszer generációk

- Első generációs (1945-1955)
    - nincs os. leginkább csak hardver elemekből állt ( különféle kapcsolók, címkiválasztó kulcsok, indító-, megállító-, lépésenkénti végrehajtást kiváltó gombok stb.
    - programozó=gépkezelő=programok végrehajtásának vezérlője
    - bináris kódolás

- Második generáció (1955-1965)
    - os van
    - egyidejűleg 1 processzus
    - fortran programozás
- Harmadik generációs (1965-1980)
    - os van, szoftverrel megvalósított operációs rendszer
    - integrált áramkörök, multiprogramozás
    - egyidejűleg több proc
    - CPU időszeletelés (time slicing): egy processzus egy meghatározott max időintervallumon keresztül használhatja a CPU-t folyamatosan (ez a tmax idő). Ha ez letelik az op.rendszer processzus ütemező átadja a CPU-t egy másik processusnak
    - Átmeneti tárolás (spooling): az I/O adatok először gyors háttértárolókra kerülnek, majd a processzus innen kapja/ide írja az adatait
- Negyedik generációs (1980-tól)
    - személyi számítógépek
    - parancssoros, grafikus felület
    - pc, workstation: egyetlen felhasználó, egy időben több feladat (Windows, MacOS)
    - hálózati os: hálózaton keresztül több felhasználó, kapcsolódik, minden felhasználó több feladatot futtathat (Unix, Linux)
    - osztott os: egy feladatot egy időben több számítógépes rendszer végez

## SZERINTEM INNENTŐL KELL

## Processzusok, szálak/fonalak, processzus létrehozása/befejezése, processzusok állapotai, processzus leírása

### Processzus

- A végrehajtás alatt lévő program.
- Szekvenciálisan végrehajtódó program
- Egyidejűleg több processus létezik: A processzor idejét meg kell osztani az egyidejűleg létező processzusok között: időosztás (time sharing)
- Futó processzusok is létrehozhatnak processzusokat: Kooperatív folyamatok, egymással együttműködő, de amúgy független processzusok
- Az erőforrásokat az OS-től kapják (centralizált erőforrás kezelés)
- jogosultságokkal rendelkeznek
- Előtérben és áttérben futó folyamatok
Processus állapotok:
- Futáskész: készen áll a futásra, csak ideiglenesen le lett állítva, hogy egy másik processzus futhasson
- Futó: a proc bitrokolja a CPU-t
- Blokkolt: bizonyos külső esemény bekövetkezéséig nem képes futni
- Iniciális
- Terminális
- Felfüggesztett

### Processzustáblázat és PCB

A proc nyilvántartására, tulajdonságainak leírására szolgáló memóriaterület.
Processusonként egy egy bejegyzés - Processzus vezérlő blokk (PCB)
PCB tartalma:

- azonosító: processzus id
- processzus állapota
- CPU állapota: a kontextus cseréhez
- jogosultságok, prioritás
- birtokolt erőforrások

### Processzus létrehozása

- Futó processzusok is létrehozhatnak processzusokat: Kooperatív folyamatok, egymással együttműködő, de amúgy független processzusok
- Egyszerű esetekben megoldható, hogy minden processzus elérhető az OS elindulása után
- Általános célú rendszerekben szükség van a processzusok létrehozására és megszüntetésére
- Processzusokat létrehozó események:
    - Rendszer inicializálása
    - Felhasználó által kezdeményezett
    - Kötegelt feladat kezdeményezése
- Az OS indulásakor sok processzus keletkezik:
    - Felhasználókkal tartják a kapcsolatot: Előtérben futnak
    - Nincsenek felhasználóhoz rendelve:
        - Saját feladatuk van
        - Háttérben futnak
- Lépései:
    1. Memóriaterület foglalása a PCB számára
    2. PCB kitöltése iniciális adatokkal
    3. Programszöveg, adatok, verem számára memóriafoglalás, betöltés
    4. A PCB procok láncra fűzése, futáskész állapot. Ettől kezdve a proc osztozik a CPU-n.

### Processzus befejezése
- Szabályos kilépés (exit(0)): önkéntes, végzett a feladatával
- Kilépés hiba miatt
- Kilépés végzetes hiba miatt: önkéntelen, illegális utasítás, nullával osztás
- Egy másik proc megsemmisíti: önkéntelen, mésik proc kill() utasítására
- Lépései:
        1. Gyermek procok megszüntetése (rekurzívan)
        2. PCB procok láncról való levétele, terminális állapot. Ettől kezdve a proc nem osztocik a CPU-n
        3. Proc bitrokában lévő erőforrások felszabadítása (pl. fájlok lezárása)
        4. A memóriatérképnek (konstansok, változók, dinamikus változók) megfelelő memóriaterület felszabadítása
        5. PCB memóriaterületének felszabadítása

### Szálak/fonalak (thread)

- Önálló végrehajtási egységként működő program, objektum, szekvenciálisan végrehajtható utasítás-sorozat
- A proc hozza létre (akár többet is egyszerre)
- Osztozik a létrehozó proc erőforrásain
- Egy folyamaton belül több tevékenység végezhető párhuzamosan
- Szálak megvalósítása:
    - A felhasználó kezeli a szálakat egy függvénykönyvtár segítségével. Ekkor a kernel (az operációs rendszer alapja (magja), amely felelős a hardver erőforrásainak kezeléséért) nem tud semmit a szálakról
    - A kernel kezeli a szálakat. Szálak létrehozása és megszüntetése kernelhívásokkal történik

## Ütemezési stratégiák és algoritmusok kötegelt, interaktív és valós idejű rendszereknél, ütemezési algoritmusok céljai

### Ütemező

- Egy CPU áll rendelkezésre. Processzusok versengenek a CPU-ért
- Az OS dönti el, hogy melyik kapja meg a CPU-t
- Az ütemező (scheduler) hozza meg a döntést  Ütemezési algoritmus
- Feladata:  Egy adott időpontban futáskész procok közül egy kiválasztása, amely a következőkben a CPU-t bitrokolni fogja
- Mikor kell ütemezni?: amikor egy processus befejeződik vagy blokkolódik
- Céljai:
    - a CPU legyen jól kihasznált
    - az átfutási idő (proc létrejöttétől megszűnéséig eltelt idő) legyen rövid
    - egységnyi idő alatt minél több proc teljesüljön

### Ütemezés kötegelt rendszerekben

A manapság haszálatos op.rendszerek nem tartoznak a kötegelt rendszerek (: Előre meghatározott sorrend szerint végrehajtandó feladatok együttese.) világába, mégis érdemes röviden megemlíteni ezek ütemezési típusait.
- Sorrendi ütemezés: 
    - Futásra kész folyamatok egy várakozó sorban helyezkednek el.
    - A sorban levő első folyamatot hajtja végre a központi egység. Ha befejeződik a folyamat végrehajtása, az ütemező a sorban következő feladatot veszi elő.
    - Új feladatok a sor végére kerülnek
    - Ha az aktuálisan futó folyamat blokkolódik, akkor a sorban következő folyamat jön, míg a blokkolt folyamat, ha újra futásra kész lesz, akkor a sor végére kerül, és majd idővel újra rá kerül a vezérlés.
- Legrövidebb feladat először:
    - az a folyamat kerül először ütemezésre, melyiknek a legkisebb a futási ideje.
    - az alkalmazhatóság szempontjából nem ideális, ha nem tudjuk előre a folyamatok végrehajtási idejét.
- Legrövidebb maradék futásidejű:
    - Ismerni kell a folyamatok futási idejét előre.
    - Amikor új folyamat érkezik, vagy a blokkolás miatt egy következő folyamathoz kerül a vezérlés, akkor nem a teljes folyamat végrehajtási idejét, hanem csak a hátralévő időt vizsgálja az ütemező, és amelyik folyamatnak legkisebb a maradék futási ideje, az kerül ütemezésre

- Háromszintű futásidejű:
    - A feladatok a központi memóriában vannak, közülük egyet hajt végre a központi egység. Előfordulhat, hogy a többi feladat közül ki kell rakni egyet a háttértárba, mivel a működés során elfogyhat a memória.
    - Az a döntést, hogy a futásra jelentkező folyamatok milyen sorrendben kerüljenek be a memóriába, a bebocsátó ütemező hozza meg. 

### Ütemezés interaktív rendszereknél

- Round Robin
    - Az ütemező beállít egy időintervallumot egy időzítő segítségével és amikor az időzítő lejár megszakítást ad.
    - Megadott időközönként óramegszakítás következik be és ekkor az ütemező a következő folyamatnak adja a processzort.
    - A folyamatokat egy sorban tárolja a rendszer, és amikor lejárt az időszelet, akkor az a folyamat, amelyiktől az ütemező éppen elveszi a vezérlést, a sor végére kerül
- Prioritásos ütemezés
    - Felmerül az igény, hogy nem feltétlenül egyformán fontos minden egyes folyamat. 
    - A folyamatokhoz egy fontossági mérőszámot, prioritást (prioritási osztályt) rendel hozzá
    - A legmagasabb prioritású futáskész processzus kapja meg a CPU-t

### Ütemezés valós idejű rendszereknél

Alapvető szerepe van az időnek
Ha a feladatainknak nemcsak azt szabjuk meg, hogy hajtódjanak végre valamilyen korrekt ütemezés szerint, hanem az is egy kritérium, hogy egy adott kérést valamilyen időn belül ki kell szolgálni, akkor valós idejű op.rendszerről beszélünk.
A megfelelő határidők betartása úgy valósítható meg, hogy egy programot több folyamatra bontunk, és ezeknek a rövid folyamatoknak az ütemező biztosítja a számukra előírt határidő betartását
- Szigorú valós idejű rendszer
    - a határidő betartása kötelező
- Toleráns valós idejű (soft real-time) rendszer
    - a határidők kis mulasztása még elfogadható, tolerálható.

### Kontextus csere

Egy CPU van és több egyidejűleg létező processzus. A CPU váltakozva hajtja végre a processzusokat. A kontextus csere, amikor a CPU átvált P1 processzusról a P2 processzusra. Ilyenkor P1 állapotát el kell menteni a CPU regisztereiből, az erre fenttartott memóriaterületre, majd P2 mentett állapotát vissza kell állítani a CPU regisztereiben.


## SZERINTEM INNENTŐL MÁR NEM KELL 

Operációs rendszerek feladatai, fajtái, felépítései és felhasználási területei. Párhuzamossággal kapcsolatos fogalmak, problémák és megoldásaik. Folyamatok, szálak fogalma, megvalósításaik és ütemezési módszereik. Memóriakezeléssel, állományrendszerekkel és szolgáltatásaikkal kapcsolatos fogalmak és megvalósítási módszereik


Memóriakezeléssel, állományrendszerekkel és szolgáltatásaikkal kapcsolatos fogalmak és megvalósítási módszereik
Memóriakezelés
A memória az egyik legfontosabb (és gyakran a legszűkösebb) erőforrás, amivel egy operációs rendszernek gazdálkodnia kell; főleg a többfelhasználós rendszerekben, ahol gyakran olyan sok és nagy folyamat fut, hogy együtt nem férnek be egyszerre a memóriába. A többfeladatos feldolgozás megjelenésével azonban szükségessé vált a memóriának a futó folyamatok közötti valamilyen „igazságos” elosztására. 
- Multiprogramozás megvalósítása rögzített memória szeletekkel.
    - Osszuk fel a memóriát n szeletre. (Fix szeletek) pl. rendszerindításnál ez megtehető
    - a főmemória kihasználása nem jó: minden program, méretétől függetlenül egy egész partíciót elfoglal.
    - Megoldás: nem egyenlő méretű partíciók
- Multiprogramozás megvalósítása memória csere használattal.
    - Teljes folyamat mozgatása memória-lemez között
    - Nincs rögzített memória partíció, mindegyik dinamikusan változik, ahogy az op.rendszer odavissza rakosgatja a folyamatokat.
        - Dinamikus, jobb memória kihasználtságú lesz a rendszer, de a sok csere lyukakat hoz létre!  Memória tömörítést kell végezni
- Multiprogramozás megvalósítása virtuális memória használatával.
    - Egy program használhat több memóriát mint a rendelkezésre álló fizikai méret.
    - Az operációs rendszer csak a „szükséges részt” tartja a fizikai memóriában
    - MMU - virtuális címek fizikai címekre való leképzése
- Multiprogramozás szegmentálással
A megoldást a virtuálismemória kezelés jelentette. Az operációs rendszer úgy szabadít fel memóriát az éppen futó program számára, hogy a memóriában tárolt, de éppen nem használt blokkokat (lapokat) kiírja a külső tárolóra, amikor pedig ismét szükség van rájuk, visszaolvassa őket.
Ilyenkor az operációs rendszer ad a központi memóriából egy akkora részt, amelyben a folyamat a legfontosabb részeit el tudja tárolni. A többit kirakja a háttértárra (az ún. lapozófájlba, Unix-ban ezt swap-nek hívják (a procok akkor is futhatnak ha csak részeik vannak a memóriában)). Ez a megoldás azért működik, mert a programok legtöbbször egy eljáráson belül ciklusban dolgoznak, nem csinálnak gyakran nagy ugrásokat a program egyik végéről a másikra. A központi egység fel van szerelve egy úgynevezett memóriakezelő egységgel (MMU), amely figyeli, hogy olyan kódrészre kerül-e a vezérlés, amely nincs benn a központi memóriában (mert például a háttértárra van kirakva). 
Memóriahasználat szerint a programokat 2 részre oszthatjuk:
- rezidens (állandóan a memóriában van, gyorsabb, tűzfal, vírusirtó)
- tranziens (csak meghíváskor töltődik be, helytakarékosabb)

Állományrendszerek (file system)
A számítógépek az adatokat különböző fizikai háttértárakon tárolhatják, a számítógép kényelmes használhatósága érdekében az operációs rendszerek egységes logikai szemléletet vezetnek be az adattárolásra és adattárakra
Az operációs rendszer támogatást nyújthat a fájl tartalmának kezelésében, a fájl szerkezetének (adatszerkezet) létrehozásában.
Állományrendszer: fájlok tárolásának és rendszerezésének a módszere, ideértve a tárolt adatokhoz való hozzáférése és az adatok egyszerű megtalálása is



Párhuzamossággal kapcsolatos fogalmak, problémák és megoldásaik
A CPU minden időpillanatban egy programot futtat, az egyik program végrehajtásáról a másik program végrehajtására vált. Ez a párhuzamosság illúzióját kelti a felhasználóban, de valójában nem erről van szó. Nem összekeverendő a többprocesszoros rendszerek valódi hardverpárhuzamosságával.


Valódi párhuzamosság:
- Többprocesszoros rendszerek
- Akár processzorok százai egy számítógépben 
- Közös sín, közös órajel, akár közös memória és perifériák, gyors kommunikáció
A párhuzamosítás tipikus megoldása az időosztás, amikor minden folyamat kap egy-egy ún. időszeletet, melynek leteltét követően egy másik folyamat kapja meg a vezérlést.
Párhuzamosság problémái: 
- a rendszerben futó folyamatok általában nem függetlenek
- Közös erőforrásokat használnak 
- függő folyamatok együttes viselkedése új típusú hibákat eredményezhet
- versenyhelyzetek kialakulása: párhuzamos végrehajtás által okozott nemdeterminisztikus hibás eredmény
Multiprogramozás: Ha az operációs rendszer egyidőben több programot futtat, multiprogramozásról beszélünk, melynek célja az erőforrások jobb kihasználása és a kényelem

