
# 16. Processzusok kommunikációja, versenyhelyzetek, kölcsönös kizárás. Konkurens és kooperatív processzusok. Kritikus szekciók és megvalósítási módszereik: kölcsönös kizárás tevékeny várakozással (megszakítások tiltása, változók zárolása, szigorú váltogatás, Peterson megoldása, TSL utasítás). Altatás és ébresztés: termelő-fogyasztó probléma, szemaforok, mutex-ek, monitorok, Üzenet, adás, vétel. Írók és olvasók problémája. Sorompók


## Processzusok kommunikációja, versenyhelyzetek, kölcsönös kizárás.

Processzus: **A végrehajtás alatt lévő program a memóriában.**

### Processzusok kommunikációja

- A processzusoknak szükségük vannak a kommunikációra
    - **Adatok átadása az egyik folyamatból a másiknak** (Pipelining)
    - **Közös erőforrások használata** (memória, nyomtató, stb.)


Kettő vagy több processzus egy-egy szakasza nem lehet átfedő, azaz két szakasz egymásra nézve **kritikus szekciók**.
**Kritikus szekció:** A program az a része, ahol előfordulhat versenyhelyzet.
**Szabályok:**
	1. Legfeljebb egy proc lehet kritikus szekciójában
	2. Kritikus szekción kívüli proc nem befolyásolhatja másik proc kritikus szekcióba lépését.
	3. Véges időn belül bármely kritikus szekcióba lépni kívánó proc beléphet.
	4. Processzusok sebessége közömbös


**Versenyhelyzet:**
Amikor több párhuzamosan futó folyamat közös erőforrást használ. A futás eredménye függ attól, hogy az egyes folyamatok mikor és hogyan futnak.

- Kooperatív processzusok közös tárolóterületen dolgoznak (olvasnak és írnak).
- Processzusok közös adatot olvasnak és a végeredmény attól függ, hogy ki és pontosan mikor fut

**Megoldás:** Egyszerrecsak egy folyamat lehet kritikus szekcióban. Amíg a folyamat kritikus szekcióban van, azt nem szabad megszakítani. Ebből a megoldásból származhatnak új problémák.

## Kölcsönös kizárás

- **Az a módszer, ami biztosítja, hogy ha egy folyamat használ valamilyen megosztott, közös adatot, akkor más folyamatok ebben az időben ne tudják azt elérni**
- pl.: egy adott időben csak egy processzus számára engedélyezett, hogy a nyomtatónak utasításokat küldjön
- Kölcsönös kizárás miatt előfordulható problémák: 
    - **holtpont (deadlock):** processzusok egymásra befejeződésére várnak, hogy a várt erőforrás felszabaduljon
    - **éhezés (starvation):** egy processzusnak határozatlan ideig várnia kell egy erőforrás használatára



## Kritikus szekciók és megvalósítási módszereik: kölcsönös kizárás tevékeny várakozással (megszakítások tiltása, változók zárolása, szigorú váltogatás, Peterson megoldása, TSL utasítás).

Láthattuk, hogy a kritikus szekcióba való belépés nem feltétel nélküli. Hogyan biztosíthatjuk a kölcsönös kizárás teljesülését?
- **Hardware-es módszerek**
    - **Megszakítások tiltásával**
        - letiltjuk a megszakítást a kritikus szekcióba lépés után, majd újra engedélyezzük, mielőtt elhagyja azt, így nem fordulhat elő óramegszakítás, azaz a CPU nem fog másik processzusra váltani
        - jól használható, de általánosan nem biztos, hogy a legszerencsésebb
            - a legegyszerűbb hiba, hogy elfelejtjük újra engedélyezni a megszakítást a kritikus szekció végén
    - **TSL utasítás segítségével**
        - A mai rendszerekben a processzornak van egy „TSL reg, lock” (TSL EAX, lock) formájú utasítása (TSL – Test and Set Lock).
        - Ez az utasítás beolvassa a LOCK memóriaszó tartalmát a „reg” regiszterbe, majd egy nem nulla értéket ír a „lock” memóriacímre.
        - A CPU zárolja a memóriasínt, azaz tiltva van a memória elérés a CPU-knak a művelet befejezéséig.
        - A művelet befejezésekor 0 érték kerül a LOCK memóriaterületre
- **Software-es módszer**
    - **Szigorú váltogatás módszere**
	    - A kölcsönös kizárás feltételeit teljesíti, kivéve azt hogy **egyetlen kritikus szekcíón kívüli folyamat sem blokkolhat másik folyamatot**
    - **Peterson-féle megoldás**
        - Van **két metódus a kritikus szekcióba való belépésre** (enter_region) és **kilépésre** (leave_region). 
        - A kritikus szekcióba lépés előtt a processzus meghívja az enter_region eljárást, kilépéskor pedig a leave_region eljárást. Az enter_region eljárás biztosítani fogja, hogy a másik processzus várakozik, ha szükséges.
        - **csak 2 processzus esetén müködik**
    - **Változók zárolása**
        - Van egy osztott zárolási változó, aminek a kezdeti értéke 0. Kritikus szekcióba lépés előtt a processzus teszteli ezt a változót. Ha 0 az értéke, akkor 1-re állítja és belép a kritikus szekcióba. Ha az értéke 1, akkor várakozik, amíg nem lesz 0.

## Altatás és ébresztés: termelő-fogyasztó probléma, szemaforok, mutex-ek, monitorok, Üzenet, adás, vétel. 

