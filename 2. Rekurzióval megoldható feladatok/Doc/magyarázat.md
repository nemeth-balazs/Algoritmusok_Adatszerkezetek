# Rekurzióval megoldható feladatok
## Feladat megnevezése: [Concert Tickets](https://cses.fi/problemset/task/1091/)

- Az algoritmus implementálása: Source/ConcertTickets.py

**Osztály áttekintése: ConcertTickets**

A ConcertTickets osztály feladata, hogy a koncertjegyeket és a vásárlók ajánlatait kezelje, és meghatározza az egyes vásárlók által megvásárolható jegyeket az ajánlataik alapján. Az osztály fő logikája a Calculate() metódusban található, amely a jegyeket sorba rendezi, majd egy bináris keresésre épülő megközelítést alkalmaz annak érdekében, hogy gyorsan megtalálja a legközelebbi megfelelő árú jegyet minden vásárló számára.

**Osztály adattagjai:**  
- _numberOfTickets: Az elérhető koncertjegyek száma.
- _numberOfCustomer: A vásárlók száma.
- _arrTicketPrices: Lista, amely a jegyek árait tartalmazza.
- _arrCustomerOffers: Lista, amely a vásárlók által kínált árakat tartalmazza.

**Konstruktor (`__init__`):**   

A konstruktor négy paramétert vár:

- numberOfTickets: A jegyek száma.
- numberOfCustomer: A vásárlók száma.
- arrTicketPrices: A jegyek árait tartalmazó lista.
- arrCustomerOffers: A vásárlói ajánlatokat tartalmazó lista.

Az adattagokat inicializálja a megadott paraméterekkel.

**checkParameters() metódus:**

Ez a metódus ellenőrzi, hogy a bemeneti paraméterek megfelelnek-e az előírt határértékeknek és feltételeknek. Ha bármely paraméter érvénytelen, a metódus False értéket ad vissza, ellenkező esetben pedig True-t. Az ellenőrzési szempontok a következők:

- A jegyek és a vásárlók száma megfelelő tartományban van-e.
- Az egyes listák hosszúsága megegyezik-e a jegyek és vásárlók számával.
- Az ajánlati és jegyárak érvényes tartományban vannak-e.

**Calculate() metódus**

A jegyárak rendezése és a vásárlói ajánlatokhoz való párosítása "Oszd meg és uralkodj" típusú keresési algoritmust használ a findBestFitRecursive rekurzív függvényen keresztül. Ennek eredményeként az algoritmus gyorsabban tudja megtalálni a legmegfelelőbb jegyárakat a vásárlói ajánlatokhoz képest, mint ha szekvenciálisan keresne

Az algoritmus lépései a következők:

**Működési elv:** 

1. Jegyárak rendezése: A jegyek árai növekvő sorrendbe kerülnek, így a bináris keresés segítségével gyorsabban meg lehet találni a megfelelő árú jegyet.
2. Ajánlatok feldolgozása:
   - Minden vásárlói ajánlat esetén meghatározza a megfelelő jegyet a findBestFitRecursive() függvény segítségével.
   - Ha található egy megfelelő jegy, amely ára kisebb vagy egyenlő a vásárló ajánlatával, azt eltávolítja a listából, és hozzáadja az eredmények listájához. Ha nem található megfelelő jegy, -1-et ad hozzá.

A függvény végül egy olyan listát ad vissza, amely minden vásárló számára megmutatja a kapott jegy árát, vagy -1-et, ha nincs elérhető jegy.

**findBestFitRecursive() függvény**  

A findBestFitRecursive() függvény egy rekurzív bináris keresési algoritmus, amely a rendezett jegyárak listájában keresi a megadott vásárlói ajánlatnak megfelelő legnagyobb értéket. A függvény működése:

- Az algoritmus mindig az aktuális intervallum középső elemét vizsgálja.
- Ha a középső elem ára kisebb vagy egyenlő a vásárlói ajánlattal és az intervallum már csak egy elemre szűkült, visszatér az indexével.
- Ha a középső elem nagyobb, az algoritmus az intervallum bal oldalán folytatódik, különben a jobb oldalon.

Ez a keresési módszer hatékonyabbá teszi a jegyek keresését a nagyobb adathalmazokon, és csökkenti az algoritmus futási idejét.


**Összefoglalás**  

A ConcertTickets osztály célja, hogy hatékony megoldást nyújtson egy kereslet-kínálat típusú problémára, ahol adott vásárlói ajánlatok alapján próbálunk eladni egy koncertre szóló jegykészletet.
## Tesztelés: ##

- Tesztrendszer: Source/File_test.py  
- Tesztfájlok: Tests/input és Tests/output

A ConcertTickets osztály tesztelése során célunk annak ellenőrzése, hogy az algoritmus helyesen párosítja-e a vásárlói ajánlatokat a jegyek áraival, és visszatér-e a megfelelő eredményekkel minden lehetséges bemenetre. A tesztelés két fő lépésből áll:

**Bemeneti paraméterek ellenőrzése:**

- Az osztály checkParameters() metódusa ellenőrzi a bemenetek helyességét, és kizárja azokat az eseteket, amelyek kívül esnek a megadott tartományokon vagy hiányosak.
- Így a tesztelés során validáljuk, hogy az osztály helyesen szűri-e ki az érvénytelen bemeneteket, és csak azokat engedi tovább, amelyek megfelelnek az előírt feltételeknek.

**Jegyek és vásárlók párosítása:**

- Az Calculate() metódus logikáját tesztfájlokkal ellenőrizzük, amelyek különböző méretű és összetételű bemeneteket tartalmaznak, beleértve a minimális és maximális értékeket, valamint olyan eseteket is, ahol nincsenek megfelelő jegyek az ajánlatokhoz.
- Az algoritmus által visszaadott jegyárakat összehasonlítjuk az előre definiált helyes kimeneti értékekkel.
- Minden teszt esetben ellenőrizzük, hogy a Calculate() metódus visszatérési értékei megegyeznek-e a várt eredményekkel, és megfelelően kezeli-e a különböző forgatókönyveket.

A tesztelési folyamat így biztosítja, hogy az osztály robusztus és pontos legyen minden bemeneti esetben, különös tekintettel a hatékonyságra és helyes eredményekre a jegyek és ajánlatok párosítása során.