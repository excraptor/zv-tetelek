
# 16. Számítógép perifériák: Mágneses és optikai adattárolás alapelvei, működésük (merevlemez, Audio CD, CD-ROM, CD-R, CD-RW, DVD, Bluray). SCSI, RAID. Nyomtatók, egér, billentyűzet. Telekommunikációs berendezések (modem, ADSL, KábelTV-s internet)

## Számítógép perifériák

A számítógéphez különböző perifériák kapcsolhatók, melyek segítségével a felhasználók kommunikálni tudnak a gazdagéppel. Ezek egy része beviteli, vagy kiviteli eszköz, - amely az adatok bevitelére, vagy kiírására szolgál. A háttértárolók feladata az adatok és programok hosszabb ideig tartó tárolása. Tartalmuk a számítógép kikapcsolása után is megmarad.
A fogalmat általában azokra az eszközökre alkalmazzák, melyek külsőleg csatlakoznak a gazdagéphez, tipikusan egy számítógépes buszon keresztül, mint például az USB.

Csoportosításuk:

- bemeneti perifériák
- kimeneti perifériák

### Mágneses adattárolás alapelvei, működése

**Egy mágneslemez egy vagy több mágnesezhető bevonattal ellátott alumíniumkorongból áll.** 
Egy **indukciós fej** lebeg a lemez felszíne felett egy vékony légpárnán.
Ha **pozitív vagy negatív áram folyik** az indukciós tekercsben, a fej alatt a lemez magnetizálódik, és ahogy a korong forog a fej alatt, így bitsorozatokat lehet felírni
Amikor a fej egy mágnesezett terület felett halad át, akkor pozitív vagy negatív áram indukálódik benne, így a korábban eltárolt biteket vissza lehet olvasni. 

Egy teljes körülfordulás alatt felírt bitsorozat **a sáv**. Minden sáv rögzített méretű tipikusan **512 bájt méretű *szektorokra* van osztva**, melyeket egy fejléc előz meg, lehetővé téve a fej szinkronizálását írás és olvasás előtt. Az adatok után hibajavító kód helyezkedik el (Hamming vagy Reed-Solomon).

Minden lemeznek vannak mozgatható karjai, melyek a forgástengelytől sugárirányban ki-be tudnak mozogni. Minden sugárirányú pozíción egy-egy sáv írható fel. Tehát a sávok forgástengely középpontú koncentrikus körök.

Egy lemezegység több, egymás felett elhelyezett korongból áll. Minden felülethez tartozik egy fej és egy mozgatókar. A karok rögzítve vannak egymáshoz, így a fejek mindig ugyanarra a sugárirányú pozícióra állnak be. Egy adott sugárirányú pozícióhoz tartozó sávok összességét cilindereknek nevezzük. Általában 6-12 korong található egymás felett.

Egy szektor beolvasásához vagy kiírásához először a fejet a megfelelő sugárirányú pozícióba kell állítani, ezt keresésnek (seek) hívják. A fej kívánt sugárirányú pozícióba való beállása után van egy kis szünet, az ún. forgási késleltetés, amíg a keresett szektor a fej alá fordul. A külső sávok hosszabbak, mint a belsők, a lemezek pedig a fejek pozíciójától függetlenül állandó szögsebességgel forognak, ezért ez problémát vet fel. Megoldásképp a cilindereket zónákba osztják, és a külső zónákban több szektort tesznek egy sávba. Minden szektor mérete egyforma. Minden lemezhez tartozik egy lemezvezérlő, egy lapka, amely vezérli a meghajtót.


### Optikai adattárolás alapelvei, működése

