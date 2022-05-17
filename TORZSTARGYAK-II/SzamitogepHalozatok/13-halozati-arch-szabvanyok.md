
# 13. Számítógép-hálózati architektúrák, szabványosítók (ISO/OSI, Internet, ITU, IEEE)

## ISO

International Organization for Standardization, Nemzetközi Szabványügyi Szervezet

Mindenféle szabványokat adnak ki, 165 tagállam nemzeti szabványügyi szervezete alkotja. A távközlési szabványokhoz az ISO és az ITU-T gyakran együttműködik, hogy a szabványok kompatibilisek legyenek egymással.

## OSI

A számítógépek kommunikációjához szükséges hálózati protokollt határozza meg.

**OSI - Open System Interconnection**

A különböző protokollok által nyújtott funkciókat rendezi egymásra épülő rétegekbe. Minden réteg csak az alsóbb rétegek által nyújtott funkciókra támaszkodhat, és az általa nyújtott funkciókat csak a felette lévő réteg számára nyújthatja. Ezt a rendszert gyakran protokoll veremnek is nevezik. Az OSI modell hét réteget definiál, az alsóbb rétegek azok, amelyeket hardver szinten is megvalósítanak, a felsőbbek szoftveresen kerülnek megvalósításra.

A rétegek alulról felfelé

- **Fizikai réteg**
    - feladata, hogy a biteket továbbítsa a kommunikációs csatornán
    - mekkora feszültség kell a 0, 1 bitek reprezentálásához, mennyi idő, hogyan jön létre az összeköttetés stb.
    - Csatlakozás felépítése és lezárása
    - Hubok, repeaterek, hálózati adapterek
- **Adatkapcsolati réteg**
    - átvitendő adatokat a küldő fél oldalán adatkeretekbe tördeli, és sorrendben továbbítja
    - a fogadó fél nyugtázza minden keret helyes vételét
    - forgalomszabályozás, hibakezelés
    - Bridgek, switchek
- **Hálózati réteg**
    - milyen útvonalon kell a csomagokat a forrásállomástól a célig eljuttatni
    - lehet **statikus, és dinamikus meghatározás** is
    - Hálózati útvonalválasztás és adatáramlás ellenőrzés
    - Routerek, IP switchek
    - **IP protocol (IP) itt található**
- **Szállítási réteg**
    - forgalomszabályozás, hibajavítás, multiplexelés
    - megbízhatóság: pl ellenőrző összeggel megnézzük, hogy az adat sérült-e
    - **TCP protokoll**
- **Viszony réteg**
    - két számítógép felhasználói kapcsolatot létesítsen
    - állományokat mozgathatunk
    - Lehet *duplex*
	    - egyidejűleg kétirányú kommunikáció
	- vagy *félduplex*
		- Kétirányú összeköttetés, de egyszerre csak egy fél küldhet üzenetet.
- **Megjelenítési réteg**
    - átvitt információ szintaktikája, szemantikája
    - a párbeszéd során absztrakt módon kell definiálni a kódolásokat
    - Adatok megfelelő formában jelenjenek meg a végfelhasználónál.
- **Alkalmazási réteg**
    - protokollok sokasága, **HTTP, FTP**
    - szolgáltatásai támogatják a szoftver alkalmazások közötti kommunikációt


## Internet

Összekapcsolt számítógépes hálózatok globális rendszere, ami a **TCP/IP** protokollt használja a kommunikációhoz. Olyan hálózatok hálózata, amely üzleti, kormányzati, állai, magán, tudományos stb hálózatokból áll. Közös protokollokat használnak és közös szolgáltatásokat nyújtanak.

Nincs központosított irányítása, sem a technológiai megvalósításban, sem a hozzáférésre és használatra vonatkozó politikában.

Elsődleges előfutár-hálózata az ARPANET volt, ami regionális tudományos és katonai hálózatok összekapcsolásának gerincét szolgáltatta. Miután a TCP/IP lett az egyetlen hivatalos protokoll rajta, gyorsan nőtt a hozzá csatlakozó hálózatok, gépek és felhasználók száma.

Azóta mégtöbb terület csatlakozott hozzá, globális gerinchálózatok épültek ki.

Egy gép rajta van az interneten, ha a TCP/IP protokollt használja, van saját IP-je, és tud más gépeknek csomagokat küldeni az interneten át.

Fő alkalmazási területek hagyományosan:

- e-levél
- hírek
- távoli bejelentkezés
- fájltranszfer

Egy új alkalmazás, a WWW bevezetése vont be több millió új felhasználót a hálózatba. Nem változatott semmit az rendelkezésre álló eszközökön, csak egyszerűbbé tette a használatukat. A böngészők megjelenésével képeket, szöveget tartalmazó oldalakra is el lehetett jutni, és onnan más oldalakra továbbnavigálni.

A növekedés nagy része az ún. ISP-knek is köszönhető. Egyéni felhasználóknak nyújtanak szolgáltatásokat, internetelérést.

## ITU
**International Telecommunication Union - Nemzetközi Távközlési egyesület**

Szükség van világméretű kompatibilitásra, hogy a különböző országokban élő emberek/számítógépek kapcsolatba kerülhessenek egymással.
A feladata az, hogy szabványosítsa a nemzetközi távközlést.

**Három fő ágazata van:**

- ITU-R: rádiókommunikációs ágazat
- ITU-T: távközlési szabványosítási ágazat
- ITU-D: fejlesztési ágazat

**ITU-R**

Az 1927-ben Nemzetközi Rádió Tanácsadó Bizottság vagy CCIR néven (francia nevén Comité consultatif international pour la radio ) alapított ágazat kezeli a nemzetközi rádiófrekvenciás spektrum- és műholdpálya-erőforrásokat. 1992-ben a CCIR lett az ITU-R. Feladata a rádiófrekvenciák kiosztása a világszerte egymással versengő csoportoknak.

**ITU-T**

A szabványosítás a kezdetektől fogva célja az ITU-nak. 1956-ban a Nemzetközi Telefon- és Távirati Tanácsadó Bizottság egységesíti a globális távközlést.

Az ITU-T feladata, hogy műszaki javaslatokat tegyen az adatkommunikáció interfészeire. Ezek gyakran válnak nemzetközi szabványokká. Fontos, hogy ezek csak műszaki javaslatokat tartalmaznak. Az elfogadása csak az adott országon múlik.

**ITU-D**

Az 1992-ben létrehozott ágazat hozzájárul az információs és kommunikációs technológiákhoz (IKT) való igazságos, fenntartható és megfizethető hozzáférés terjesztéséhez.

## IEEE

**Villamos és Elektronikai Mérnökök Intézete**

A világ legnagyobb szakmai szervezete.
Konferenciák és folyóiratok mellett szabványokat dolgoznak ki a villamosmérnöki tudományok és az informatika terén.

Az **IEEE 802**-es bizottsága több **LAN** fajtát szabványosított. A sikertörténetek (802.3 és **802.11: WLAN, adatátviteli protokoll**, logikai kapcsolatvezérlés és vezeték nélküli LAN) hatása óriási volt. 