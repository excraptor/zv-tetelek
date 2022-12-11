
# 15. Neumann-elvű gép egységei. CPU, adatút, utasítás-végrehajtás, utasítás- és processzorszintű párhuzamosság. Korszerű számítógépek tervezési elvei. Példák RISC (UltraSPARC) és CISC (Pentium 4) architektúrákra, jellemzőik

Számítógép architektúra: A hardver egy általános absztrakciója: a hardver struktúráját és viselkedését jelenti más rendszerek egyedi, sajátos tulajdonságaitól eltekintve

## Neumann elvű gép

1. **Teljesen elektronikus működés**
2. **Kettes számrendszer** használata
3. **Belső memória használata**
4. **Tárol program elve**: A számításokhoz szükséges adatokat és programutasításokat a gép azonos módon, egyaránt a **belső memóriában** tárolja.
5. **Soros utasítás-végrehajtás**: Az utasítások végrehajtása időben egymás után történjen.
6. **Univerzális felhasználhatóság**, Turing-gép (programozhatóság, különböző feladatoakt programokkal legyenek megoldva)
7. **Szerkezet**: öt funkcionális egység
	- Aritmetikai egység
	- Központi vezérlőegység
	- Memóriák
	- Bemeneti és kimeneti egységek. 

### Neumann-elvű gép egységei

1. **központi memória:** a program kódját és adatait tárolja számokként
	- RAM, ROM
2. **központi feldolgozóegység (CPU):** a központi memóriában tárolt program utasításait beolvassa és végrehajtja
	- *ALU (Arithmetic logic unit)* 
	- *CU (vezérlőegység)*
	- Regiszterek
3. **beviteli/kiviteli eszközök:** kapcsolatot teremt a felhasználóval, adatot tárol a háttértáron, nyomtat, stb.
	- **Háttértárak:** Merevlemez, SSD stb.
	- Billentyűzet, egér stb.
4. **Busz és sínrendszerek:**
	- **külső sín:** A számítógép egyes elemei között biztosít kapcsolatot. Pl. perifériák, csatolókártyák
	- **belső sín:** CPU részegységei közötti kommunikációt hozza létre (vezérlőegység-ALU-regiszterek)
	
## CPU, adatút, utasítás-végrehajtás, utasítás- és processzorszintű párhuzamosság

### CPU

A CPU feladata a központi memóriában tárolt program utasításainak beolvasása és végrehajtása
**3 fő egysége:**
- **vezérlőegység (CU):**
    - Utasítások beolvasása a memóriából
	    - Értelmezi, végrehajtja, kiszámítja a következő utasítás címét.
    - az ALU és regiszterek vezérlése
    - Szervezi ütemezi a processzor munkáját
- **aritmetika-logikai egység (ALU):**
    - Egy tipikus Neumann-féle CPU belső szerkezetének részében az ALU végzi az összeadást, a kivonást és más egyszerű műveleteket az inputjain, így adva át az eredményt az output regiszternek, azaz a kimeneten ez fog megjelenni.
    - az utasítások végrehajtásához szükséges aritmetikai és logikai műveleteket végzi el
        - Aritmetikai operátorok: +, -, *, / (alapműveletek) 
        - Logikai operátorok: NOT, AND, OR, NAND, NOR, XOR, NXOR (EQ)
- **regiszterek:** 
    - kisméretű, gyors memóriarekeszek, amelyek részeredményeket és vezérlőinformációkat tárolnak
    - A regiszterek a számítógépek központi feldolgozó egységeinek, illetve mikroprocesszorainak gyorsan írható-olvasható, ideiglenes tartalmú, és általában egyszerre csak 1 gépi szó feldolgozására alkalmas tárolóegységei
    - Itt találhatóak különféle fontos számlálók és jelzők. Ilyen pl:
	    - **Utasításszámláló (PC/IP)**, ami mindig a következő utasitás címére mutat
	    - **Utasításregiszer(IR)**, ami a memóriából kiolvasott utasíátst tárolja.
	    - **Veremmutató(SP)**
	    - **Flagregiszter**, amely a processzor működése közben létrejött állapotok jelzőit tárolja.

