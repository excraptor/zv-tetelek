

# 1. Adatbázis-tervezés: A relációs adatmodell fogalma. Az egyed-kapcsolat diagram és leképezése relációs modellre, kulcsok fajtái. Funkcionális függőség, a normalizálás célja, normálformák


# 1. Adatbázis-tervezés: A relációs adatmodell fogalma. Az egyed-kapcsolat diagram és leképezése relációs modellre, kulcsok fajtái. Funkcionális függőség, a normalizálás célja, normálformák

## A relációs adatmodell fogalma
A relációs adatmodell mind az adatokat, mind a köztük lévő kapcsolatokat kétdimenziós táblákban tárolja.

**Attribútum:**
- névvel, értéktartománnyal megadott tulajdonság
- Z értéktartományát dom(Z) jelöli
- csak elemi típusú értékekből állhat (numerikus, karakter, string)
- gyakran megadjuk az ábrázolás hosszát is

**Relációséma:**
Ha $A = \{A_1,..,A_n\}$ jelöli az **attribútumhalmazt** és a **séma neve** $R$, akkor a **relációsémát** $R(A_1,...,A_n)$ = $R(A)$ jelöli
- névvel ellátott attribútumhalmaz
- névütközés esetén kiírhatjuk a tábla nevét is az attribútum elé

A relációséma nem tárol adatot!
Csak szerkezeti leírást jelent.

Az adatok relációkkal adhatók meg. Egy R(A) séma feletti reláció A értéktartományainak direktszorzatának egy részhalmaza (mindegyik attribútum értékei közül választunk egyet, és ezt egy vektorba pakoljuk). Egy ilyen reláció már megjeleníthető adattábla formájában, egy reláció a táblázat egy sorának felel meg.

## Az egyed-kapcsolat diagram és leképezése relációs modellre

### EK-diagram

Az egyed-kapcsolat modell konkrét adatmodelltől függetlenül, szemléletesen adja meg az adatbázis szerkezetét.

**Egyed vagy entitás**
- a valós világ egy objektuma
- szeretnénk róla információt tárolni az adatbázisban
- **egyedtípus:** általánosságban jelent egy valós objektumot
- **egyedpéldány:** egy konkrét objektum
- **gyenge egyed:** ha az egyedet nem határozza meg egyértelműen attribútumainak semmilyen részhalmaza

**Tulajdonság vagy attribútum**
- az egyed egy jellemzője
- **tulajdonságtípus:** Pl felhasználók jelszava  általánosságban
- **tulajdonságpéldány:** pl Egy konkrét jelszó
- az attribútumok egy olyan legszűkebb részhalmazát, amely egyértelműen meghatározza az egyedet, **kulcsnak** nevezzük

**Kapcsolatok**

- egyedek között alakulhatnak ki
- **kapcsolattípus:** pl felhasználó és üzenet között
- **kapcsolatpéldány:** pl Kis József és a 69420. üzenet
- kapcsolatoknak is lehet tulajdonsága

Azt a modellt, amelyben az adatbázis a tárolandó adatokat egyedekkel, tulajdonságokkal és kapcsolatokkal írja le, egyed-kapcsolat modellnek nevezzük, a hozzá kapcsolódó diagramot pedig egyed-kapcsolat diagrammnak.

A diagramon

- az egyedeket téglalappal
- a tulajdonságokat ellipszissel
- a kulcsot aláhúzással
- a kapcsolatokat rombusszal 

jelöljük.


### EK leképezése relációs adatmodellre

**Egyedek leképezése**
- minden egyedhez egy relációsémát írunk fel, melynek neve az egyed neve, attribútumai pedig az egyed attribútumai, kulcsa pedig az egyed kulcsa
- gyenge egyednél az attribútumokhoz hozzá kell venni a meghatározó kapcsolatokon keresztük csatlakozó egyedek kulcsattribútumait is, külső kulcsként

**Összetett attr. leképezése**

- összetett attribútumot helyettesítünk az őt alkotó elemi attribútumokkal

**Többértékű attribútumok leképezése**

- egyik lehetőség:
    - eltekintünk attól, hogy többértékű, és egyszerű szövegként tároljuk
    - hátránya, hogy nem kezelhetők külön külön az elemek
- másik lehetőség:
    - minden sorból annyit veszünk fel, ahány értéke van a többértékű attribútumnak
    - hátránya a sok fölösleges sor
    - kulcsok elromlanak
    - kerülendő
