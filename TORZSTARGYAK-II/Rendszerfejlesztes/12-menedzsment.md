
# 12. Projektmenedzsment. Költségbecslés, szoftvermérés

## Projektmenedzsment
**Tényezők: (4P):**
- **Munkatársak (people):** Sikeres projekt legfontosabb tényezői
- **Termék (product):** Létrehozandó termék
- **Folyamat (process):** A feladatok, tevékenységek halmaza
- **Projekt:** Minden olyan tevékenység, ami a termék létrehozásához szükséges.

**Összetevői:**
- Az emberek menedzselése
- Minőség-ellenőrzés és -biztosítás
- Folyamat továbbfejlesztése
- Konfiguráció kezelés
- Rendszer építés
- Hibamenedzsment

**Projekt sikertelenségének okai:**
- A szükséges ráfordítások alulbecslése
- Technikai nehézségek
- A projekt csapatban nem megfelelő a kommunikáció
- A projekt menedzsment hibái

### Az emberek menedzselése

Szoftverfejlesztő szervezet legnagyobb vagyona az emberek
Sok projekt bukásának legfőbb oka a rossz humánmenedzsment
Hatékony együttműködés fontos - Csapatszellemet kell kialakítani
Fontos a kommunikáció
Az emberek kiválasztása különböző tesztekkel történhet:

- Programozási képesség
- Pszichometrikus tesztek

### Csoportmunka
- Hatékony együttműködést kell kialakítani
- Fontos a munkakörnyezet
	- Nyitott, privát tér kombinálás, közös terek
- Csoport összetétele és kommunikáció fontos.

Több formája van pl:
- *Zárt forma:* Hagyományos felépítés
- *Véletlenszerű forma:* Laza szerkezet, egyedi kezdeményezések
- *Nyitott forma:* zárt és véletlenszerű kombinálása

### Minőség-ellenőrzés és –biztosítás
*Mindenki célja:* termék vagy szolgáltatás minőségének magas szinten tartása
A termék feleljen meg a specifikációnak
Fejlesztőnek is lehetnek (belső) igényei, pl. karbantarthatóság
Egyes jellemzőket nem könnyű specifikálni , pl. karbantarthatóság

### Szoftverköltség becslése
Projekt tevékenységeihez tartozó, **munka-, idő- és pénzköltségek**.
Becsléseket kell adni és **folyamatosan frissíteni**

### Folyamat továbbfejlesztése

CMM(I) (Capability Maturity Model (Integration)): a szoftver folyamat mérése

- Cél: a szoftverfejlesztési folyamat hatékonyságának mérése
- Egy szervezet megkaphatja valamely szintű minősítését
- 5 besorolási szint
    - 1. Kezdeti: csak néhány folyamat definiált, a többségük esetleges
    - 2. Reprodukálható: az alapvető projekt menedzsment folyamatok definiáltak. Költség ütemezés, funkcionalitás kezelése
    - 3. Definiált: a menedzsment és a fejlesztés folyamatai is dokumentáltak és szabványosítottak az egész szervezetre.
    - 4. Ellenőrzött: a szoftver folyamat és termék minőségének részletes mérése, ellenőrzése.
    - 5. Optimalizált: a folyamatok folytonos javítása az új technológiák ellenőrzött bevezetésével

A szoftver folyamat javítása - Az alapvető cél a minőség és a hatékonyság növelése

Használjunk metrikákat

Hiba analízis

- Hibák eredetének kategorizálása
- Hibák javítási költségei

### Konfiguráció kezelés

A rendszer változásainak kezelése

Változások felügyelt módon történjenek

Fejlesztés, evolúció, karbantartás miatt van rá szükség

Minőségkezelés része

Szoftver változatok

- Verziók (version, revision)
- Kiadások (release)
- Alapvonal (baseline, mainline, trunk)
- Fejlesztési ágak (branch)

Konfigurációs adatbázis - mindent tárol:

- Forráskód, (bináris kód), dokumentumok
- Építési folyamat, szkriptek
- Hiba adatbázis
- Változtatások története
- Verziók

### Rendszer építés

Komponensek fordítása és szerkesztése

Komponensek (és fájlok) között építési függőségek vannak

Nagy rendszernél bonyolult a folyamat - Hosszadalmas is, ezért inkrementálisan kell végezni

Automatizálni kell: építési szkriptek: configure, make

Eszközkiválasztás (fordítóprogram), beállítások

