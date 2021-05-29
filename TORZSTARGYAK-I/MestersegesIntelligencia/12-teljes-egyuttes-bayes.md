# 12. Teljes együttes eloszlás tömör reprezentációja, Bayes hálók. Gépi tanulás: felügyelt tanulás problémája, döntési fák, naiv Bayes módszer, modellillesztés, mesterséges neuronhálók, k-legközelebbi szomszéd módszere

## Teljes együttes eloszlás tömör reprezentációja, Bayes hálók

### Teljes együttes eloszlás

Minden lehetséges eseményre tudjuk annak a valószínűségét. Pl van 3 logikai típusú véletlen változónk, akkor összesen 2^3=8-féle eset lehet ezekre. A teljes együttes eloszlásnál mind a 8 esetnek tudjuk a valószínűségét.

### Tömör reprezentáció

A kijelentések függetlensége a legfontosabb tulajdonság a teljes együttes eloszlás tömöríthetőségéhez. Van függetlenség, és feltételes függetlenség.

Függetlenség
a és b kijelentések függetlenek, ha P(a és b) = P(a)*P(b)

A függetlenség struktúrát takar. Ha pl n logikai változónk van, amik két független részhalmazra oszthatók m és k mérettel, akkor a 2^n valószínűség tárolása helyett elég 2^m+2^k valószínűséget tárolni, ami sokkal kevesebb lehet.

Extrém esetben, ha pl. az A1,..., An diszkrét változók kölcsönösen függetlenek (tetszőleges két részhalmaz független), akkor csak O(n) értéket kell tárolni, mivel ez esetben

P(A1,..., An) = P(A1)...P(An)

Feltételes függetlenség
a és b kijelentések feltételesen függetlenek c feltevésével, akkor és csak akkor, ha P(a és b | c) = P(a|c)*P(b|c). Tipikus eset, ha a és b közös oka c.

Naiv-Bayes szabály
Ha A feltevése mellett B1,...,Bn kölcsönösen függetlenek, akkor 
P(B1, . . . , Bn|A) = Produktum^n_i=1 P(Bi|A)

### Bayes hálók

A feltételes függetlenség hasznos, mert tömöríthetjük a teljes együttes eloszlást.