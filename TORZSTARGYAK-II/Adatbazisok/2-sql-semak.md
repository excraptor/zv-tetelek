# 2. Az SQL adatbázisnyelv: Az adatdefiníciós nyelv (DDL) és az adatmanipulációs nyelv (DML). Relációsémák definiálása, megszorítások típusai és létrehozásuk. Adatmanipulációs lehetőségek és lekérdezések

## SQL

Structured Query Language, egy lekérdező nyelv. Arra szolgál, hogy adatokat kezeljünk vele.
- beszúrás
- törlés
- módosítás
- lekérdezés

A nyelv elemeit két fő részre oszthatjuk.

## Az adatdefiníciós nyelv (DDL)

Ide tartoznak az adatbázisok, sémák, típusok definíciós utasításai, pl:

- CREATE DATABASE
- CREATE TABLE
- ALTER TABLE
- DROP TABLE
- **CREATE TRIGGER**: Nem tábla létrehozásra van

## Az adat manipulációs nyelv (DML)

Ide tartoznak a beszúró, módosító, törlő, lekérdező utasítások.

- INSERT INTO
- UPDATE 
- DELETE FROM 
- SELECT

Egyes irodalmak különválasztják a lekérdező utasításokat a manipulációs utasításoktól.

## Relációsémák definiálása, megszorítások típusai és létrehozásuk

Relációsémákat a 
```
CREATE TABLE tablanev(
	mező1 típus [oszlopfeltételek],
	....
	[tablafeltételek]
);
```

utasítással hozhatunk lére. A sémák különböznek a tábláktól, és nevével ellentétben a CREATE TABLE utasítás csak a relációsémát hozza létre. A tábla már az adatrekordok halmazát jelenti.

### Megszorítások

**Oszlopfeltételek:**

Csak az adott mezőre vonatkoznak

- **PRIMARY KEY**, az elsődleges kulcs
- **UNIQUE**, kulcs, minden érték egyszer fordulhat elő az oszlopban
- **NOT NULL**, az oszlop értéke nem lehet NULL, azaz kötelező kitölteni
- **REFERENCES T(oszlop)**, a T tábla oszlop oszlopára vonatkozó külső kulcs
- **DEFAULT tartalom**, az oszlop alapértelmezett értéke tartalom lesz

**Táblafeltételek**

Ha több oszlopra is vonatkoznak feltételek, azt itt tudjuk megadni.

- **PRIMARY KEY(oszloplista)**, az elsődleges kulcs/kulcsok
- **UNIQUE (oszloplista)**, kulcs, minden érték egyszer fordulhat elő az oszlopban
- **FOREIGN KEY (oszloplista) REFERENCES T(oszloplista)**, a T tábla oszloplista oszloplistájára vonatkozó külső kulcs

**Külső kulcs feltételek és szabályok**
Az integritás megőrzése szempontjából a külső kulcsokhoz meghatározhatjuk azt is, hogy hogyan viselkedjenek a hivatkozott kulcs törlése vagy módosítása esetén.

**ON DELETE**
- **RESTRICT,** ha van a törlendő rekord kulcsára van vonatkozó külső kulcs, megtiltjuk a törlést
- **SET NULL,** a törlendő rekord kulcsára hivatkozó külső kulcs értékét NULL-ra állítjuk
- **NO ACTION,** a törlendő rekord kulcsára vonatkozó külső kulcs értéke nem változik
- **CASCADE,** a törlendő rekord kulcsára hivatkozó külső kulcsú rekordok is törlődnek

**ON UPDATE**

- **RESTRICT,** ha van a módosítandó rekord kulcsára van vonatkozó külső kulcs, megtiltjuk a módosítást
- **SET NULL,** a módosítandó rekord kulcsára hivatkozó külső kulcs értékét NULL-ra állítjuk
- **NO ACTION,** a módosítandó rekord kulcsára vonatkozó külső kulcs értéke nem változik
- **CASCADE,** a módosítandó rekord kulcsára hivatkozó külső kulcsú rekordok is az új értékre változnak


**Táblákra és attribútumokra vonatkozó megszorítások**

Elsődleges feladata, hogy megelőzzük az adatbeviteli hibákat, és elkerüljük a hiányzó adatokat a kötelező mezőkből.

**NOT NULL:** a cella értékét kötelező kitölteni, nem lehet NULL

**CHECK (feltétel):** ellenőrző feltétel arra, hogy milyen értékeket vehet fel az adott oszlop

**DOMAIN:** értéktartomány egy oszlop értékeire vonatkozóan


## Adatmanipulációs lehetőségek és lekérdezések

#### **Adatok beszúrása:**

