
# 10.Normálformák az elsőrendű logikában. Egyesítési algoritmus. Következtető módszerek: Alap rezolúció és elsőrendű rezolúció, ezek helyessége és teljessége
**Elsőrendű logika szintaxis:**
*Elsőrendű változók:* $x, y, z, ..., x_1,y_5...$
*Függvényjelek:* $f,g,...,f_1,g_5...$
*Predikátumjelek:* $p,q,r,...,p_1...$
*Konnektívák:* $\lor, \wedge, \neg, \leftrightarrow, \rightarrow$
*Kvantorok:* $\forall, \exists$
*Logikai konstansjelek:* $\downarrow, \uparrow$

## Normálformák predikátumkalkulusban
Formulákkal dolgozni tudjunk, úgy nevezett **zárt Skolem** alakra kell hozni

1. Nyilak eliminálása
2. Kiigazítás (Változó név ütközés elkerülés)
	- Különböző kvantorok különböző változókat kötnek
	- Nincs olyan változó, amely szabadon ($\exists$) és kötötten ($\forall$) is előfordul
	- Indexelés
3.  Prenex alakra hozás
	- Kvantorokat az elejére szervezzük.
4. Skolem alakra hozás
	- Összes kvantor elől és mindegyik $\forall$
	- Töröljük $\exists$ változókat (pl $\exists x$)
	- A magbeli törölt változók helyére mindenhova $f(x_1,..x_n)$ kerül, ahol $f$ egy **új függvényjel**
5. Lezárás
	- Ne maradjon szabad változó-előfordulás
	- A szabad változó helyére, berakunk egy *új* konstans szimbólumot.

## Egyesítési algoritmus

Ha F egy formula, akkor F\[x/t\] azt jelenti, hogy F-ben x összes előfordulását helyettesítjük t-vel.

Ha $x_1, x_2, ..., x_n$ **változók**, és $t_1, ..., t_n$ **termek**, akkor az \[x1/t1\], ..., \[xn/tn\] helyettesítés azt jelenti, hogy először $x_1$ helyére írunk $t_1$-et, aztán az eredményben $x_2$ helyére $t_2é-t, stb.

Formulák halmazaira, pl klózokra is értelmezhetjük ezt.

Klóz végzett helyettesítésnél \[x/t\] azt jelenti, hogy minden klózra elvégezzük az x helyére t helyettesítést, és az eredményeket visszapakoljuk egy halmazba.
Ha $C={l_1, l_2, ..., l_n}$ **literálok halmaza**, akkor $s$ a $c$ egyesítője, ha $l_1$\*s = ... = $l_n$\*s.
C-re akkor mondjuk, hogy egyesíthető, ha van egyesítője.

Az s helyettesítés általánosabb az s' helyettesítésnél, ha van olyan s" helyettesítés, hogy s\*s" = s'.

Egyesítési algoritmus:

- input: C klóz
- output: C legáltalánosabb helyettesítője, ha egyesíthető, különben azzal tér vissza, hogy nem egyesíthető
- veszünk két literált, és keressük az első eltérést
- ha az egyik helyen egy x változó áll, a másikon egy t term, amiben nincs x, akkor x/t és vissza az előző pontra
- különben return nem egyesíthető

Nem egyesíthető pl

- ha f(x) és c a különbség a két literál azonos pontján
- ha x és f(x) a különbség
- ha g(x) és f(x) a különbség

## Alap rezolúció
Azért ALAP mert **alap termek** vannak benne.
($E(\Sigma$): Klózok herbrand kiterjesztése)
- **input:** elsőrendű formulák egy $\Sigma$ halmaza
- **output:** kielégíthetetlen véges sok lépésben, vagy kielégíthető véges sokban vagy végtelen ciklus
- Módszer:
	- $\Sigma$ elemeit zárt skolem alakra hozzuk, a formula belsejét pedig CNF-re, ez legyen $\Sigma'$
	- ekkor $E(\Sigma'$) a klózok **alap példányainak** a halmaza
	- $E(\Sigma'$)-n futtatjuk az ítéletkalkulusbeli rezolúciós algoritmust
	- általában végtelen sok alapterm van
- vegyük fel $E(\Sigma'$) egy elemét, és rezolváljunk vele, amíg lehet
- ha kijön az üres klóz, akkor jók vagyunk, ha nem, generálunk tovább

**Helyesség és teljesség:**
$üresklóz \in Res^*(E(\Sigma'))$, ha $\Sigma \vDash \downarrow$, **AZAZ, HA letudjuk vezetni az üresklózt akkor kielégíthetetlen, és fordítva**

**Bizonyításra pár bulletpoint:**
1. Zárt Skolem alakra hozás az s-ekvivalens átalakítás, azaz ha $\Sigma$ pontosan akkor kielégíthetetlen,ha $\Sigma'$ is
2. Herbrand-tétel következménye, hogy $\Sigma'$ pontosan akkor kielégíthetetlen ha $E(\Sigma')$ az


## Elsőrendű rezolúció

- **input:** elsőrendű formulák egy szigma halmaza
- **output:** kielégíthetetlen-e?
- $\Sigma$ zárt skolemre, mag cnfre, $\Sigma'$
- $\Sigma'$ elemeit közvetlenül felvehetjük a listára
- ha kijön az üres klóz, kielégíthetetlen
- ha nem tudunk több klózt levezetni, kielégíthető


Rezolvensképzés:

- C1 és C2 klózokat akarjuk rezolválni
- átnevezzük a változókat úgy, hogy ne legyen közös változó C1-ben és C2-ben
- kiválasztunk C1-ből és C2-ből is literálokat, az egyikből pozitívokat, a másikból negatívokat
- ezeket pozitívan belepakoljuk egy C halmazba
- ha C egyesíthető egy s helyettesítéssel, akkor vehetjük a rezolvensét C1-nek és C2-nek
- elmentjük s-t
- vesszük C1-ből és C2-ből a maradék literálokat, és berakjuk egy halmazba
- ezen a halmazon elvégezzük az s helyettesítést, ez lesz a rezolvens

**Helyesség és teljesség:**
Az elsőrendű klózok $\Sigma$ halmaza pontosan akkor **kielégíthetetlen**, ha $üresklóz \in Res^*(\Sigma)$ (levezethető az üresklóz $\Sigma$ az elsőrendű rezoluciós algoritmussal)

**Bizonyításra pár bulletpoint:**
1. Helyesség:
	-  Kijöhet az üres klóz, akkor $\Sigma$ kielégíthetetlen, rezolvensképzés helyességéből következik.
2. Teljesség:
	- Ha $\Sigma$ kielégíthetetlen, akkor az üres klóznak vanegy $C_1', ... , C_n' = üresklóz$ alaprezolúciós levezetése.