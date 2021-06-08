# 16. Processzusok kommunikációja, versenyhelyzetek, kölcsönös kizárás. Konkurens és kooperatív processzusok. Kritikus szekciók és megvalósítási módszereik: kölcsönös kizárás tevékeny várakozással (megszakítások tiltása, változók zárolása, szigorú váltogatás, Peterson megoldása, TSL utasítás). Altatás és ébresztés: termelő-fogyasztó probléma, szemaforok, mutex-ek, monitorok, Üzenet, adás, vétel. Írók és olvasók problémája. Sorompók


## Processzusok kommunikációja, versenyhelyzetek, kölcsönös kizárás.

### Processzusok kommunikációja

- A processzusoknak szükségük vannak a kommunikációra
    - Adatok átadása az egyik folyamatból a másiknak (Pipelining)
    - Közös erőforrások használata (memória, nyomtató, stb.)

Versenyhelyzet

- Kooperatív processzusok közös tárolóterületen dolgoznak (olvasnak és írnak).
- Processzusok közös adatot olvasnak és a végeredmény attól függ, hogy ki és pontosan mikor fut
- Megoldás: Egyszerrecsak egy folyamat lehet kritikus szekcióban. Amíg a folyamat kritikus szekcióban van, azt nem szabad megszakítani. Ebből a megoldásból származhatnak új problémák.

## Kölcsönös kizárás

- Az a módszer, ami biztosítja, hogy ha egy folyamat használ valamilyen megosztott, közös adatot, akkor más folyamatok ebben az időben ne tudják azt elérni
- pl.: egy adott időben csak egy processzus számára engedélyezett, hogy a nyomtatónak utasításokat küldjön
- Kölcsönös kizárás miatt előfordulható problémák: 
    - holtpont (deadlock): processzusok egymásra befejeződésére várnak, hogy a várt erőforrás felszabaduljon
    - éhezés (starvation): egy processzusnak határozatlan ideig várnia kell egy erőforrás használatára

Kritikus szekció

- A program azon része, amelyben a programunk a közös adatokat használja
- Szabályok: 
    - legfeljebb egy proc lehet kritikus szekciójában
    - kritikus szekción kivüli proc nem befolyásolhatja másik proc kritikus szekcióba lépését
    - véges időn belül bármely kritikus szekciüba lépni kivánó proc beléphet


## Kritikus szekciók és megvalósítási módszereik: kölcsönös kizárás tevékeny várakozással (megszakítások tiltása, változók zárolása, szigorú váltogatás, Peterson megoldása, TSL utasítás).

Láthattuk, hogy a kritikus szekcióba való belépés nem feltétel nélküli. Hogyan biztosíthatjuk a kölcsönös kizárás teljesülését?
- Hardware-es módszer
    - Megszakítások tiltásával
        - letiltjuk a megszakítást a kritikus szekcióba lépés után, majd újra engedélyezzük, mielőtt elhagyja azt, így nem fordulhat elő óramegszakítás, azaz a CPU nem fog másik processzusra váltani
        - jól használható, de általánosan nem biztos, hogy a legszerencsésebb
            - a legegyszerűbb hiba, hogy elfelejtjük újra engedélyezni a megszakítást a kritikus szekció végén
    - TSL utasítás segítségével
        - A mai rendszerekben a processzornak van egy „TSL reg, lock” (TSL EAX, lock) formájú utasítása (TSL – Test and Set Lock).
        - Ez az utasítás beolvassa a LOCK memóriaszó tartalmát a „reg” regiszterbe, majd egy nem nulla értéket ír a „lock” memóriacímre.
        - A CPU zárolja a memóriasínt, azaz tiltva van a memória elérés a CPU-knak a művelet befejezéséig.
        - A művelet befejezésekor 0 érték kerül a LOCK memóriaterületre
- Szoftware-es módszer
    - Szigorú váltogatás módszere
         	A folyamat			B folyamat
        - 
    - Peterson-féle megoldás
        - Van két metódus a kritikus szekcióba való belépésre (enter_region) és kilépésre (leave_region). A kritikus szekcióba lépés előtt a processzus meghívja az enter_region eljárást, kilépéskor pedig a leave_region eljárást. Az enter_region eljárás biztosítani fogja, hogy a másik processzus várakozik, ha szükséges.
        - 
    - Változók zárolása
        - Van egy osztott zárolási változó, aminek a kezdeti értéke 0. Kritikus szekcióba lépés előtt a processzus teszteli ezt a változót. Ha 0 az értéke, akkor 1-re állítja és belép a kritikus szekcióba. Ha az értéke 1, akkor várakozik, amíg nem lesz 0.

## Altatás és ébresztés: termelő-fogyasztó probléma, szemaforok, mutex-ek, monitorok, Üzenet, adás, vétel. 

### Altatás-ébresztés

Ahogy láttuk az előző, tevékeny várakozást használó versenyhelyzet-elkerülő megoldásokban a legfontosabb gond az, hogy processzoridőt pazarolnak. Ahhoz, hogy a drága processzoridőt se pazaroljuk, olyan megoldást lehet javasolni, ami vagy blokkolni tud egy folyamatot (aludni küldi), vagy fel tudja ébreszteni ebből a blokkolt állapotból.

A tevékeny várakozás feloldására az egyik eszköz a sleep-wakeup rendszerhívás páros. A lényege, hogy a sleep rendszerhívás blokkolja a hívót, azaz fel lesz függesztve, amíg egy másik processzus fel nem ébreszti. A wakeup rendszerhívás a paraméterül kap egy processzus azonosítót, amely segítségével felébreszti az adott processzust, tehát nem lesz blokkolva továbbá.

Termelő-fogyasztó probléma