### Adatút
- Az adatút az adatok áramlásának útja, alapfeladata, hogy kiválasszon egy vagy két regisztert, az ALU-val műveletet végeztessen el rajtuk (összeadás, kivonás...), az eredményt pedig valamelyik regiszterben tárolja. Egyes gépeken az adatút működését mikroprogram vezérli, másutt a vezérlés közvetlenül a hardver feladata.
- Folyamata:
    - A regiszter készletből feltöltődik az ALU két bemenő regisztere (A és B)
    - Az eredmény az ALU kimenő regiszterébe kerül
    - Az ALU kimenő regiszteréből a kijelölt regiszterbe kerül az eredmény
- Két operandusnak az ALU-n történő átfutásából és az eredmény regiszterbe tárolásából álló folyamatot adatútciklusnak nevezzük.


### Utasítás-végrehajtás

A mikroprocesszor 1-1 utasítása úgynevezett gépi ciklusok egymásutániságából áll, vagyis 1 utasítás egy vagy több gépi ciklusból tevődik össze.

A CPU minden utasítást apró lépések sorozataként hajt végre. 
Ezek a lépések a következők:

    1. A soron következő utasítás beolvasása a memóriából az utasításregiszterbe.
    2. Az utasításszámláló beállítása a következő utasítás címére.
    3. A beolvasott utasítás típusának meghatározása.
    4. Ha az utasítás memóriabeli szót használ, a szó helyének megállapítása.
    5. Ha szükséges, a szó beolvasása a CPU egy regiszterébe.
    6. Az utasítás végrehajtása.
    7. Vissza az 1. pontra, a következő utasítás végrehajtásának megkezdése.

Ezt a lépéssorozatot gyakran nevezik betöltő-dekódoló-végrehajtó ciklusnak, és központi szerepet tölt be minden számítógép működésében.

Nagy probléma a számítógépeknél, hogy a memória olvasása lassú, ezért az utasítás és az adatok beolvasása közben a CPU több része kihasználatlan. A gyorsítás egyik módja a lapkák gyorsítása az órajel frekvenciájának növelésével, de ez korlátozott. Emiatt a legtöbb tervező a párhuzamosság kiaknázásában lát lehetőséget.

A párhuzamosság két féleképpen lehet jelen: utasításszintű párhuzamosság vagy processzorszintű párhuzamosság formájában.

### Utasításszintű párhuzamosság

Az utasítások végrehajtásának gyorsítása érdekében előre be lehet olvasni az utasításokat, hogy azok rendelkezésre álljanak, amikor szükség van rájuk. Ezeket az utasításokat egy előolvasási puffer (prefetch buffer) elnevezésű regiszterkészlet tárolja. Ilyen módon a soron következő utasítást általában az előolvasási pufferből lehet venni ahelyett, hogy egy memóriaolvasás befejeződésére kellene várni.

**Csővezeték:**
Lényegében az előolvasás az utasítás végrehajtását két részre osztja:  **beolvasás** és **tulajdonképpeni végrehajtás**. 

A csővezeték ezt a stratégiát viszi sokkal tovább. Az utasítás végrehajtását kettő helyett több részre osztja, minden részt külön hardverelem kezel, amelyek mind egyszerre működhetnek.

A csővezeték lehetővé teszi, hogy kompromisszumot kössünk késleltetés (mennyi ideig tart egy utasítás végrehajtása) és áteresztőképesség (hány MIPS a processzor sebessége) között.
    
**Párhuzamos csővezeték:**
Az előolvasó egység két utasítást olvas be egyszerre, majd ezeket az egyik, illetve a másik csővezetékre teszi. 
A **csővezetékeknek saját ALU-juk van**, így párhuzamosan tudnak működni, feltéve, hogy a két utasítás nem használja ugyanazt az erőforrást, és egyik sem használja fel a másik eredményét. Ugyanúgy, mint egyetlen csővezeték esetén, a feltételek betartását vagy a fordítóprogramnak kell garantálnia, vagy a konfliktusokat egy kiegészítő hardvernek kell a végrehajtás során felismernie és kiküszöbölnie.