Ha csak adott oszlopoknak akarunk értéket adni (pl mert nem kötelező, vagy alapértelmezett érték):
 `INSERT  INTO táblanév (oszloplista) VALUES (értéklista);`
Ha minden oszlop értékét ki akarjuk tölteni:
`INSERT  INTO táblanév VALUES (értéklista);`

Adatok módosítása:

```
UPDATE táblanév SET
 oszlop=kifejezés 
 [oszlop2=kifejezés2] 
 [WHERE feltétel];
```

Módosítjuk egy vagy több oszlop értékét az adott táblában, azokon a sorokon, amelyek eleget tesznek a WHERE záradékban tett feltételnek.

#### **Adatok törlése:**

`DELETE FROM táblanév [WHERE feltétel];`

Töröljük az összes rekordot a táblából, amelyek megfelelnek a WHERE záradékban megadott feltételnek.

#### **Lekérdezések:**

`SELECT oszloplista FROM tábla;`

A megadott oszlopokat kilistázza az adott táblából. oszloplista helyére megadható \*, ha az összes oszlopot listázni akarjuk.

**Teljes szintaxisa:** 
```
SELECT [DISTINCT] oszloplista FROM táblalista 
[WHERE feltétel]
[GROUP  BY oszloplista] 
[HAVING csoportfeltétel]
[ORDER  BY oszloplista [DESC]];
```
**DISTINCT:** csak a különböző sorokat írja ki
**FROM táblalista:** a táblalistában megadott táblákbó képez Descartes szorzatot
**WHERE:** kiválasztás a feltétel szerint
**GROUP BY:** csoportosítás az oszloplistában szereplő oszlopok szerint
**HAVING:** a csoportosítás után a csoportokra vonatkozó feltétel
**ORDER BY:** az oszloplistában szereplő adatok rendezése abc szerint növekvő vagy csökkenő sorrendben

#### **Összesítő függvények**

Leggyakrabban a **GROUP BY-jal együtt** szoktuk használni, de enélkül is lehet.
**Leginkább** a **SELECT utáni oszloplistában**, de a **where-ben** és a **having-ban** is használható. Az eredményoszlopokat AS kulcsszóval el is nevezhetjük.

**MIN(oszlop):** az oszlopban lévő minimumot adja vissza
**MAX(oszlop):** maxot
**AVG(oszlop):** az oszlop átlaga
**SUM(oszlop):** az oszlop összege
**COUNT (\[DISTINCT\]** oszlop): az eredményben szereplő (különböző) rekordok száma

#### **Természetes összekapcsolás**

**SELECT * FROM T1, T2 WHERE T1.X = T2.X;**

X az most egy oszlop, egy kulcs-külső kulcs kapcsolat.

Erre használható még SQL-ben az **INNER JOIN** kulcsszó is.

```SELECT * FROM T1, T2 INNER JOIN T2 ON T1.X = T2.X;```

Használható még a NATURAL JOIN kifejezés is, de ez egy picit máshogy működik. Ennek a használatához a két tábla közös attribútumhalmaza ugyanazokat az oszlopneveket tartalmazza mindkét táblában és a párosított oszlopok típusa is megegyezik. Ebből kifolyólag nem kell megadnunk a kapcsolódó, kulcs és külső kulcs oszlopokat. A közös oszlop csak egy példányban jelenik majd meg.

```SELECT * FROM T1 NATURAL JOIN T2;```

**Jobboldali, baloldali és teljes külső összekapcsolás:**
Valamelyik, vagy mindkét tábla összes rekordja szerepelni fog az eredményben.

**Baloldali összekapcsolásnál (LEFT JOIN)** a baloldali tábla minden rekordja megmarad, és ezekhez a rekordokhoz párosítjuk a jobboldali tábla rekordjait. 
**Jobboldalinál (RIGHT JOIN) pont fordítva**. 
**Teljes összekapcsolásnál (FULL OUTER JOIN)** pedig mindkét tábla összes rekordja megmarad, és mindenhol a hiányzó helyeken NULL értékek lesznek.

**Theta kapcsolás**
Nem feltételezünk, hogy lenne a két táblának közös kapcsolómezője. $\rightarrow$ **Descartes szorzat**
```SELECT * FROM T1 , T2 WHERE feltétel ;```


**Lekérdezések eredményén, amikor ugyanannyi és ugyanolyan típusú oszlopot kérünk le**, használhatunk halmazműveleteket is, pl **UNION vagy INTERSECT**.

#### Alkérdések

Alkérdés tulajdonképpen egy **SELECT** utasítás. Leginkább a **WHERE** és **HAVING** feltételeibe szoktuk megadni.

Lehetőség van megadni őket beszuró, módosító és törlő utasitásokban.
Pl: ```INSERT INTO táblanév [(oszloplista)] AS (alkérdés);```