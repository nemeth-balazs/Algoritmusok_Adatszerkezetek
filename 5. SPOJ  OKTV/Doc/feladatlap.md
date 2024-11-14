# SPOJ feladat
## Feladat megnevezése: [DISQUERY - Distance Query](https://www.spoj.com/problems/DISQUERY/)

Az ország közlekedési hálózata N városból (amelyeket 1-től N-ig terjedő egész számokkal jelölnek) és N-1 útból áll, amelyek összekötik a városokat. Minden két különböző város között egyedi útvonal van, és tudjuk minden egyes út pontos hosszát.

Írj egy programot, amely a megadott K várospár mindegyikére meghatározza az útvonalon lévő legrövidebb és leghosszabb út hosszát.

**Bemenet:**

A bemenet első sora egy N egész számot tartalmaz, ahol 2 <= N <= 100 000. Az ezt követő N-1 sor mindegyike három egész számot tartalmaz: A, B és C, ami azt jelenti, hogy van egy C hosszúságú út A és B városok között.

Minden út hossza egy pozitív egész szám, amely legfeljebb 1 000 000 lehet.
A következő sor egy K egész számot tartalmaz, ahol 1 <= K <= 100 000. Az ezt követő K sor mindegyike két különböző egész számot tartalmaz: D és E – ezek egy-egy lekérdezésként szolgáló városok címkéi.

**Kimenet:**

A kimenet K sora mindegyike két egész számot kell tartalmazzon – a feladatleírás szerinti hosszértékeket az adott várospárra.

**Példa:**

Bemenet:  
5  
2 3 100  
4 3 200  
1 5 150  
1 3 50  
3  
2 4  
3 5  
1 2  

Kimenet:  
100 200  
50 150  
50 100  

**Példa:**

Bemenet:  
7  
3 6 4  
1 7 1  
1 3 2  
1 2 6  
2 5 4  
2 4 4  
5  
6 4  
7 6  
1 2  
1 3  
3 5  

Kimenet:  
2 6  
1 4  
6 6  
2 2  
2 6   
