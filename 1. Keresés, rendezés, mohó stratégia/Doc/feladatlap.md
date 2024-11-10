# Keresés, rendezés, mohó stratégia
## Feladat megnevezése: [Ferris Wheel](https://cses.fi/problemset/task/1090/)

Van n gyerek, akik fel szeretnének ülni egy óriáskerékre, és a feladatod, hogy minden gyerek számára találj egy gondolát.

Minden gondolában legfeljebb egy vagy két gyerek ülhet, és a gondola összsúlya nem haladhatja meg az x-et. Ismered minden gyerek súlyát.

Mi a minimálisan szükséges gondolák száma ahhoz, hogy az összes gyerek fel tudjon ülni?

**Bemenet:**

Az első sor két egész számot tartalmaz: n (a gyerekek száma) és x (a maximálisan megengedett súly egy gondolában).

A következő sor n darab egész számot tartalmaz, amelyek a gyerekek súlyait jelölik: p<sub>1</sub>, p<sub>2</sub>,..., p<sub>n</sub>.

**Kimenet:**

Írj ki egy egész számot, amely a minimálisan szükséges gondolák számát jelenti.

**Feltételek:**

- 1 <= n <= 2*10<sup>5</sup>
- 1 <= x <= 10<sup>9</sup>
- 1 <= p<sub>i</sub> <= x

**Példa:**

Bemenet:  
4 10  
7 2 3 9

Kimenet:  
3