# 6. A környezetfüggetlen nyelvtan és nyelv definíciója. Derivációk és derivációs fák kapcsolata. Veremautomaták és környezetfüggetlen nyelvtanok ekvivalenciája. A Bar-Hillel lemma és alkalmazása


## A környezetfüggetlen nyelvtan és nyelv definíciója

Egy G=(N, SZIGMA, P, S) nyelvtan, környezetfüggetlen, ha minden szabálya A -> alfa alakú, ahol alfa egy terminálisokból és nemterminálisokból álló szó.

Egy nyelv környezetfüggetlen, ha van olyan CF nyelvtan, ami őt generálja.

## Derivációk és derivációs fák kapcsolata

Korlátozás nélküli deriváció

- bármely nemterminális helyére helyettesíthetünk

Bal/jobboldali deriváció

- csak a legbal/jobboldalabbi nemterminálisba helyettesíthetünk

Derivációs fák

Mindig csak egy gyökere van

- vagy csak a gyökérből áll
- vagy van egy epszilon gyerek
- vagy kiindul belőle k darab él, amelyek végpontjai további derivációs fák gyökerei

Legyen t egy derivációs fa, gyökere X
t magassága h(t)
t határa fr(t) - határ kb a levelek balról jobbra olvasva

Derivációs fák kapcsolata a derivációkkal

Tetszőleges X gyökerű derivációs fára és alfa szóra X-ből akkor vezethető le alfa, ha van olyan X gyökerű derivációs fa, amelyre fr(t) = alfa

## Veremautomaták és környezetfüggetlen nyelvtanok ekvivalenciája

### Veremautomata

Veremautomatának nevezzük azt a P= (Q,Σ,Γ,δ,q0,Z0,F), ahol

- Q: állapotok halmaza
- Σ: input abc
- Γ: verem abc
- q0 eleme Q: kezdőállapot
- Z0: verem kezdőszimbólum
- F: végállapotok halmaza
- δ: átmenetfüggvény

Az átmenet a következőképpen történik: ha az automata a q állapotban van, a szimbólum érkezik és Z van a verem tetején, akkor átmegy a q_i állapotba, a veremben pedig Z helyére alfa_i kerül. Az átmenetnél az automata kiolvas egy betűt az inputból, leveszi Z-t a verem tetejéről, és tetszőleges hosszú szót odaír a helyére.

Egy szó elfogadása történhet végállapotokkal, vagy üres veremmel is. Ugyanazon automatánál általában nem egyezik meg az üres veremmel és a végállapotokkal felismert nyelv.

### Ekvivalencia

Minden környezetfüggetlen nyelvtanhoz meg lehet adni veremautomatát úgy, hogy a veremautomata (üres veremmel vagy végállapottal) ugyanazt a nyelvet ismeri fel, amit a környezetfüggetlen nyelvtan generál.

A bizonyításhoz egy környezetfüggetlen nyelvtanhoz konstruálunk egy egyállapotos nemdeterminisztikus veremautomatát, ami üres veremmel ismeri fel a szavakat. A veremabc legyen a nemterminálisok unió terminálisok. Ezzel a veremautomatával szimuláljuk a nyelvtan levezetéseit. Tudjuk továbbá, hogy az üres veremmel és a végállapotokkal felismert nyelvek halmaza ugyanaz, így ez az állításunk igaz lesz.

Minden veremautomatával felismert nyelv környezetfüggetlen.

Itt pedig veremautomatához adunk meg egy környezetfüggetlen nyelvtant.

Lásd pdf 2.

## Bar-Hillel lemma és alkalmazása

Tulajdonképpen pumpáló lemma CF nyelvekre

Ha L egy környezetfüggetlen nyelv, akkor létezik egy nyelvtől függő k szám, amire ha egy L-beli szó hossza nagyobb k-nál, akkor feldarabolható 5 részre, amikre a következők teljesülnek:

- |w2w3w4| <= k
- w2w4 nem epszilon
- minden n >= 0-ra w1w2^nw3w4^nw5 eleme L-nek

Alkalmazás: az L={a^nb^nc^n|n≥1} nyelv nem környezetfüggetlen.

Tegyük fel, hogy igen, ekkor léteznie kell olyan k számnak, amire teljesülnek a Bar-Hillel lemmában a feltételek.

Vegyük az a^kb^kc^k szót, aminek hossza 3k >= k, tehát jó lesz fixen.

A lemma szerint ennek létezik w1w2w3w4w5 felbontása, melyre w2w4 nem epszilon, és minden n >= 0-ra w1w2^nw3w4^nw5 eleme a nyelvnek.

Nézzük ekkor mi lehet w2-ben és w4-ben! Egyik sem tartalmazhat két betűt, mert ekkor pl ha kétszer vesszük w2-t és w4-et, akkor a betűk sorrendje nem abc lesz. Tehát biztosan csak egyféle betűt tartalmaznak. Ekkor a w1w2^2w3w4^2w5 szóbal legalább egy, és legfeljebb két betű száma több, mint a többi betűé, tehát biztos nem eleme ez a szó L-nek.