Véges méretű memóriaterületen (tárolón) dolgozik két processzus (osztoznak). A gyártó adatokat helyez el a tárolón, a fogyasztó kiveszi az adatokat a tárolóból és feldolgozza azokat, viszont a memória véges. Ha a tároló tele van és a gyártó elemet akar berakni, akkor elalszik, majd felébreszti a fogyasztó, ha egy elemet kivesz a tárolóból. Fordítva is: ha a tároló üres, és a fogyasztó ki akar venni egy elemet, akkor elalszik, és majd felébreszti a gyártó, ha legyártott egy eleme

Szemafor

- „A vonat megáll egy piros szemafor előtt, és addig várakozik, amíg szabad utat nem kap, mert valamilyen oknál fogva (elaludt a bakter, foglalt a pálya stb.) a továbbhaladás meg van tiltva.”
- A szemafor a számítógép-programozásban használt változó vagy absztrakt adattípus, amit az osztott erőforrásokhoz való hozzáférések szabályozásához használnak a többszálú környezetekben. 
- Ha értéke pozitív, akkor nyitott állapotban van, ha nulla, akkor tilosat mutat
- Amekkora értékkel inicializáljuk a szemafort annyi „vonatot” enged át, mielőtt tilosat mutatna.
- pl.: Tekintsünk egy egész számot. Legyen, mondjuk, a kezdőértéke egy. Amikor a kritikus művelethez érek, akkor azt mondom, hogy jelzem az erőforrás-használati igényemet. A jelzés jelentse azt, hogy eggyel csökkentem a szám értékét. Ezt szokás „down” vagy sok más helyen „P” operációnak is nevezni. Ha a csökkentés eredmény nem negatív lesz, akkor szabad az út, és végzi a dolgát a program. Ha ezután érkezik egy másik folyamat, ami ugyanezt az erőforrást szeretné használni, szintén hasonló módon kezdi a dolgot, de neki már a P operáció pirosra állítja a szemafort hiszen az „egész” értéke mínusz egy lesz. Ekkor ez a második folyamat mindaddig vár, amíg a szemafor értékét egy úgynevezett „up” vagy „V” operációval – ami az eggyel való növelést jelenti – fel nem szabadítja az erőforrást ami után a P operációnál várakozó program tovább haladhat. Ezzel tulajdonképpen újra tilos jelzés lesz érvényben a kritikus erőforrásra a kezdőérték egy volt.

Mutex

- Olyan speciális szemafor, amelynek csak két értéke lehet
- Ha csak kölcsönös kizárás biztosítására kell a szemafort létrehozni, és nincs szükség annak számlálási képességére, akkor azt egy kezdőértékkel hozzuk létre. Ezt a kétállapotú (értéke 0 és 1) szemafort sok környezetben speciális névvel, az angol kölcsönös kizárás kifejezésből mutexnek nevezzük.
- Ha egy folyamatnak zárolásra van szüksége, a „mutex_lock” eljárást hívja, míg ha a zárolást meg akarja szüntetni, a „mutex_unlock” utasítást hívja.
- Aki másodszor (vagy harmadszor) hívja a „mutex_lock” eljárást, az blokkolódik, és csak a „mutex_unlock” hatására tudja folytatni a végrehajtást.

Monitor

- Eljárások, változók ás adatszerkezetek együttese egy speciális modulba összegyűjtve, hogy használható legyen a kölcsönös kizárás megvalósítására
- Legfontosabb tulajdonsága, hogy egy adott időpillanatban csak egy proc lehet aktív benne
- A processzusok bármikor hívhatják a monitorban lévő eljárásokat, de nem érhetik el a belső adatszerkezeteit (mint OOP-nál)
- wait(c): alvó állapotba kerül a végrehajtó proc
- signal(c): a c miatt alvó procot felébreszti

Üzenet, adás, vétel.

- Folyamatok együttműködéshez információ cserére van szükség. Két mód: 
    - közös tárterületen keresztül
    - kommunikációs csatornán keresztül (egy vagy kétirányú) 
- Folyamat fommunikáció fajták:
    - Közvetlen kömmunikáció
        - csak egy csatorna létezik, és más folyamatok nem használhatják
        - 
    - Közvetett kommunikáció
        - Közbülső adatszerkezeten (pl. postaládán (mailbox)) keresztül valósul meg.
        - 
    - Aszimmetrikus
        - Adó vagy vevő megnevezi, hogy melyik folyamattal akar kommunikálni
        - A másik fél egy kaput (port) használ, ezen keresztül több folyamathoz, is kapcsolódhat. 
        - Tipikus eset: a vevőhöz tartozik a kapu, az adóknak kell a vevő folyamatot és annak a kapuját megnevezni. (Pl. szerver, szolgáltató folyamat)
        - 
    - Üzenetszórás
        - A közeg több folyamatot köt össze.
        - 
- Műveletek:
    - send(cél, &üzenet)
    - receive(forrás, &üzenet)

## Írók és olvasók problémája. Sorompók.

### Írók és olvasók problémája

Több proc egymással versengve írja és olvassa ugyanazt az adatot. Megengedett az egyidejű olvasás, de ha egy proc írni akar, akkor más procok sem nem írhatnak se nem olvashatnak. (pl, adatbázisok, fájlok, hálózat)

Sorompók:
- Sorompó primitív
    - Könyvtári eljárás
- Fázisokra osztjuk az alkalmazást
- Szabály
    - Egyetlen processzus sem mehet tovább a következő fázisra, amíg az összes processzus nem áll készen
- Sorompó elhelyezése mindegyik fázis végére
    - Amikor egy processzus a sorompóhoz ér, akkor addig blokkolódik ameddig az összes processzus el nem éri a sorompót
- A sorompó az utolsó processzus beérkezése után elengedi a azokat
- Nagy mátrix-okon végzett párhuzamos műveletek