# Dinamikus programozási feladat
## Feladat megnevezése: [Book Shop](https://cses.fi/problemset/task/1158/)

Egy könyvesboltban vagy, amely n különböző könyvet árul. Minden könyv árát és oldalszámát ismered.

Úgy döntöttél, hogy a vásárlásod teljes ára legfeljebb x lesz. Mi a maximális oldal szám, amit megvásárolhatsz? Minden könyvet legfeljebb egyszer vásárolhatsz meg.

**Bemenet:**

Az első bemeneti sor két egész számot tartalmaz: n és x: a könyvek száma és a maximálisan megengedett összes ár.

A következő sor n egész számot tartalmaz: h<sub>1</sub>, h<sub>2</sub>, ..., h<sub>n</sub>: az egyes könyvek ára.

Az utolsó sor n egész számot tartalmaz: s<sub>1</sub>, s<sub>2</sub>, ..., s<sub>n</sub>: az egyes könyvek oldalszáma.

**Kimenet:**

Írj ki egy egész számot: a maximális oldalszámot.

**Feltételek:**

- 1 <= n <= 1000
- 1 <= x <= 10<sup>5</sup>
- 1 <= h<sub>i</sub>,s<sub>i</sub> <= 1000

**Példa:**

Bemenet:  
4 10  
4 8 5 3  
5 12 8 1

Kimenet:  
13  

Magyarázat: Megvásárolhatod az 1-es és a 3-as könyvet. Az áruk 4+5=9, és az oldalszámuk 5+8=13.