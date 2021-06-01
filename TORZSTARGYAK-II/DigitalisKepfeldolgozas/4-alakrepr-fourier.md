# 4. Alakreprezentáció, határ- és régió-alapú alakleíró jellemzők, Fourier leírás

## Alakreprezentáció

Az alak/forma megítélésének fontos szerep jut a látásunkban.
Az alak (shape) nem bír egzakt matematikai definícióval

A szegmentálást
követően az objektumok kontúrjaiból vagy foltjaiból (attól függően, hogy határ- vagy
régió-alapú szegmentálást vetettünk-e be) számos alakleíró jellemzőt vonhatunk ki.
Hangsúlyozandó, hogy itt már elszakadhatunk a digitális képektől, némelyik jellemző
csak egy szám, mások pedig összetett struktúrák is lehetnek.

Az alakleíró jellemzőket három osztályba soroljuk.

### Határ alapú alakleíró jellemzők

Freeman féle lánckód

- 4 vagy 8 szomszédok felé mutató vektort sorszámozza
- óramutató járásával ellentétes irányban növekszik
- kiválaszt a kontúron egy kezdőpontot
- egymás után írja a kontúrt körbekötő vektorok sorszámait
- a kontúr leírható egy négyes vagy nyolcas számrendszerbeli számmal, ez a lánckód