**Szuperskaláris architektúra:**
Itt **egy csővezetéket** használnak, **de több funkcionális egységgel**. 
Ezek olyan processzorok, amelyek több – gyakran négy vagy hat – utasítás végrehajtását kezdik el egyetlen órajel alatt.
 
 Természetesen egy szuperskaláris CPU-nak több funkcionális egységének kell lennie, amelyek kezelik mindezeket az utasításokat. Az utasítások megkezdését sokkal nagyobb ütemben végzik, mint amilyen ütemben azokat végre lehet hajtani, így a terhelés megoszlik a funkcionális egységek között. A szuperskaláris processzor elvében implicit módon benne van az a feltételezés, hogy a megfelelő fázis lényegesen gyorsabban tudja előkészíteni az utasításokat, mint ahogy a rákövetkező fázis képes azokat végrehajtani. Ez a fázis funkcionális egységeinek többsége egy órajelnél jóval több időt igényel feladata elvégzéséhez – a memóriához fordulók vagy a lebegőpontos műveleteket végzők biztosan. Akár több ALU-t is tartalmazhat.


### Processzorszintű párhuzamosság

**Tömb processzorok:**

Egy tömbprocesszor nagyszámú egyforma processzorból áll, ugyanazon műveleteket egyszerre végzik különböző adathalmazokon. A feladatok szabályossága és szerkezete különösen megfelelővé teszi ezeket párhuzamos feldolgozásra. Olyan utasításokat hajthatnak végre, mint amilyen például két vektor elemeinek páronkénti összeadása.

**Multiprocesszorok:**

Ezekben több teljes CPU van, amelyek egy közös memóriát használnak. Amikor két vagy több CPU rendelkezik azzal a képességgel, hogy szorosan együttműködjenek, akkor azokat szorosan kapcsoltaknak nevezik. 
A legegyszerűbb, ha **egyetlen sín van, amelyhez csatlakoztatjuk a memóriát és az összes processzort**. 
Ha sok gyors processzor próbálja állandóan elérni a memóriát a közös sínen keresztül, az **konfliktusokhoz vezet**. 

Az egyik megoldás, hogy minden processzornak biztosítunk valamekkora saját lokális memóriát, amelyet a többiek nem érhetnek el. Így csökken a közös sín forgalma. Jellemzően maximum pár száz CPU-t építenek össze.

**Multiszámítógépek:**

Nehéz sok processzort és memóriát összekötni. Ezért gyakran sok összekapcsolt számítógépből álló rendszereket építenek, amelyeknek csak saját memóriájuk van. 
A **multiszámítógépek CPU-it lazán kapcsoltaknak** nevezik. A multiszámítógép processzorai üzenetek küldésével kommunikálnak egymással. 
Nagy rendszerekben nem célszerű minden számítógépet minden másikkal összekötni, ezért **2 és 3 dimenziós rácsot, fákat és gyűrűket használnak az összekapcsolásra** Ennek következtében egy gép valamelyik másikhoz küldött üzeneteinek gyakran egy vagy több közbenső gépen vagy csomóponton kell áthaladniuk ahhoz, hogy a kiindulási helyükről elérjenek a céljukhoz. 
Néhány mikroszekundumos nagyságrendű üzenetküldési idők nagyobb nehézség nélkül elérhetők. 10 000 processzort tartalmazó multiszámítógépeket is építettek már.

## Korszerű számítógépek tervezési elvei

- Minden utasítást közvetlenül a hardver hajtson végre.
    - Ezek nem bonthatók fel interpretált mikroutasításokra. Az interpretációs szint kiküszöbölésével a legtöbb utasítás gyors lesz.
- Maximalizálni kell az utasítások kiadásának ütemét
    - Megpróbálják egy másodperc alatt a lehető legtöbb utasítás végrehajtását elkezdeni, tehát a párhuzamosságra kell törekedni.
