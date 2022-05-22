
# 4. A PSPACE osztály. PSPACE-teljes problémák. Logaritmikus tárigényű visszavezetés. NL-teljes problémák

## PSPACE osztály = $Space(n^k)$
Polinom tárban (det. vagy nemdet.) eldönthető problémák osztálya.
**Savitch-tétel**: Az $f(n)$ tárban nemdeterminisztikusan eldönthető problémák mind eldönthetők determinisztikusan, $f^2(n)$ tárban is
Tehát: $NSPACE(f(n))$ részhalmaza $SPACE(f^2(n))$-nek és mivel polinom négyzete polinom $\rightarrow$ PSPACE = NPSPACE
+Elérhetőség eldönthető O(log^2n) tárban

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
- - az első játékos kezd, lerakja a bábut a kezdőcsúcsra
- - felváltva lépnek
- - egy olyan csúcsba kell húzni a bábut, ami egy lépésben elérhető, és ahol még nem voltak
- - aki először nem tud lépni, vesztett

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


**Egyéb infók:**
L $\subseteq$ NL (részhalmaza, vagy egyenlő vele)
