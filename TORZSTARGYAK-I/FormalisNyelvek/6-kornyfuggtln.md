
# 6. A környezetfüggetlen nyelvtan és nyelv definíciója. Derivációk és derivációs fák kapcsolata. Veremautomaták és környezetfüggetlen nyelvtanok ekvivalenciája. A Bar-Hillel lemma és alkalmazása

## Alapfogalmak, jelölések
**Ábécé:** Szimbólumok egy tetszőleges véges, nemüres halmaza jele: $\Sigma$
-	$\Sigma^*$: Az összs szavak + $\epsilon$
- $\Sigma^+$: Az összes szavak, kivéve az $\epsilon$
- $\Sigma$ **ábécé feletti szó:** egy $a_1,...,a_k$ alakú sorozat.
- **Nyelv:** $\Sigma^*$ tetszőleges $L$ részhalmazát egy $\Sigma$ feletti **nyelvnek** nevezzük. Ha $L$ véges számú szóból áll, akkor **véges nyelvnek nevezzük*
- **Nyelvtan:** Könnyen leírható eszköz, amely alkalmas nyelvek megadására. Effektíve nyelveket tuduk vele reprezentálni.
	- PL Környezetfüggetlen: $G = (N, \Sigma, P, S)$, ahol
		- N egy ábécé
		- $\Sigma$ egy ábécé, terminális
		- $S\in N$ kezdő szimbólum
		- $P$ pedig egy $A\rightarrow \alpha$ alakú átírási szabály.

## A környezetfüggetlen nyelvtan és nyelv definíciója

Egy $G=(N, \Sigma, P, S)$ **nyelvtan**, környezetfüggetlen, ha minden szabálya $A \rightarrow \alpha$ alakú, ahol $\alpha$ egy **terminálisokból** és **nemterminálisokból** álló szó.

Egy **nyelv környezetfüggetlen, ha van olyan CF nyelvtan, ami őt generálja.**

## Derivációk és derivációs fák kapcsolata

**Korlátozás nélküli deriváció**
- bármely nemterminális helyére helyettesíthetünk

**Bal/jobboldali deriváció**
- csak a legbal/jobboldalabbi nemterminálisba helyettesíthetünk

pl: Bal oldali
$\underline{K} \Rightarrow \underline{T} \Rightarrow \underline{T}*F \Rightarrow \underline{F}*F$ 
Vegyes:
$\underline{K} \Rightarrow \underline{T} \Rightarrow \underline{T}*F \Rightarrow F*\underline{F}$ 

**Derivációs fák:**
**Mindig csak egy gyökere van** 
- vagy csak a gyökérből áll
- vagy van egy epszilon gyerek
- vagy kiindul belőle k darab él, amelyek végpontjai további derivációs fák gyökerei

**Gyökere** mindig egy **terminális-** vagy egy **nemterminális szimbólum**. Az elágazások pedig megfelelnek a nyelvtan szabályainak.

Legyen $t$ egy derivációs fa, gyökere $X$
$t$ magassága $h(t)$
$t$ határa $fr(t)$ - **határ kb a levelek balról jobbra olvasva**

**Derivációs fák kapcsolata a derivációkkal**
Tetszőleges $X$ gyökerű derivációs fára és $\alpha$ **szóra** $X$-ből akkor vezethető le $\alpha$, ha van olyan $X$ gyökerű derivációs fa, amelyre $fr(t) = \alpha$

## Veremautomaták és környezetfüggetlen nyelvtanok ekvivalenciája

### Veremautomata

Veremautomatának nevezzük azt a P= (Q,Σ,Γ,δ,q0,Z0,F), ahol

- Q: állapotok halmaza
- $\Sigma$: input abc
- $\Gamma$: verem abc
- $q_0$ eleme Q: kezdőállapot
- $Z_0$: verem kezdőszimbólum
- F: végállapotok halmaza
- $\delta$: átmenetfüggvény

**Az átmenet a következőképpen történik:**
 - ha az **automata a q állapotban van**, a szimbólum érkezik és **Z van a verem tetején**, akkor átmegy a $q_i$ **állapotba**, a **veremben pedig Z helyére $\alpha_i$ kerül**. 
 - Az **átmenetnél az automata kiolvas egy betűt az inputból**, leveszi **Z-t a verem tetejéről**, és tetszőleges hosszú szót odaír a helyére.

Egy szó elfogadása történhet végállapotokkal, vagy üres veremmel is. Ugyanazon automatánál általában nem egyezik meg az üres veremmel és a végállapotokkal felismert nyelv.

### Ekvivalencia

Tétel: Minden CF nyelv felismerhető PDA-val.

**Minden környezetfüggetlen nyelvtanhoz meg lehet adni veremautomatát úgy, hogy a veremautomata (üres veremmel vagy végállapottal) ugyanazt a nyelvet ismeri fel, amit a környezetfüggetlen nyelvtan generál.**

A bizonyításhoz egy környezetfüggetlen nyelvtanhoz konstruálunk egy egyállapotos nemdeterminisztikus veremautomatát, ami **üres veremmel ismeri fel a szavakat.** **A verem abc legyen a nemterminálisok unió terminálisok**. 
Ezzel a veremautomatával szimuláljuk a nyelvtan levezetéseit. Tudjuk továbbá, hogy az üres veremmel és a végállapotokkal felismert nyelvek halmaza ugyanaz, így ez az állításunk igaz lesz.

Itt pedig veremautomatához adunk meg egy környezetfüggetlen nyelvtant.

Lásd pdf 2.

## Bar-Hillel lemma és alkalmazása

**Tulajdonképpen pumpáló lemma CF nyelvekre**

Ha L egy környezetfüggetlen nyelv ($L \subseteq \Sigma^*$), akkor létezik egy nyelvtől függő **k** szám, amire ha egy **L-beli szó hossza nagyobb k-nál**, akkor feldarabolható 5 részre, amikre a következők teljesülnek.
Ha $L \subseteq \Sigma^*$ nyelv környezetfüggetlen, akkor
- Megadható olyan ($L$ től függő) $k > 0$ egész szám,
- Hogy minden $w \in L$ szóra, ahol $|w| \ge k$,
- létezik olyan $w = w_1w_2w_3w_4w_5$ felbontás, amelyre igazak a következő állítások:
	1. $|w_2w_4| > 0$ és $|w_2w_3w_4| \le k$
	2. Minden $n \ge 0$--ra $w_1w_2^nw_3w_4^nw_5 \in L$



Alkalmazás: az $L={a^nb^nc^n|n≥1}$ nyelv nem környezetfüggetlen.

**Tegyük fel, hogy igen, ekkor léteznie kell olyan k számnak, amire teljesülnek a Bar-Hillel lemmában a feltételek.**

Vegyük az $a^kb^kc^k$ szót, aminek hossza $3k >= k$, tehát **jó lesz fixen**.

A lemma szerint ennek létezik $w_1w_2w_3w_4w_5$ felbontása, melyre $w_2w_4$ nem epszilon, és minden $n >= 0$-ra $ $w_1w_2^nw_3w_4^nw_5$ eleme a nyelvnek.

Nézzük ekkor mi lehet **w2-ben és w4-ben**! Egyik sem tartalmazhat két betűt, mert ekkor pl ha kétszer vesszük w2-t és w4-et, akkor a betűk sorrendje nem abc lesz. Tehát biztosan csak egyféle betűt tartalmaznak. Ekkor a $w_1w_2w_3w_4w_5$ szóbal legalább egy, és legfeljebb két betű száma több, mint a többi betűé, tehát biztos nem eleme ez a szó L-nek.