### Hibamenedzsment

Hibák követése fontos

Fontos, mert sok hiba van/lesz: kategorizálás, prioritások felállítása, követés elengedhetetlen

Milyen jellegű a hiba - (hibabejelentés, új feature, ...)

Hibák követésére hibaadatbázis

- Minden hibának egyedi azonosítója van
- Bejelentő neve
- Kijelölt felelős személy, megfigyelők listája
- Dátum
- Rövid összegzés
- Súlyosság: pl. triviális, kicsi, nagy
- Platform, operációs rendszer
- Termék, komponens, verziószám
- Függőségek más hibákkal
- Fontos a hiba életútjának rögzítése

### Szoftverköltség becslése

Projekt tevékenységeinek kapcsolódása a munka-, idő- és pénzköltségekhez
Becsléseket lehet és kell adni

Projekt összköltsége:

- Hardver és szoftver költség karbantartással
- Utazási és képzési költség
- Munkaköltség

Ezeket meg kell becsülni:

- Mennyi pénz?
- Mennyi ráfordítás?
- Mennyi idő?

Munkaköltség:

- Legjelentősebb
- Fejlesztők fizetése
- Kisegítő személyzet fizetése
- Bérleti díj, rezsi
- Infrastruktúra használat (pl. hálózat)
- Járulékok, adók

## Szoftvermérés

Szoftvermérés: termék vagy folyamat valamely jellemzőjét numerikusan kifejezni (metrika).
Ezen értékekből következtetések vonhatók le a minőségre vonatkozóan.

Két csoport:

- Vezérlési metrikák. Folyamattal kapcsolatosak, pl. egy hiba javításához szükséges átlagos idő(folyamat és projekt metrikák)
- Prediktor metrikák. Termékkel kapcsolatosak, pl. LOC, ciklomatikus komplexitás, osztály metódusainak száma (termék metrikák)
    - LOC = Lines Of Code
        - Több technika: Csak nem üres sorok, Csak végrehajtható sorok
        - Félrevezető lehet - Nem összehasonlítható programozási nyelvek (assembly, magas szintű nyelv)
- Mérési folyamat:
    - Alkalmazandó mérések kiválasztása
    - Mérni kívánt komponensek kiválasztása
    - Mérés (metrika számítás)
- Termék metrikák
    - Dinamikus
        - Szorosabb kapcsolat egyes minőségi jellemzőkkel
        - (pl. teljesítmény, hibák száma)
    - Statikus
        - Közvetett kapcsolat
        - Számtalan konkrét metrikát ajánlottak már
        - Kritikus kérdés: hogyan következtetünk a minőségi jellemzőkre a sok számból?
    - Fajták:
        - Méret
        - Komplexitás, csatolás, kohézió
        - Objektumorientáltsággal kapcsolatos metrikák
- Méret alapú metrikák (folyt.)
    - Széleskörűen használják ezeket a metrikákat, de nagyon sok vita van alkalmazásokról
    - Hibák / KLOC
    - Defekt / KLOC
    - Költség / LOC
    - Dokumentációs oldalak / KLOC
    - Hibák / emberhónap
    - LOC / emberhónap
    - Költség / dokumentációs oldal
- Funkció alapú metrikák
    - Felhasználói inputok száma - alkalmazáshoz szükséges adatok
    - Felhasználói outputok számariportok, képernyők,hibaüzenetek
    - Felhasználói kérdések száma - on-line input és output
    - Fájlok száma- adatok logikai csoportja
- 3D mérték
    - Számítás: Index=I+O+Q+F+E+T+R
        - I=input
        - O=output
        - Q=lekérdezés
        - F=fájlok
        - E=külső interfész
        - T=transzformáció
        - R=átmenetek
- Minőség mérése
    - Integritás: külső támadások elleni védelem
    - Fenyegetettség: annak valószínűsége, hogy egy adott típusú támadás bekövetkezik egy adott időszakban
    - Biztonság: annak valószínűsége, hogy egy adott típusú támadást visszaver a rendszer
    - Integritás = Σ [1-(fenyegetettség x (1-biztonság))] (Összegzés a különböző támadás típusokra történik)
    - DRE (defect removal efficiency)
        - DRE = E/(E+D), ahol E olyan hibák száma, amelyeket még az átadás előt felfedezünk, D pedig az átadás után a felhasználó által észlelt hiányosságok száma