Az optikai adattárolók megjelenése kör alakú lemez, amelyek felületén helyezkedik el az adattárolásra alkalmas réteg. A lemezek írása és olvasása a nevükből adódóan optikai eljárással történik. 
Az optikai írás és az olvasás **lézersugárral történik a lemez forgatása közben**. A lemezen történő adatrögzítéskor a lézersugár **apró mélyedéseket hoz létre spirál alakú vonalban**, így tárolva a digitális adatot.

 az adat kiolvasásához ugyanilyen hullámhosszú lézersugár halad végig a mélyedések sorozatán és olvassa vissza a digitális adatot aszerint, hogy a sugár visszatükröződik, vagy szétszóródik a lemez felületéről. 

Az optikai tárolókat több tulajdonságuk is jelentősen megkülönbözteti a mágneses táraktól: az optikai tárolás elméletben sokkal nagyobb adatsűrűséget enged meg, mivel a fény sokkal kisebb területre fókuszálható, mint a mágneses adattárolókban az elemi mágnesezhető részecskék mérete. Továbbá, a megfelelő minőségű és megfelelően kezelt optikai lemezek élettartama évszázadokban mérhető, ezenkívül nem érzékenyek az elektromágneses behatásokra sem.

A felületen elhelyezkedő mélyedéseket üregnek (pit), az üregek közötti érintetlen területeket pedig szintnek (land) hívják.

Az tűnik a legegyszerűbbnek, hogy üreget használjunk a 0, szintet az 1 tárolásához, ennél azonban megbízhatóbb, ha az üreg/szint vagy a szint/üreg átmenetet használjuk az 1-hez, az átmenet hiányát pedig a 0-hoz, ezért ez utóbbi módszert alkalmazzák.

**Merevlemez (HDD)**
- Mágneses adattároló
- Tárolókapacitás: 500 GB – 12 TB
- Írása és olvasási sebesség: függ a forgási sebességtől, ez jellemzően 5400, 7200, 1000 vagy 15000 fordulat/perc, és az adatsűrűségtől (egy adathordozó fizikai felületével arányos tárolókapacitása)

**Audio CD**
- A jel sűrűsége állandó a spirál mentén
- 74 percnyi anyag fér rá (Beethoven IX. szimfóniája kiadható legyen)
- Állandó kerületi sebesség, ehhez szükséges a változó forgási sebesség (120 cm/mp)
- Nincs hibajavítás, mivel nem gond, ha néhány bit elvész az audio anyagból

**CD-ROM**
- Univerzális adathordozó, illetve médialemez. 
- Csak olvasható (véglegesített) adathordozó.
- Népszerűen használták szoftverek és adatok terjesztésére
- Az ilyen típusú lemezeket kereskedelmi forgalomban hozzák létre, és létrehozásuk után nem menthet rájuk adatokat.
- 650 MB tárolható

**CD-R**
- Író berendezéssel rögzíthető az adat (1x)
- Újdonság:
        ◦ Író lézernyaláb
        ◦ Alumínium helyett arany felület
        ◦ Üregek és szintek helyett festékréteg alkalmazása: Kezdetben átlátszó a festékréteg (cianin (zöld) vagy ftalocianin (sárgás))
- 700 MB tárolható

**CD-RW**
- Újraírható optikai lemez
- A CD-RW lemez adatait számos alkalommal törölhetjük és rögzíthetjük.
- Újdonság:
        ◦ Más adattároló réteg:
            ▪ Ezüst, indium, antimon és tellúr ötvözet
            ▪ Kétféle stabil állapot: kristályos és amorf (más fényvisszaverő képesség)
- 3 eltérő energiájú lézer:
            ▪ Legmagasabb energia: megolvad az ötvözet → amorf
            ▪ Közepes energia: megolvad → kristályos állapot
            ▪ Alacsony energia: anyag állapotnak érzékelése, de meg nem változik

**DVD**
- Nagy kapacitású optikai tároló, amely leginkább mozgókép és jó minőségű hang, valamint adat tárolására használatos
- Méreteit tekintve általában akkora, mint a CD, vagyis 120 mm átmérőjű.
- Létezik egyrétegű/kétrétegű illetve egyoldalas/kétoldalas lemez (4,5 GB – 17 GB)
- Nagyobb jelsűrűség, mert
        ◦ Kisebbek az üregek (0,4 μm (CD: 0,8 μm))
        ◦ Szorosabb spirálok
        ◦ Vörös lézert használtak

