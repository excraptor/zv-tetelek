# 11. Szoftverfejlesztési folyamat és elemei; a folyamat különböző modelljei

## Alapvető elemek

- Szoftverspecifikáció: a szoftver funkcióit és korlátait meg kell határozni
- Szoftvertesztelés és implementáció: a specifikációnak megfelelően a szoftvert elő kell állítani
- Szoftvervalidáció: a szoftvert ellenőrizni kell, hogy tényleg azt fejlesztettük ki, amit az ügyfél kíván
- Szoftverevolúció: a szoftvert úgy alakítani, hogy megfeleljen a későbbi kívánságoknak

## A szoftverfolyamat modelljei

A szoftverfolyamat modellje a szoftverfolyamat absztrakt reprezentációja. Ezek a modellek egy-egy egyedi
perspektívából reprezentál egy szoftverfolyamatot, de nem pontos specifikációja annak. Sokkal inkább hasznos
absztrakciók, amit a szoftverfejlesztési folyamat különböző megközelítési módjainak megértéséhez használunk.

### Vízesés modell

- Specifikáció: rögzítjük a termék követelményeit. Mit tudjon a szoftver, és mit nem.
- Tervezés: szétválasztódnak a szoftver- és hardverkövetelmények. Megtervezzük a rendszer architektúráját.
- Implementáció: a szoftver fejlesztése, egységtesztelése. Az egységtesztelés azt a célt szolgálja, hogy a szoftver minden egyes egysége megfelel-e a specifikációnak.
- Verifikáció: a különálló programegységes és programok integrálása és teljes rendszerként való tesztelése, hogy a rendszer megfelel-e a specifikációnak. A tesztelés után a rendszer átadható az ügyfélnek.
- Karbantartás: a szoftver életciklusának leghosszabb fázisa. A karbantartásba beletartozik olyan hibák javítása is, amelyek nem merültek fel az életciklus korábbi szakaszaiban, illetve a szolgáltatások továbbfejlesztése.

A fázisok eredménye egy vagy több dokumentum, amelyek jóváhagyása megtörtént. A következő fázis nem indulhat, amíg az előző be nem fejeződött.

Probléma: a folyamat korai szakaszaiban állást kell foglalnunk és el kell köteleznünk magunkat, és nehéz az ügyfélhez történő alkalmazkodás. Akkor jó, ha előre ismerjük a követelményeket. Nagyobb rendszerek kisebb folyamatainál használják főleg.

### Evolúciós fejlesztés

Az evolúciós fejlesztés lényege, hogy ki kell fejleszteni egy korai implementációt, azt a felhasználókkal véleményeztetni, és finomítani a felhasználói visszajelzések alapján, amíg megfelelő rendszert el nem élünk. 

Két különböző típusa ismert:

- Feltáró fejlesztés: a folyamat célja az hogy a megrendelővel együtt feltárjuk a követelményeket, és kialakítsuk a véglekges rendszert. A végleges rendszer úgy alakul ki, hogy egyre több, az ügyfél által kért tulajdonságot társítunk a már meglévőkhöz.
- Eldobható prototípus fejlesztése: ekkor az evolúciós fejlesztés célja, hogy minél jobban megértsük az ügyfél követelményeit, és azokra alapozva a legpontosabban fejlesszük le a terméket.

Az evolúciós fejlesztés jobb, mint a vízesés modell, ha a lehető legpontosabban szeretnénk az ügyfél kívánságainak megfelelő szoftvert fejleszteni. Előnye, hogy a specifikáció inkrementálisan fejleszthető.

A vezetőség és a tervezők szempontjából két probléma merülhet fel: 

- A folyamat nem látható. A menedzsereknek rendszeresen leszállítható eredményekre van szükségük, hogy mérhessék a fejlődést.
- A rendszerek sokszor szegényesen struktúráltak. A folyamatos változtatások rontják a szoftver struktúráját.

A várhatóan rövid élettartamú kis vagy közepes rendszerek esetén az evolúciós megközelítési mód a legcélravezetőbb.

