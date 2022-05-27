
# 4. A PSPACE osztály. PSPACE-teljes problémák. Logaritmikus tárigényű visszavezetés. NL-teljes problémák

## Alapvető információk:
**Időigény:** Adott futásidejű algoritmus adott számítási kapacitású architektúrán mekkora inputra fut le.

**Az input mérete:** Az $a_1,..,a_n$ input **mérete** az $a_i$ számok **bináris reprezentáció** hosszának összege.

**A gép időkorlátja:** $M$ Ram gép időkorlátja az $f(n) : \N \rightarrow \N$ függvény, ha tetszőleges $n$ méretű inputon legfeljebb $f(n)$ lépésben megáll.

## Tárigény-elemzés
1. Input read-only? (**int: akárhány bites egész**)
*K a max értéke $\Rightarrow$ logK bit kell hozzá.*
	- Igen: Nem kell vele számolni, a hivónak kell lefoglalnia
	- Nem: Akkor számolnunk kell vele.
2. Lokális változók?
	- A lokális változók mekkora értéket vesznek fel és ezeket összekell adni. 


## PSPACE osztály = $Space(n^k)$
Polinom tárban (det. vagy nemdet.) eldönthető problémák osztálya.
**Savitch-tétel**: Az $f(n)$ tárban nemdeterminisztikusan eldönthető problémák mind eldönthetők determinisztikusan, $f^2(n)$ tárban is
Tehát: $NSPACE(f(n))$ részhalmaza $SPACE(f^2(n))$-nek és mivel polinom négyzete polinom $\rightarrow$ PSPACE = NPSPACE
+Elérhetőség eldönthető O(log^2n) tárban.

## PSPACE-teljes problémák
**Nehézség, teljesség:**
$A$ egy **probléma** $C$ pedig a problémák egy **osztálya**
	1. **C-nehéz:** Minden $C$-beli probléma visszavezethető $A$-ra
	2. **C-teljes:** $A$ probléma ráadásul $C$-ben van

QSAT PSPACE-teljes
QSAT (kvantifikált SAT)

- *Adott:* adott egy ítéletkalkulusbeli logikai formula, változó kvantorokkal az elején (létezik, bármely, létezik, bármely stb), **magja CNF alakú, kvantormentes**
- *Kérdés:* igaz-e ez a formula?

**QSAT mint kétszemélyes játék**
- input ugyanaz
- van-e az első játékosnak nyerő stratégiája abban a játékban, ahol:
- - a játékosok sorban értéket adnak a változóknak, első játékos x1-nek, második x2-nek stb
- - ha a formula igaz lesz, az első játékos nyert, ha hamis, akkor a második
- ez ugyanaz tkp, mint a sima QSAT, szóval ez is PSPACE-teljes

hasonlít a minimaxra
az éses csúcsoknál lévő játékos minimalizál

**Földrajzi játék**
- adott egy irányított gráf és egy kijelölt kezdőcsúcs
- az első játékosnak van-e nyerő stratégiája?
	-  az első játékos kezd, lerakja a bábut a kezdőcsúcsra
	-  felváltva lépnek
	-  egy olyan csúcsba kell húzni a bábut, ami egy lépésben elérhető, és ahol még nem voltak
	-  aki először nem tud lépni, vesztett

QSAT <= Földrajzi játék
Egy $\exists x_1\forall x_2 \exists x_3....\forall x_m \phi$ alakú formulából készÍtünk egy gráfot egy kezdőcsúccsal úgy, hogy 
- Ha a formula igaz, vagyis ha a $\exist$ játékosnak van nyerő stratégiája a QSAT játékban, akkor a készített FÖLDRAJZI JÁTÉK példányban az első játékosnak legyen;
- Ha pedig a $\forall$ játékosnak van nyerő stratégiája, akkor a második nyerje.
1. Minden változóhoz elkészitünk egy gadgetet és ezeket láncba kötjük.
2. Ha elágazáshoz érünk, akkor az választ, hogy fel vagy lehúzza a bábut: 0 vagy 1-re állítás
3. Ezután kényszeríti a következtő ellenfelet egy lépésre.
4. Felveszünk klózonként még egy új csúcsot és az utolsó gadget jobb oldalába éleket húzunk belőle ezekbe.
5. Továbbá a klúz csúcsokból visszafelé húzunk éleket az értékválasztó gadgetekbe: Ha $x$ szerepl benne, akor az $x$ gadged **alsó** csúcsába, ha $\neg x$ akkor a felsőbe.

Földrajzi játék PSPACE-teljes

Adott két reguláris kifejezés, igaz-e, hogy ugyanazokra a szavakra illeszkednek?
Adott két nemdet automata, ekvivalensek-e?
Adott, egy SOKOBAN/RUSH HOUR feladvány, megoldható-e?

## Logtáras visszavezetés = L= Space(log 𝑛)

Polinomidejű visszavezetés túl erős, ha pl P-beli problémákat akarunk egymáshoz viszonyítani, mert egy polinomidejű visszavezetés alatt már akár meg is oldhatnánk egy P-beli problémát

Logtáras visszavezetés
Jele: $A \le_l  B$.

 Ha $f$ egy olyan függvény, hogy
- A inputjaiból B inputjait készíti
- választartó módon
- és logaritmikus tárban kiszámítható

akkor f egy logtáras visszavezetés A-ról B-re.

## NL-teljes problémák = NSpace(log 𝑛)
Nemdeterminisztikus logtáras problémák

Elérhetőség 
1. Adott: egy 𝐺 = (𝑉, 𝐸) irányított gráf. Feltehetjük, hogy 𝑉 = {1, 2, . . . , 𝑛}. 
2. Kérdés: létezik-e 1-ből 𝑛-be vezető irányított út?
Nemdeterminisztikus módon választunk 1 és $n$ között csúcsot és mivel az inputot olvasni kell, outputra nem irunk semmit, csak két változót tartunk számon, amibe csak $1...n$ vannak számok így logtáras lesz.

**Immerman-Szelepcsényi tétel:**
Van olyan **nemdeterminisztikus** algoritmus, mely **logaritmikus tárban** kiszámítja az input gráf megadott csúcsából elérhető csúcsok számát
következmény: 
- $NSPACE(f(n)) = coNSPACE(f(n)).$
- $NL = coNL$

**Egyéb infók:**
L $\subseteq$ NL (részhalmaza, vagy egyenlő vele)

Elérhetőség megoldható **lineáris** tárban: Szélességi keresés algotimus egy $N$-csúcsú gráf esetén két, egyenként legfeljebb $N$ méretű csúcshalmazt tárol. Ezt pl egy $N$ hosszú bitvektor alkalmazásával egy-egy regiszterben $O(N)$ tárban megoldható.