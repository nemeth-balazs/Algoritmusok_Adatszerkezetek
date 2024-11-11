# Rekurzióval megoldható feladatok
## Feladat megnevezése: [Concert Tickets](https://cses.fi/problemset/task/1091/)

Van n darab koncertjegy, mindegyiknek van egy adott ára. Ezután m vásárló érkezik, egymás után. Minden vásárló megmondja a maximális árat, amit hajlandó fizetni egy jegyért, és ezután kap egy jegyet, amelynek ára a lehető legközelebb van a megadott maximális árhoz úgy, hogy ne lépje túl azt.

**Bemenet:**

Az első bemeneti sor tartalmazza az n és m egész számokat: a jegyek és a vásárlók számát.

A következő sor n egész számot tartalmaz, h<sub>1</sub>, h<sub>2</sub>..., h<sub>n</sub>: az egyes jegyek ára.

Az utolsó sor m egész számot tartalmaz, t<sub>1</sub>, t<sub>2</sub>..., t<sub>n</sub>: a vásárlók által megadott maximális árak a beérkezésük sorrendjében.

**Kimenet:**

Minden vásárló esetén írd ki, hogy milyen áron vásárolja meg a jegyet. Ezután az adott jegy nem vásárolható meg újra.
Ha egy vásárló nem tud jegyet vásárolni, akkor írd ki, hogy -1.

**Feltételek:**

- 1 <= n, m <= 2*10<sup>5</sup>
- 1 <= h<sub>i</sub>, t<sub>i</sub> <= 10<sup>9</sup>

**Példa:**

Bemenet:  
5 3  
5 3 7 8 5  
4 8 3

Kimenet:  
3  
8  
-1