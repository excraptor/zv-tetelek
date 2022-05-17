
# 10. A programozási nyelvek csoportosítása (paradigmák), az egyes csoportokba tartozó nyelvek legfontosabb tulajdonságai

## Paradigmák

A programozási paradigma egy osztályozási forma, amely a programozási nyelvek jellemzőin alapul.

## Imperatív
Utasításokat használ, hogy egy program állapotát megváltoztassa. 

## Procedurális
A feladatokat felbonthatjuk elvégzendő feladatok szerint, tehát *alprogramokat* (függvény, eljárás) hozunk létre. Ezek között paraméterátadással, függvény visszatérési értékkel kommunikálnak.
Pl: C, C++,...

### Objektumorientált paradigma

Az objektum orientál paradigma az objektumok fogalmán alapuló programozási paradigma. Az objektumok **egységbe foglalják az adatokat** és a hozzájuk tartozó **műveleteket**. A program egymással kommunikáló objektumok összességéből áll melyek használják egymás műveleteit és adatait.
Öröklödés osztályok között, egyszeres vagy többszörös öröklödéssel. Lehetséges polimorfizmus és absztrakt osztályok létrehozására.

#### Smalltalk

GNU Smalltalk interpreter
Beolvas minden karaktert az első **! –ig**. A „!” jellel jelezzük, hogy végre szeretnénk hajtani az addig beírt kifejezéseket. Több kifejezés futtatása esetén itt is – mint sok más nyelven – jeleznünk kell azt, hogy hol fejeződik be egy kifejezés erre való a **„pont” (.)**
 
#### Precedencia
Ha nem zárójelezünk – mindig balról jobbra történik, így a 2+3\*10 értéke 50 lesz, használjunk zárójelet: 2+(3\*10).
Objektumok, üzenetek
A Smalltalk nyelv egy objektumorientált nyelv **MINDENT** objektumnak tekintünk. 
A programozás során üzeneteket küldünk az egyes objektumoknak. Egy objektumnak háromféle üzenetet küldhetünk:
- **Unáris:** szintaxis: ’Hello’ printNl ! 
- **Bináris:** szintaxis: 3+5 
- **Kulcsszavas:** szintaxis: tomb at:1 put: 10
**Objektumok összehasonlítása:** két objektum egyenlő, ha ugyanazt az objektumot reprezentálják és azonos, ha értékük megegyezik és egyazon objektumok.
 
#### Objektumok másolása

- **deepCopy (unáris üzenet):** Teljes másolat készítése objektumról.
- **shallowCopy (unáris üzenet):** Felszíni másolat
- **copy (unáris üzenet):** Osztályonként változó lehet, az Object osztályban a shallowCopy-t jelenti.

#### Metaosztály

Mint korában említettük, a Smalltalkban mindent objektumnak tekintünk. Még az osztályok is objektumok. De ha az osztály objektum, akkor az is - *mint minden más objektum* - valamilyen osztályhoz kell tartozzon. Másképp fogalmazva minden osztály (pontosan) egy másik osztály példánya. Ezen "másik" osztályt metaosztálynak hívjuk

#### Object osztály

Az Object osztály minden osztály közös **őse**, tehát minden objektum az Object osztály egy példánya. Ezért minden, az Object osztálynak rendelkezésre álló művelettel minden más objektum is rendelkezik.
- **class** – unáris: visszatérése az objektum osztálya
- **isMemberOf** – kulcsszavas: visszatérése logikai érték. Ha a címzett objektum példánya ezen osztálynak, akkor "true" a visszatérési érték, egyébként "false"
    - 'Hello' isMemberOf: String ! → true

#### Változók

- Lokális változók:
    - |x y z| - deklarálása (2 pipeline között)
    - x := 2. (egyszeres értékadás)
    - x := y := z := 2. (többszörös értékadás)
- Globális változók: Smalltalk at: #valtozonev put: érték !

#### Blokkok

Más programozási nyelveken megismert programblokkok szerepével egyezik meg. Vannak paraméteres és nem paraméteres blokkok. Paraméteres blokkok rendelkeznek lokális változókkal, melyeknek a blokk kiértékelésekor adunk értéket. A változók élettartama és láthatósága korlátozódik az adott blokkra.
- [:i | i printNl ] value: 5
- [’Hello’ print . ’world’ printNl] value.

