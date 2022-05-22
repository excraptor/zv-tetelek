
# 13. Számítógép-hálózati architektúrák, szabványosítók (ISO/OSI, Internet, ITU, IEEE)

## ISO

International Organization for Standardization, Nemzetközi Szabványügyi Szervezet

Mindenféle szabványokat adnak ki, 165 tagállam nemzeti szabványügyi szervezete alkotja. A távközlési szabványokhoz az ISO és az ITU-T gyakran együttműködik, hogy a szabványok kompatibilisek legyenek egymással.

PL:
- Az **IEEE 802.11** egy vezeték nélküli adatátviteli protokoll, Az OSI két legalsó rétegét, a fizikai és az adatkapcsolati réteget definiálja.
- **IEEE 754/1985** lebegőpontos számformátum
## OSI

A számítógépek kommunikációjához szükséges hálózati protokollt határozza meg.

**OSI - Open System Interconnection**

A különböző protokollok által nyújtott funkciókat rendezi egymásra épülő rétegekbe. Minden réteg csak az alsóbb rétegek által nyújtott funkciókra támaszkodhat, és az általa nyújtott funkciókat csak a felette lévő réteg számára nyújthatja. Ezt a rendszert gyakran protokoll veremnek is nevezik. Az OSI modell hét réteget definiál, az alsóbb rétegek azok, amelyeket hardver szinten is megvalósítanak, a felsőbbek szoftveresen kerülnek megvalósításra.

A rétegek alulról felfelé

- **Fizikai réteg**
	- Bitek kommunikációs csatornára való juttatása.
    - Csatlakozás felépítése és lezárása
    - Hubok, repeaterek, hálózati adapterek
    - Ethernet szabványok is tartoznak ide. (pl: **IEEE 802.11** vezetéknélküli adatátvitel)
- **Adatkapcsolati réteg**
    - A **küldő** az adatokat egyértelmûen azonosítható adatkeretkre tördeli szét, ellátja a szükséges vezérlõbitekkel, majd sorrendben továbbítja azokat.
    - A **fogadó** oldal pedig a kapott kereteket megfelelõ sorrendben összeállítja.
    - Az **küldő** oldal ezenkívül még a fogadó által küldött **nyugtázásokat is feldolgozza.**
    - **Fizikai címzés: MAC cím**
    - forgalomszabályozás, hibakezelés
    - Bridgek, switchek
- **Hálózati réteg**
    - Milyen útvonalon kell az *adatkapcsolati réteg által elkészített keretek* a forrásállomástól a célig eljuttatni. $\rightarrow$ **Forgalomirányítás**
    - lehet 
	    - **statikus:** Táblázatok amelyek nem változnak
	   - **dinamikus:** Táblázatok változnak.
    - Hálózati útvonalválasztás és adatáramlás ellenőrzés
    - Routerek, IP switchek
    - **IP protocol (IP) itt található**, logikai címzés
    
- **Szállítási réteg**
	- *minden adat érintetlenül, sértetlenül érkezzen meg a rendeltetési helyére.*
	- Forrás- és célállomás egymással kommunikál
    - forgalomszabályozás, hibajavítás, multiplexelés
    - **megbízhatóság:** pl ellenőrző összeggel megnézzük, hogy az adat sérült-e
    - **TCP protokoll** itt található

A felső háromat együtt **felső rétegnek** nevezik

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
**Legfontosabb alkalmazás rétegei: a HTTP, FTP, SMPT, DNS**

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