### Altatás-ébresztés

Ahogy láttuk az előző, tevékeny várakozást használó versenyhelyzet-elkerülő megoldásokban a legfontosabb gond az, hogy processzoridőt pazarolnak. Ahhoz, hogy a drága processzoridőt se pazaroljuk, olyan megoldást lehet javasolni, ami vagy blokkolni tud egy folyamatot (aludni küldi), vagy fel tudja ébreszteni ebből a blokkolt állapotból.

A **tevékeny várakozás feloldására az egyik eszköz a sleep-wakeup** rendszerhívás páros. A lényege, hogy a **sleep rendszerhívás blokkolja a hívót**, azaz fel lesz függesztve, amíg egy másik processzus fel nem ébreszti. A **wakeup rendszerhívás a paraméterül kap egy processzus azonosítót, amely segítségével felébreszti az adott processzust**, tehát nem lesz blokkolva továbbá.

### Termelő-fogyasztó probléma
Két processzus osztozik egy közös, rögzített méretű tárolón. A *termelő* adatokat tesz bele, a *fogyasztó* kiveszi azokat.
Ha a tároló tele van és a gyártó elemet akar berakni, akkor elalszik, majd felébreszti a fogyasztó, ha egy elemet kivesz a tárolóból. 
**Fordítva is:** ha a tároló üres, és a fogyasztó ki akar venni egy elemet, akkor elalszik, és majd felébreszti a gyártó, ha legyártott egy eleme

### **Szemafor**
- A szemafort 1965-ben Dijsktra hozta létre, amely **egy nagyon jelentős technika az egyidejű folyamatok kezelésére egy egyszerű egész érték használatával**
- Ez egy **megosztott egész változó**. Értéke pozitív vagy 0, és csak **várakozások** és **signal** műveleteken kereszütl érhetőek el.
- Két metódusa van a *down* és az *up*. (általánosítható a *sleep* és *wakeup*-ra)
	- **down** metódus megnézi, hogy az adott folyamat a szemaforon nagyobb-e mint 0. 
	- Ha igen, akkor **csökkent rajta eggyel**
	- Ha nem (tehát =0), akkor egyből altatásba rakja, nem növel rajta.
- Garantált, hogyha a szemafor elindult, akkor semelyik másik processzus nem érheti ezl a szemafort, amíg a feladat le nem futott, vagy blokkoltba került.
- Az **up** metódus a szemafor elérését növeli.

### **Mutex**

- Olyan speciális szemafor, amelynek **csak két értéke** lehet
- Ha csak kölcsönös kizárás biztosítására kell a szemafort létrehozni, és nincs szükség annak számlálási képességére, akkor azt egy kezdőértékkel hozzuk létre. 
- **Ezt a kétállapotú (értéke 0 és 1) szemafort** sok környezetben speciális névvel, az angol kölcsönös kizárás kifejezésből mutexnek nevezzük.
- Ha egy **folyamatnak zárolásra van szüksége, a „mutex_lock” eljárást hívja**, míg ha a **zárolást meg akarja szüntetni, a „mutex_unlock” utasítást hívja**.
- Aki másodszor (vagy harmadszor) hívja a „mutex_lock” eljárást, az blokkolódik, és csak a „mutex_unlock” hatására tudja folytatni a végrehajtást.

### Monitor

- Eljárások, változók ás adatszerkezetek együttese egy speciális modulba összegyűjtve, hogy használható legyen a kölcsönös kizárás megvalósítására
- Legfontosabb tulajdonsága, hogy egy adott időpillanatban csak egy proc lehet aktív benne
- A processzusok bármikor hívhatják a monitorban lévő eljárásokat, de nem érhetik el a belső adatszerkezeteit (mint OOP-nál)
- wait( c ): alvó állapotba kerül a végrehajtó proc
- signal( c ): a c miatt alvó procot felébreszti

### Üzenet, adás, vétel.

- Folyamatok együttműködéshez információ cserére van szükség. Két mód: 
    - közös tárterületen keresztül
    - kommunikációs csatornán keresztül (egy vagy kétirányú) 
- Folyamat fommunikáció fajták:
    - Közvetlen kömmunikáció
        - csak egy csatorna létezik, és más folyamatok nem használhatják
    - Közvetett kommunikáció
        - Közbülső adatszerkezeten (pl. postaládán (mailbox)) keresztül valósul meg.
    - Aszimmetrikus
        - Adó vagy vevő megnevezi, hogy melyik folyamattal akar kommunikálni
        - A másik fél egy kaput (port) használ, ezen keresztül több folyamathoz, is kapcsolódhat. 
        - Tipikus eset: a vevőhöz tartozik a kapu, az adóknak kell a vevő folyamatot és annak a kapuját megnevezni. (Pl. szerver, szolgáltató folyamat)
    - Üzenetszórás
        - A közeg több folyamatot köt össze.
- Műveletek:
    - send(cél, &üzenet)
    - receive(forrás, &üzenet)

## Írók és olvasók problémája. Sorompók.

### Írók és olvasók problémája

Több proc egymással versengve írja és olvassa ugyanazt az adatot. Megengedett az egyidejű olvasás, de ha egy proc írni akar, akkor más procok sem nem írhatnak se nem olvashatnak. (pl, adatbázisok, fájlok, hálózat)
Ha a folyamatos olvasók utánpótlása, az írok éheznek.
Megoldás: Érkezési sorrend betartása $\rightarrow$ csökken a hatékonyság

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