**Blu-Ray**
- A DVD technológia továbbfejlesztése, a Blu-Ray disc
- Kék lézer használata írásra és olvasásra a vörös helyett
        ◦ Rövidebb hullámhossz, jobban fókuszálható, kisebb mélyedések
- 25 GB (egyoldalas) és 50 GB (kétoldalas) adattárolási képesség


## SCSI, RAID

### SCSI
**Olyan szabányegyüttes, melyet számítógépek és perifériák közötti adatátvitelre terveztek. A SCSI szabványok definiálják a parancsokat, protokollokat, az elektromos és optikai csatolófelületek definícióit.**
#### SCSI meghajtók
Az *ATA* és *SATA* meghajtóknál haladóbb eszközök. Az SCSI nagyobb sebességet biztosít és megbízhatóbb, viszont azoknál sokkal drágábbak ezért nem használják otthoni felhasználásra.

#### SCSI merevlemezek
Az SCSI-lemezek nem különböznek az IDE-lemezektől abban a tekintetben, hogy ezek is **cilinderekre**, **sávokra** és **szektorokra** vannak osztva, de más az interfészük, és sokkal nagyobb az adatátviteli sebességük. Az **5 MHz-estől a 160 MHz-ig nagyon sok változatot kifejlesztettek.**

#### SCSI lánc
Az SCSI kábelre több SCSI eszköz is felfűzhető, ezt nevezik **SCSI láncnak**.
Több verzió létezik, de akár legfeljebb 7 vagy 15 eszköz fűzhető fel. Ezeket a felfűzött meghajtókat egy **SCSI host apdater kezeli**.
A lánc hossza nem haladhatja meg a 1,5-12 métert, mivel lehet külső vagy belső is ez a lánc és fontos, hogy  a jelek ne zavarják egymást.

A SCSI-vezérlők és –perifériák kezdeményező és fogadó üzemmódban működhetnek. Általában a kezdeményezőként működő vezérlő adja ki a parancsokat a fogadóként viselkedő lemezegységeknek és egyéb perifériáknak.

A szabvány megengedi, hogy az összes eszköz egyszerre működjön, így nagyban növelhető a hatékonyság több folyamatot futtató környezetben.

### RAID

A RAID tárolási technológia, mely segítségével az adatok elosztása vagy replikálása több fizikailag független merevlemezen, egy logikai lemez létrehozásával lehetséges. Minden RAID szint alapjában véve vagy az adatbiztonság növelését vagy az adatátviteli sebesség növelését szolgálja.

Azon túl, hogy a RAID szoftverszempontból egyetlen lemeznek látszik, az adatok szét vannak osztva a meghajtók között, lehetővé téve a párhuzamos működést.

A RAID alapötlete a lemezegységek csíkokra (stripes) bontása. Ezek a csíkok azonban nem azonosak a lemez fizikai sávjaival.

**RAID-0 (összefűzés vagy csíkozás)**

Lemezek egyszerű összefűzését jelenti, viszont semmilyen redundanciát nem ad, így nem biztosít hibatűrést, azaz egyetlen meghajtó meghibásodása az egész tömb hibáját okozza. Mind az írási, mind az olvasási műveletek párhuzamosítva történnek, ideális esetben a sebesség az egyes lemezek sebességének összege lesz, így a módszer a RAID szintek közül a legjobb teljesítményt nyújtja (a többi módszernél a redundancia kezelése lassítja a rendszert).

Ahol nem szempont a biztonság vagy kevés merevlemez csatolható fel ott a legjobb.

**RAID-1 (tükrözés)**