#### Vezérlési szerkezetek

- **Feltételes vezérlés:**	valtozo > 10 ifTrue: [‘x erteke nagyobb 10-nel’ printNl]
                   			        ifFalse: [‘x erteke nem nagyobb 10-nel’ printNl]
- **Ismétléses vezérlés:**	[a<10] whileTrue: [a printNl . a:=a+1]
- **For ciklus:**		1 to: 10 do: [:i | i printNl]

**Kollekciók**
- **Set:** ismétlés nélküli rendezetlen halmaz - new, add()
- **Bag:** olyan Set, amiben megengedjük az ismétlődést - new, add()
- **Dictionary:** egy asszociatív tömb (egy olyan tömb, amit nem csak számokkal, hanem (itt) tetszőleges objektummal is indexelhetünk)

**Tömb**
- tömb := Array new: 10
- tömb at: 1
- tömb at: 1 put: obj
A collect
- kollekció elemein lépked végig, mely minden egyes elemére végrehajtja az üzenet argumentumblokkjában található utasításokat
- |tomb| tomb := #(10 3 43 29) collect: [:tombelem | tombelem*2]
Osztályok
  
- példányváltozók: minden objektum rendelkezik vele
- osztályváltozó: kb. statikus globális változó

#### Metódusok definiálása osztályokhoz
 
pl.:
 

Beolvasás	 x := stdin nextLine.S
Integer üzenetek
 

## Dekleratív programozás
Deklaráljuk a program elvárt működését, nem akarojuk explicit meghatározni annak mikéntjét.

### Funkcionális programozás
- Értékek, kifejezések és függvények vannak
- A program maga egy függvény
- Ciklus helyett **rekurzió**
- A funkcionális programnyelvek a programozási feladatot egy függvény kiértékelésének tekintik.
- A két fő eleme az **érték** és a **függvény**, nevét is függvények kitüntetett szerepének köszönheti.
- **Egy más megfogalmazás szerint, a funkcionális programozás során a programozó inkább azt specifikálja programban, mit kell kiszámítani, nem azt, hogy hogyan, milyen lépésekben.**
- Függvények hívásából és kiértékelésből áll a program. Nincsenek állapotok, mellékhatások (nem számít, mikor, csak az melyik függvényt hívjuk).

#### Haskell

Egy funkcionális programozási nyelven írt programban nem a kifejezések egymásutánján van a hangsúly. A **program egy függvényhívással hajtódik végre.** Egy funkcionális program típus- , osztály-, és függvénydeklarációk, illetve definíciók sorozatából és egy kezdeti kifejezés kiértékeléséből áll. A kiértékelést úgy képzeljük el, mint a kezdeti kifejezésben szereplő függvények behelyettesítését. Tehát egy program végrehajtása nem más, mint a kezdeti kifejezésből kiinduló redukciós lépések sorozata. Egy kifejezés normál formájú, ha már tovább nem redukálható (nem átírható) állapotban van. **Egy redukálható kifejezést redexnek hívunk.**

**Kiértékelési módok**

A Haskell nyelv a **lusta kiértékelési stratégiát használja.**
A lusta kiértékelés során mindig a legkülső redex kerül helyettesítésre, az argumentumokat csak szükség esetén értékeli ki. Ez a módszer mindig megtalálja a kezdeti kifejezés normál formáját. A mohó kiértékelés az argumentumok kiértékelésével kezdődik, csak ezután hajtja végre a függvény alkalmazásának megfelelő redukciós lépést. 
Futtatás
Elindítjuk a Haskell interpretert (hugs) és betöltjük az általunk megírt definíciós forrásállományt. Betöltés után rendelkezésre áll az összes általunk megírt függvény, melyek közül bármelyiket meghívhatjuk a függvény nevének beírásával (a megfelelő paraméterezéssel). Amennyiben módosítjuk a definíciós állományt, újra kell tölteni azt.
 
Atomi típusok: Int, Float, Bool
Függvények definiálása
   
A visszatérési értéket a kiértékelése határozza meg, ami lehet egy konstans érték vagy akár egy rekurzív kifejezés is

