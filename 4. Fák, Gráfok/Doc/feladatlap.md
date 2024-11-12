# Fák, Gráfok feladat
## Feladat megnevezése: [Building Roads](https://cses.fi/problemset/task/1666/)

Bytelandban n város és m út található közöttük. A cél új utak építése, hogy bármely két város között legyen útvonal.
A feladatod, hogy megállapítsd a minimálisan szükséges utak számát, valamint hogy mely utakat kell megépíteni.

**Bemenet:**

Az első bemeneti sor két egész számot tartalmaz, n és m: a városok és az utak számát. A városok számozása 1, 2, ..., n.

Ezt követően m sor található, amelyek az utakat írják le. Minden sor két egész számot tartalmaz, a és b: van egy út ezen városok között.

Egy út mindig két különböző várost köt össze, és legfeljebb egy út van bármely két város között.

**Kimenet:**

Először írj ki egy egész számot, k-t: a szükséges új utak számát.

Ezután írj ki k sort, amelyek az új utakat írják le. Bármely érvényes megoldás elfogadható.

**Feltételek:**

- 1 <= n <= 10<sup>5</sup>
- 1 <= m <= 2x10<sup>5</sup>
- 1 <= a, b <= n

**Példa:**

Bemenet:  
4 2  
1 2  
3 4  

Kimenet:  
1  
2 3