A RAID 1 eljárás alapja az adatok tükrözése (disk mirroring), azaz az információk egyidejű tárolása a tömb minden elemén. Az adatok olvasása párhuzamosan történik a diszkekről, felgyorsítván az olvasás sebességét; az írás normál sebességgel, párhuzamosan történik a meghajtókon. Az eljárás igen jó hibavédelmet biztosít, bármely meghajtó meghibásodása esetén folytatódhat a működés.

**RAID-2**

Egyes meghajtókat hibajavító tárolására tartanak fenn. A hibajavító kód lényege, hogy az adatbitekből valamilyen matematikai művelet segítségével redundáns biteket képeznek. A használt eljárástól függően a kapott kód akár több bithiba észlelésére, illetve javítására alkalmas. A védelem ára a megnövekedett adatmennyiség. A módszer esetleges lemezhiba esetén képes annak detektálására, illetve kijavítására 

**RAID-3**

A RAID 3 felépítése hasonlít a RAID 2-re, viszont nem a teljes hibajavító kód, hanem csak egy lemeznyi paritásinformáció tárolódik. 
Egy adott paritáscsík a különböző lemezeken azonos pozícióban elhelyezkedő csíkokból XOR művelet segítségével kapható meg. A rendszerben egy meghajtó kiesése nem okoz problémát, mivel a rajta lévő információ a többi meghajtó (a paritást tároló meghajtót is beleértve) XOR-aként megkapható.

**RAID-4**

A RAID 4 felépítése a RAID 3-mal megegyezik. Az egyetlen különbség, hogy itt nagyméretű csíkokat definiálnak, így egy rekord egy meghajtón helyezkedik el, lehetővé téve egyszerre több (különböző meghajtókon elhelyezkedő) rekord párhuzamos írását, illetve olvasását (multi-user mode). Problémát okoz viszont, hogy a paritás-meghajtó adott csíkját minden egyes íráskor frissíteni kell (plusz egy olvasás és írás), aminek következtében párhuzamos íráskor a paritásmeghajtó a rendszer szűk keresztmetszetévé válik. 

**RAID-5**

A RAID 5 a paritás információt nem egy kitüntetett meghajtón, hanem „körbeforgó paritás” (rotating parity) használatával, egyenletesen az összes meghajtón elosztva tárolja, kiküszöbölvén a paritás-meghajtó jelentette szűk keresztmetszetet. Mind az írási, mind az olvasási műveletek párhuzamosan végezhetőek. Egy meghajtó meghibásodása esetén az adatok sértetlenül visszaolvashatóak, a hibás meghajtó adatait a vezérlő a többi meghajtóról ki tudja számolni.

## Nyomtatók, egér, billentyűzet

### Nyomtatók

**Mátrixnyomtatók**

A nyomtatófejben apró tűk vannak (általában 9 vagy 24 db). A papír előtt egy kifeszített festékszalag mozog, amelyre a tűk ráütnek, és létrehoznak a papíron egy pontot. A kép ezekből a pontokból fog állni. A tűket elektromágneses tér mozgatja, és rugóerő húzza vissza eredeti helyükre. Ezzel az eljárással nem csak karakterek, hanem képek, rajzok is nyomtathatóak. A nyomtatott képek felbontása gyenge, a nyomtató lassú viszont olcsók és nagyon megbízhatók.

**Tintasugaras nyomtató:**

A tintasugaras nyomtatók tintapatronok segítségével tintacseppeket juttatnak a papírlapra. A patronban van egy porlasztó, ez megfelelő méretű tintacseppekre alakítja a tintát, és a papírlapra juttatja azt. A színes tintasugaras nyomtató színes tintapatronokat használ, általában négy alapszín használatával keveri ki a megfelelő árnyalatokat: ciánkék, bíborvörös, sárga és fekete színek használatával. Minden tintasugaras nyomtató porlasztással juttatja a tintacseppeket a papírlapra, de a porlasztás módszere változó. Ez történhet piezoelektromos úton, elektrosztatikusan, vagy gőzbuborékok segítségével.