Esetvizsgálatok
 
Függvény paramétere függvény
 
Lokális definíciók függvénydefiníciókban
 
Típusok létrehozása

Példák
 
### Logikai programozás

A problémakörrel kapcsolatos tényeket logikai képletek formájában fejezik ki, és a programokat következtetési szabályok alkalmazásával hajtják végre, amíg nem találnak választ a problémára, vagy a képletek halmaza nem következetes.

#### Prolog

A logikai programok egy modellre vonatkoztatott állítások halmaza, melyek a modell tulajdonságait és azok között fellépő kapcsolatokat (relációit) írják le. Egy adott relációt meghatározó állítások részhalmazát predikátumnak nevezzük. A predikátumokat alkotó állítások tények vagy szabályok lehetnek. A tényeket és szabályokat (és majd a Prolognak feltett kérdéseket is) ponttal zárjuk le. Tekintsük a következő példát, mely egy család tagjai között fellépő kapcsolatot írják le.
 
A szulo predikátum argumentumait szándékosan írtuk kis betűkkel. A kis betűkkel írtakat a Prolog konstansként kezeli. (ka, katalin, szilvia, stb…) Minden nyomtatott nagybetűt vagy nagy kezdőbetűvel kezdődőket változónak tekinti. (X, Y, Szilvia, Magdolna, stb…)

Egy prolog program csak az **adatokat** és az **összefüggéseket** tartalmazza, majd **kérdések hatására** a *programvégrehajtás* beépített **következtető-rendszer** végzi.


#### Futtatás

- kiterjesztés **.pl**
- A Prolog egy terminálablakba beírt „sicstus” paranccsal indítható. Egy Prolog állományt a következőképpen „tölthetjük be”: (feltéve, hogy az aktuális könyvtárban létezik egy prolog.pl állomány)

##### A Prolog program felépítése

 - Prolog érték: **term**
	- Egyszerű term: alma, 1000,...
	- Összetett termek
	    - **Lista:** nagyon hasonlít a Haskell-ben megismert listára. Itt sincsenek indexelve az elemek, rekurzióval fogjuk bejárni a listát. Példa listára: [1,2,3,4,5].
Kiértékelés
Kifejezések kiértékelésére a beépített, **infix is operátort**
- Relációk megadása:
	- Tények
	- Következtetés szabályok
- Kérdésfeltevés interaktív módon
	- Eldöntendő kérdés
	- Általános kérdés

**Tények:**
	Tények fejezik ki, hogy a megadott objetumok között fennáll bizonyos reláció. ```barát(john, mary).```
Ezek egy adatbázis definiálnak.

**Kérdések:**
Eldöntendő kérdések ugyanúgy néznek ki, mint a tények csak más a szövegkörnyezet.
```?- barát(john, mary).```

**Következtető rendszer:**
Prolog **backtracking** keresést alkalmaz a válaszok megtalálásra.
Termek


 
   
## Párhuzamos programozás

### Occam
Imperatív, folyamatok saját memóriával rendelkeznek, üzenetküldéssel kommunikálnak.
Occam program részei:
	- Változók
	- Folyamatok
	- Csatornák

**Csatornák:**
	A csatorna két folyamat közti **adatátvitelre** szolgál
	- Egyirányú
	- Küldős és fogadó is legfeljebb egy lehet
	- biztonságos
	- **Szinkron:** A küldő és fogadó bevárják egymást, megtörténik az adatátvitel, majd a küldő és fogadó folyatótdik.

**Folyamatok:**
	Életciklus:
		- Elindul
		- Csinál valamit
		- Befejeződik
Befejezésnél **holtpontba** kerülhet, erre odakell figyelni.
**Elemi folyamatok:**
	- Üres utasitás - **SKIP**
	- Beépített holtpont - **STOP**
	- Értékadás - v:=e
	- Input - c **?** v
	- Output - c **!** e