- Az utasítások könnyen dekódolhatók legyenek.
    - Az utasítások szabályosak, egyforma hosszúak legyenek, és kevés mezőből álljanak.
- Csak a betöltő és tároló utasítások hivatkozzanak a memóriára
    - A memóriaműveletek sok időt vehetnek igénybe, legjobb más utasításokkal átfedve végrehajtani, ha semmi mást nem tesznek, csak adatokat mozgatnak a regiszterek és a memória között, minden más utasítás csak regisztereket használhat.
- Sok regiszter legyen.
    - Mivel a memóriaműveletek lassúak, sok regiszterre van szükségünk, hogy egy beolvasott szó mindig a regiszterben maradhasson, amíg szükség van rá.

## RISC Reduced Instruction Set Computer – Csökkentett utasításkészletű számítógép

A mikroprocesszorok létrejöttét követően két irányzat alakult ki. – RISC, CISC
Azt a szempontot tartották szem előtt, hogy a processzor kevés alapvető utasítást tudjon végrehajtani, de azokat rendkívül gyorsan (jellemzően 1 órajelciklus alatt). Ezek a RISC (Reduced Instruction Set Computer - redukált utasításkészletű) processzorok.
Itt az összetettebb funkciókat több utasítás kombinációjával lehet megvalósítani. A RISC mikroprocesszorokba számos belső regiszter kerül integrálásra, ezáltal is csökkentve a memóriához való fordulás gyakoriságát és gyorsítva a mű ködést. 
Ugyancsak sajátja ezen processzoroknak a - később ismertetett - ún. pipeline architektúra. Ennek lényege az, hogy a műveleteket részműveletekké bontják szét, és e részműveleteket időben párhuzamosítják, A RISC processzorok az utolsó 10 évben - első sorban a nagyobb teljesítményt igénylő rendszereknél (pl. munkaállomások) nyertek teret
Nagyon kevés utasítással rendelkeznek, tipikusan 50 körül. Az adatút egyszeri bejárásával végrehajthatók ezek az utasítások, tehát egy órajel alatt. Nem használ mikroprogram interpretálást, ezért sokkal gyorsabb, mint a CISC.

**UltraSparc architektúra:**
1. Memória: 8 bit-byteokból áll össze. (halfword, word, doubleword)
2. Regiszterek: 100 féle különböző általános célű regisztert tartalmaz. Egy adott task egyszerre csak 32 regisztert érhet el.
3. Adat formája: 
	- Integerek 8-, 16-, 32- vagy 64-bit bináris számok
	- Karakterek 8 biten ASCII kódolásban
	- Lebegőpontosok három különböző formában tárolódnak (egyszeres-, kétszeres, négyszeres-pontosságú) 
4. Utasítás formátuma: 3 alapvető utasítást formát használ. Mindegyik 32-bit hosszú ahol az első két bit a jelző bit.
	1. A  hívásokért felelős
	2.  Utasítások elágazásáért felelős
	3. Az összes többi utasítás használja, mint például a regiszter betöltés és a tárolás.


Példa: IBM 801, UltraSPARC, ARM

## CISC Complex Instruction Set Computer – Összetett utasításkészletű számítógép
Azok a processzorok tartoznak ide, amelyek utasításkészlete lehetőleg minden programozói igényt ki próbál elégíteni, vagyis komplex utasításkészletet alkot. Ezeket nevezzük CISC (Complex Instruction Set Computer = komplex utasításkészletű számítógép) processzoroknak. Markáns elemei az Intel processzorok. A CISC törekvésnek az egyik mozgatórugója, hogy megpróbálják a magasabb szintű nyelvek lehetőségeit közelíteni, vagyis, hogy a programozás "munkaigényes" alacsony szintjét, gépközeli voltát így is ellensúlyozzák.
Interpretálást használ, ezért sokkal összetettebb utasításai vannak, mint egy RISC gépnek. Több száz ilyen utasítása lehet. Az interpretálás miatt lassabb a végrehajtás.

Példa: x86 architektúrák pl. Intel 80x86 család.