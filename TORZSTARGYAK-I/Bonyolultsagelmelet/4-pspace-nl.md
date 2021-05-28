# 4. A PSPACE osztály. PSPACE-teljes problémák. Logaritmikus tárigényű visszavezetés. NL-teljes problémák

## PSPACE osztály

Savitch-tétel

- Elérhetőség eldönthető O(log^2n) tárban

Az f(n) tárban nemdeterminisztikusan eldönthető problémák mind eldönthetők determinisztikusan, f^2(n) tárban is

Tehát: NSPACE(f(n)) részhalmaza SPACE(f^2(n))-nek
és mivel polinom négyzete polinom
PSPACE = NPSPACE

Polinom tárban (det. vagy nemdet.) eldönthető problémák osztálya

## PSPACE-teljes problémák

QSAT PSPACE-teljes

QSAT (kvantifikált SAT)

- adott egy ítéletkalkulusbeli logikai formula, változó kvantorokkal az elején (létezik, bármely, létezik, bármely stb)
- magja CNF alakú, kvantormentes
- igaz-e ez a formula?

QSAT mint kétszemélyes játék

- input ugyanaz
- van-e az első játékosnak nyerő stratégiája abban a játékban, ahol:
- - a játékosok sorban értéket adnak a változóknak, első játékos x1-nek, második x2-nek stb
- - ha a formula igaz lesz, az első játékos nyert, ha hamis, akkor a második
- ez ugyanaz tkp, mint a sima QSAT, szóval ez is PSPACE-teljes

hasonlít a minimaxra
az éses csúcsoknál lévő játékos minimalizál

Földrajzi játék

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

## Logtáras visszavezetés

Polinomidejű visszavezetés túl erős, ha pl P-beli problémákat akarunk egymáshoz viszonyítani, mert egy polinomidejű visszavezetés alatt már akár meg is oldhatnánk egy P-beli problémát

Logtáras visszavezetés

f egy olyan függvény, hogy

- A inputjaiból B inputjait készíti
- választartó módon
- és logaritmikus tárban kiszámítható

akkor f egy logtáras visszavezetés A-ról B-re.