Az Occam egy párhuzamos programozási nyelv. Ezen paradigma szerint az egyes folyamatok párhuzamosan futnak. Ez több processzoros gépek esetén valós párhuzamosságot jelent (egy processzor egy folyamatot dolgoz fel), de egy processzor esetén ez nyilván nem valósulhat meg, az egyes folyamatok „időszeleteket” kapnak, az Occam a párhuzamosságot időosztással szimulálja. Az egyes folyamatok közötti kommunikáció csatornákon keresztül valósul meg. A P1 és P2 folyamatok a C csatornán keresztül kommunikálnak:
 
A folyamatok közötti kommunikációt mindig csatornákkal valósítjuk meg. A fenti példában a P1 folyamat a C csatornán keresztül valamilyen adatot küld a P2 folyamatnak. Ez a következőképpen valósul meg: ha egy folyamat elérkezik arra a pontra, ahol értéket küld [fogad], várakozik a másik folyamatra, amíg az is el nem ér a fogad [küld] pontra. Amikor mindketten készen állnak az adatcserére (azaz mindkét folyamatban a küldés [fogadás] pontra került a vezérlés) létrejön az adatcsere, majd mindkettő folytatja a futását.

#### Fordítás

- KroC, csak Linux-hoz
- kroc -d pelda.occ
Fontos tudnivalók a nyelvről
- Minden, a nyelvben lefoglalt kulcsszót nagy betűvel kell írni (SEQ, PAR, PROC, stb...) 
- A blokkstruktúrát indentációval jelöljük (két szóközzel beljebb kezdjük) 
- Minden egyes kifejezés új sorban kezdődik (esetlegesen két szóközzel beljebb) 
- Egy Occam program a következőképpen épül fel: 
<deklarációk>
<folyamat> 
- Például: 
 
#### Elemi folyamatok
 
A fenti példában, küldés esetében egy kifejezést (k + 5) küldünk a C csatornára, fogadás esetén pedig a C csatornáról várunk egy értéket, amely az x változóban kerül.
A SKIP folyamat a legegyszerűbb elemi folyamat, „semmit nem csinál”. Haszontalannak tűnhet, de összetettebb programok esetében (például még nem kifejlesztett programrészek esetében) hasznos lehet. Párhuzamos folyamatok esetében fontos, hogy minden folyamat termináljon, ellenkező esetben az egész, folyamatokból álló „rendszer” leáll.
A STOP szintén „nem csinál semmit”, de ez sosem terminál – ellentétben a SKIP-el. Egy folyamatban a STOP (feltéve hogy a vezérlés odakerül), annak holtpontba jutását eredményezi. Szintén haszontalannak tűnhet, de ezzel egy folyamatot leállíthatunk más folyamatok működésének befolyásolása nélkül, ami hibakeresésnél hasznos lehet.
Azt mondjuk, hogy egy folyamat holtpont állapotba került, ha az már nem képes további működésre (vezérlése leáll), és ez a leállás nem a folyamat helyes lefutásának eredménye. Párhuzamos folyamatok közül akár egy folyamat holtpont állapotba kerülése az egész program holtpont állapotba kerülését eredményezi, hiszen az összes többi folyamat várja a holtpontban levő folyamat terminálását, ami sosem fog bekövetkezni.
Blokk struktúra	2 szóközönként beljebb kell kezdeni
#### Precedencia

A kifejezésekben, operátorok között precedenciát nem határozunk meg, így MINDIG zárójelezést kell használni a precedencia meghatározásához

#### Adattípusok
 
 
Csatorna	 
SEQ	  
PAR
 
Az egész PAR blokk akkor terminál, ha a benne „elindított” folyamatok mindegyike terminál
PROC
A PROC egy előre definiált, névvel ellátott folyamat. Tekinthetünk úgy rá, mintha egy eljárást definiálnánk
   
ALT
 
Ha egy őr engedélyezetté válik, akkor a benne megadott változó felveszi a csatornáról érkező adat értékét és „elindítja” a hozzá tartozó folyamatot
    Az x változó értéke attól függ, hogy c1-re vagy c2-re érkezik előbb adat.
Mivel a program írásakor nem tudhatjuk, hogy melyik csatornáról fog adat érkezni, ezért az ALT-ot tartalmazó programok nemdeterminisztikusak
Függvény
 
Vezérlési szerkezetek
- Feltételes vezérlés
   		Holtpont elkerülése  
- Ismétléses vezérlés	
 
- For ciklus		