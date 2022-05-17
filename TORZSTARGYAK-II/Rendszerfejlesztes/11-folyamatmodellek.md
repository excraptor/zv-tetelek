
# 11. Szoftverfejlesztési folyamat és elemei; a folyamat különböző modelljei

**A szoftverfolyamat:** Tevékenységek és kapcsolódó eredmények, amely során elkészítjük a szoftvert.
## Alapvető elemek

- **Szoftverspecifikáció (mit):** 
	- a szoftver funkcióit és korlátait meg kell határozni
	- *Legkisebb a változás költséges*
	- Eredménye a **követelményspecifikáció**
- **Szoftvertesztelés és implementáció (hogyan):** 
	- a specifikációnak megfelelően a szoftvert elő kell állítani
	- Alrendszerek meghatározása, komponens tervezés stb.
- **Szoftvervalidáció (ellenőrzés):** 
	- a szoftvert ellenőrizni kell, hogy tényleg azt fejlesztettük ki, amit az ügyfél kíván.
	- **Verifikáció:** Rendszer megfelel e a specifikációnak
	- **Validáció:** Megfelel e a megrendelő elvárásainak
- **Szoftverevolúció (változás):** a szoftvert úgy alakítani, hogy megfeleljen a későbbi kívánságoknak

## A szoftverfolyamat modelljei

A szoftverfolyamat modellje a szoftverfolyamat absztrakt reprezentációja. Ezek a modellek egy-egy egyedi
perspektívából reprezentál egy szoftverfolyamatot, de nem pontos specifikációja annak. Sokkal inkább hasznos
absztrakciók, amit a szoftverfejlesztési folyamat különböző megközelítési módjainak megértéséhez használunk.

### Vízesés modell

- **Specifikáció:** rögzítjük a termék követelményeit. Mit tudjon a szoftver, és mit nem.
- **Tervezés:** szétválasztódnak a szoftver- és hardverkövetelmények. Megtervezzük a rendszer architektúráját.
- **Implementáció:** a szoftver fejlesztése, egységtesztelése. Az egységtesztelés azt a célt szolgálja, hogy a szoftver minden egyes egysége megfelel-e a specifikációnak.
- **Verifikáció:** a különálló programegységes és programok integrálása és teljes rendszerként való tesztelése, hogy a rendszer megfelel-e a specifikációnak. A tesztelés után a rendszer átadható az ügyfélnek.
- **Karbantartás:** a szoftver életciklusának leghosszabb fázisa. A karbantartásba beletartozik olyan hibák javítása is, amelyek nem merültek fel az életciklus korábbi szakaszaiban, illetve a szolgáltatások továbbfejlesztése.

A fázisok eredménye egy vagy több dokumentum, amelyek jóváhagyása megtörtént. A következő fázis nem indulhat, amíg az előző be nem fejeződött.

**Probléma:** a folyamat korai szakaszaiban állást kell foglalnunk és el kell köteleznünk magunkat, és nehéz az ügyfélhez történő alkalmazkodás. Akkor jó, ha előre ismerjük a követelményeket. Nagyobb rendszerek kisebb folyamatainál használják főleg.

### Evolúciós fejlesztés

Az evolúciós fejlesztés lényege, hogy ki kell fejleszteni egy korai implementációt, azt a felhasználókkal véleményeztetni, és finomítani a felhasználói visszajelzések alapján, amíg megfelelő rendszert el nem élünk. 

Két különböző típusa ismert:

- **Feltáró fejlesztés:** a folyamat célja az hogy a megrendelővel együtt feltárjuk a követelményeket, és kialakítsuk a véglekges rendszert. A végleges rendszer úgy alakul ki, hogy egyre több, az ügyfél által kért tulajdonságot társítunk a már meglévőkhöz.
- **Eldobható prototípus fejlesztése:** ekkor az evolúciós fejlesztés célja, hogy minél jobban megértsük az ügyfél követelményeit, és azokra alapozva a legpontosabban fejlesszük le a terméket.

Az evolúciós fejlesztés jobb, mint a vízesés modell, ha a lehető legpontosabban szeretnénk az ügyfél kívánságainak megfelelő szoftvert fejleszteni. Előnye, hogy a specifikáció inkrementálisan fejleszthető.

A vezetőség és a tervezők szempontjából két probléma merülhet fel: 