A **gőzbuborékos nyomtató a következő módon működik:**
A nyomtató cserélhető tintapatronja a papír felett oldalirányban mozog. A nyomtatófejben lévő, tintával töltött kamrácskákhoz szabad szemmel alig látható fúvókák (porlasztók) kapcsolódnak. Azokat a kamrákat, mely a nyomtatandó képrészlet soron következő képpontjához szükségesek, elektromos impulzus melegíti fel, minek következtében a tinta a melegítési helyeken felforr, és a keletkező gőzbuborék egy-egy tintacseppet lő a porlasztókon keresztül a papírlapra. A tintasugaras nyomtatók egy-egy karaktert sokkal több képpontból állítanak össze mint például a mátrixnyomtatók, ezért sokkal szebb képet is adnak annál: megfelelő tintasugaras nyomtatóval igen jó minőségű, színes képek, akár fotók is nyomtathatók.

**Lézernyomtató**
A nyomtató szíve egy fényérzékeny anyaggal bevont forgó henger. Egy-egy lap nyomtatása előtt eletromosan feltöltődik. Ezt követően egy lézer fénye pásztázza végig a hengert hosszában, amelyet egy nyolcszögletű tükörrel irányítanak a hengerre. A fényt modulálják, hogy világos és sötét pontokat kapjanak. Azok a pontok, ahol fény éri a hengert, elveszítik elektromos töltésüket. Miután egy pontokból álló sor elkészült, a henger elfordul és elkezdődhet a következő sor előállítása. Később az első sor eléri a tonerkazettát, amely elektrosztatikusan érzékeny fekete port tartalmaz. A por hozzátapad a még feltöltött pontokhoz, így láthatóvá válik a sor. Tovább fordulva a bevont henger hozzányomódik a papírhoz, átadva a papírnak a festéket. A papír ezután felmelegített görgők között halad el, ezáltal a festék véglegesen hozzátapad a papírhoz.
A lézernyomtatók kiváló minőségű képet készítenek, nagy a rugalmasságuk, sebességük és elfogadható a költség.

### Egér

Az egér egy grafikus felületen való mutató mozgatására szolgáló periféria. Az egéren egy, kettő vagy akár több nyomógomb van, illetve egy görgő is lehet rajta. Belsejében található érzékelő felismeri és továbbítja a számítógép felé az egér mozgását egy sima felületen

**Optikai**
Az optikai egér a mozgásokat egy optikai szenzor segítségével ismerte fel, mely egy fénykibocsátó diódát használt a megvilágításhoz. Az első optikai egereket csak egy speciális fémes egérpadon lehetett használni, melyre kék és szürke vonalak hálója volt felfestve. Miután a számítógépes eszközök egyre olcsóbbak lettek, lehetőség nyílt egy sokkal pontosabb képelemző chip beépítésére is az egérbe, melynek segítségével az egér mozgását már szinte bármilyen felületen érzékelni lehetett, így többé nem volt szükség speciális egérpadra. Ez a fejlesztés megnyitotta a lehetőséget az optikai egerek elterjedése előtt. 
A modern optikai egerek egy reflexszenzor segítségével sorozatos képeket készítenek az egér alatti területről. A képek közötti eltérést egy képelemző chip dolgozza fel, és az eredményt a két tengelyhez viszonyított elmozdulássá alakítja.


**Mechanikus**
Egy golyó két egymáshoz képest 90 fokban elhelyezett tengelyt forgat, melyek továbbítják a mozgását a fényáteresztő résekkel rendelkező korongoknak. Az optocsatolók infravörös LEDjei átvilágítanak a hozzájuk tartozó korongok résein. Bármely korong elfordulásakor a rajta lévő rések átengedik LED fényét, míg a rések közötti fogak nem. Végeredményben az egér elmozdulása fényimpulzusok sorozatává változik, mégpedig annál több fényimpulzus keletkezik, minél nagyobb az egér által megtett út, A fényérzékeny szenzorok érzékelik a fényimpulzusokat és elektromos jelekké alakítják.