- harmadik lehetőség
    - új táblát veszünk fel, ahova kigyűjtjük, hogy melyik sorhoz milyen értékei tartoznak a többértékű attribútumnak
    - akár külön kigyűjthetjük egy táblába az összes lehetséges értékét a többértékű attribútumnak, és egy kapcsolótáblával kötjük össze az egyeddel

**Kapcsolatok leképezése**

- minden kapcsolathoz felveszünk egy új sémát
- neve a kapcsolat neve, attribútumai a kapcsolódó egyedek kulcsattribútumai és a kapcsolat saját attribútumai
- meg kell határozni ennek a sémának is a kulcsát
- ha ez a kulcs megegyezik valamelyik kapcsolt egyed kulcsával, akkor ez a séma beolvasztható abba az egyedbe, ezt hívjuk konszolidációnak, ez a gyakorlatban egy lépésben is elvégezhető persze
- 1:1 kapcsolat esetén az egyik tetszőlegesen választott egyedbe beolvaszthatjuk a kapcsolat sémáját
- 1:N kapcsolat esetén az N oldali egyedet bővítjük a másik egyed kulcsattribútumaival, és a kapcsolat saját attribútumaival
- N:M kapcsolat esetén új sémát veszünk fel

**Specializáló kapcsolatok leképezése**

Minden megközelítésnek lehetnek hátrányai, mérlegelnünk kell

Első lehetőség

- főtípus és altípus is külön sémában, és az altípus attribútumai közé felvesszük a főtípus attribútumait is
- minden egyedpéldány csak egy táblában fog szerepelni

Második lehetőség

- minden altípushoz új séma, de abban csak a főtípus kulcsattribútumai jelennek meg
- minden egyedpéldány szerepel a saját altípusának táblájában és a főtípus táblájában is

Harmadik lehetőség

- egy közös tábla az összes lehetséges attribútummal
- minden sorban csak a releváns cellákat töltjük ki

## Kulcsok fajtái

**Szuperkulcs**
- egyértelműen azonosítja a tábla sorait
- $R(A)$ bármely két sora különbözik a szuperkulcson
- mivel a táblában általában nem engedünk meg ismétlődő sorokat, ezért ha az összes attribútumot vesszük, az mindig szuperkulcs

**Kulcs**
- olyan szuperkulcs, amelynek egyetlen valódi részhalmaza sem szuperkulcs
- ha egyelemű, **egyszerű kulcsnak** nevezzük
- ha többelemű, **összetettnek**
- előfordulhat, hogy van több kulcs is, ekkor kiválasztunk egyet
- a kiválaszott kulcsot elsődleges kulcsnak nevezzük

**Külső kulcs**

- másik, vagy ugyanazon séma elsődleges kulcsára vonatkozik

Mind az elsődleges kulcs és a külső kulcsok is a sémára vonatkozó feltételek, függetlenek az adatoktól

## Funkcionális függőség

P és Q attribútumhalmazok, az R(A) sémán
P-től funkcionálisan függ Q, ha bármilyen R feletti tábla esetén ha P-n megegyezik két sor, akkor Q-n is meg fog egyezni.

Triviális, ha Q részhalmaza P-nek, és nemtriviális, ha P-nek és Q-nak nincs közös attribútuma.

Pl a felhasználónévtől funkcionálisan függ az email sokszor.

## Normalizálás célja, normálformák

Tárolhatnánk az összes adatunkat egy nagy táblában is, de ilyenkor gondok merülhetnek fel az adatbázisműveletek során, illetve nagyon redundáns lenne az adattárolás. A normalizálás célja kisebb táblák létrehozása a redundancia elkerülése érdekében.

### Normálformák

Dekompozíció segítségével megszüntetjük lépésről lépésre a redundanciát úgy, hogy a sémában lévő függőségekre egyre szigorúbb feltételeket adunk.

**Elsődleges, másodlagos attribútum:** szerepel a séma valamelyik kulcsában, ha nem akkor másodlagos
Tranzitív, közvetlen függés: Ha $X$-től függ $Z$, és van olyan $Y$, hogy $X \rightarrow Y$ és $Y \rightarrow Z$, ellenkező esetben közvetlenül függ

1NF:

- Ha az attribútumok értéktartománya csak egyszerű adatokból áll (nincs többszörös vagy összetett attribútum)

2NF:

- Ha minden másodlagos attribútum teljesen függ bármely kulcstól

3NF:

- Minden másodlagos attribútum közvetlenül függ bármely kulcstól, azaz nincs tranzitív függés

BCNF:

- Egy relációséma Boyce-Codd normálformában van, ha bármely nemtriviális $L \rightarrow B$ függés esetén L szuperkulcs.