- A folyamat nem látható. A menedzsereknek rendszeresen leszállítható eredményekre van szükségük, hogy mérhessék a fejlődést.
- A rendszerek sokszor szegényesen struktúráltak. A folyamatos változtatások rontják a szoftver struktúráját.

A várhatóan rövid élettartamú kis vagy közepes rendszerek esetén az evolúciós megközelítési mód a legcélravezetőbb.

### Iterációs, inkrementális modell

- Folyamat iterációja elkerülhetetlen
- ha a követelmények változnak, akkor a folyamat bizonyos részeit is változtatni kell
- ennél a modellnél minimális a specifikáció, fejlesztésben sok iteráció van, és menet közben alakul ki a végleges specifikáció
- Inkrementalitás: részfunkciókkal már működő rendszert fejlesztünk, amit minden iterációban (inkrementálisan) javítunk
- Nagy körvonalakban specifikáljuk a rendszert
    - „Inkremensek” meghatározása
    - Funkcionalitásokhoz prioritásokat rendelünk
    - Magasabbakat előbb kell biztosítani
- Architektúrát meg kell határozni
- További inkremensek pontos specifikálása menet közben történik
- Egyes inkremensek kifejlesztése történhet akár különböző folyamatokkal is - Vízesés vagy evolúciós, amelyik jobb
- Az elkészült inkremenseket akár szolgálatba is lehet állítani
- Ha határidő csúszás van kilátásban a teljes projekt nem lesz kudarcra ítélve, esetleg csak egyes inkremensek
- Megfelelő méretű inkremensek meghatározása nem triviális feladat
    - Ha túl kicsi: nem működőképes
    - Ha túl nagy: elveszítjük a modell lényegét

Bizonyos esetekben számos alapvető funkcionalitást kell megvalósítani. Egész addig
nincs működő inkremens

### eXtreme Programming (XP)

- Szélsőséges inkrementális modell
- Nagyon kis funkcionalitású inkremensek
- Megrendelő intenzív részvétele fontos
- Programozás csoportos tevékenység - többen ülnek a képernyő előtt
- Sok támadója van


### RAD (Rapid Application Development)

- Extrém rövid életciklus
	- Működő rendszer 60-90 nap alatt
- Vízesés modell „nagysebességű” adaptálása
	- Párhuzamos fejlesztés
	- Komponens alapú fejlesztés
- Fázisai:
    - *Üzleti modellezés*
        -  Milyen információk áramlanak funkciók között
    - *Adatmodellezés*
        -  Finomítás adatszerkezetekre
    - *Adatfolyam processzus*
        -  Adatmodell megvalósítása
    - *Alkalmazás generálás*
        -  4GT alkalmazása, automatikus generálás, komponensek
    - *Tesztelés*
        -  Csak komponens tesztelés
        - 
Problémák:
- Nagy emberi erőforrásigény
- Fejlesztők és megrendelők intenzív együttműködése szükséges
- Nem minden típusú fejlesztésnél alkalmazható

### Spirális modell

- Olyan evolúciós modell, amely kombinálja a prototípus modellt a vízesés modellel
- Inkrementális modellhez hasonló, csak általánosabb megfogalmazásban
- Nincsenek rögzített fázisok
- Más modelleket ölelhet fel
    - Prototípuskészítés pontatlan követelmények esetén
    - Vízesés modell egy későbbi körben
    - Kritikus részek esetén formális módszerek
- A spirál körei a folyamat egy-egy fázisát reprezentálják
- Minden körben a kimenet egy „release” (modell vagy szoftver)
- Körök céljai pl.:
    - Megvalósíthatóság (elvi prototípusok)
    - Követelmények meghatározása (prototípusok)
    - Tervezés (modellek és inkremensek)
    - Stb. (javítás, karbantartás, stb.)
- A körök 3-6 darab szektorokra oszthatók


### WINWIN spirális modell

- WINWIN = mindenki nyer
- Megrendelő és fejlesztő is
- Sok tárgyalás kell a két fél között
- WINWIN modell számos tárgyalási szempontot visz bele a spirális modellbe
    - Egyes (al)rendszerek kulcsszereplői, érdekeltek
    - Az érdekeltek nyerő feltételei
    - Tárgyalás, kompromisszumok