### Billentyűzet

A billentyűzet gombjai kábelezés szempontjából egy ún. billentyűzet-mátrixban vannak elhelyezve. Egy meghatározott billentyű lenyomásának vagy felengedésének észlelésekor a belső mikroprocesszor egy, az adott billentyűt egyértelműen azonosító ún. scan-kódot küld a számítógép felé. Ugyanezen billentyű felengedésekor a mikroprocesszor egy másik, felengedési scan-kódot továbbít a billentyűzet-illesztő áramkör felé. Ezáltal részint kiküszöbölhető a több billentyű közel egyidejű lenyomásából adódó jelenség, a karakterek "elvesztése". A megfelelő gomb vagy kombinációk értelmezése és feldolgozása így teljesen a számítógép billentyűzetkezelő rutinjának feladata.

## Telekommunikációs berendezések

### Modem

A modem egy olyan berendezés, ami egy vivőhullám modulációjával a **digitális jelet analóg információvá, illetve a másik oldalon ennek demodulációjával újra digitális információvá alakítja**. Az eljárás célja, hogy a digitális adatot analóg módon átvihetővé tegye.
A moduláció különféle eljárások csoportja, melyek biztosítják, hogy egy tipikusan szinuszos jel - a vivő - képes legyen információ hordozására. A szinuszos jel három fő paraméterét, az **amplitúdóját**, a **fázisát** vagy a **frekvenciáját** **módosíthatja a modulációs eljárás**, azért, hogy a vivő információt hordozhasson. Néhány ok, ami miatt szükséges a közvetítő közegen való átküldést megelőző moduláció:
A modem egy másik modemmel működik párban, ezek az átviteli közeg két végén vannak. Szigorú értelemben véve a két modem két adatátviteli berendezést köt össze, azonban a másik végberendezés tovább csatlakozhat az internet felé.


### ADSL

Az ADSL vagyis az aszimmetrikus digitális előfizetői vonal valójában egy kommunikációs technológia, amely egy csavart rézérpárú telefonkábelen keresztül juttat el adatot A pontból B pontba. A technológia segítségével a hagyományos modemekhez képest gyorsabb digitális adatátvitel érhető el, ezért igazi áttörés volt megjelenése az internetszolgáltatás piacán.
Az ADSL jellemzője, hogy a letöltési és a feltöltési sávszélesség aránya nem egyenlő (vagyis a vonal aszimmetrikus), amely az otthoni felhasználóknak kedvezve a letöltés sebességét helyezi előnybe a feltöltéssel szemben.
Mind technikai, mind üzleti okai vannak az ADSL gyors elterjedésének. A technikai előnyt az adja, hogy a zajelnyomási lehetőségeket kihasználva lehetővé teszi nagyobb távolságon is a gyors adatátvitelt a felhasználó lakása és a DSLAM eszköz között (amely a telefonközpontokban helyezkedik el).

### KábelTV-s internet

A kábelszolgáltatók minden városban fő telephellyel rendelkeznek, valamint rengeteg, elektronikával zsúfolt dobozzal szerte a működési területükön, amelyeket fejállomásoknak neveznek.
A fejállomások nagy sávszélességű kábelekkel vagy üvegkábelekkel kapcsolódnak a fő telephelyhez. Minden fejállomásról egy vagy több kábel indul el, otthonok és irodák százain halad keresztül. Minden előfizető a rajta keresztülhaladó kábelhez csatlakozik. Így a felhasználók osztoznak egy fejállomáshoz vezető kábelen, ezért a kiszolgálás sebessége attól függ, hogy pillanatnyilag hányan használják az adott vezetéket. A kábelek sávszélessége 750 MHz.