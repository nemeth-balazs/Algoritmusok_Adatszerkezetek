# Keresés, rendezés, mohó stratégia feladat
## Feladat megnevezése: [Ferris Wheel](https://cses.fi/problemset/task/1090/)

- Az algoritmus implementálása: Source/FerrisWheel.py

**Osztály áttekintése: FerrisWheel**

A FerrisWheel osztály célja annak megállapítása, hogy minimálisan hány fordulóra van szükség ahhoz, hogy az összes gyerek biztonságosan felüljön az óriáskerékre. Minden fülke egy vagy két gyereket tud elvinni, amíg összsúlyuk nem haladja meg az adott súlyhatárt.

**Osztály adattagjai:**  
- _numberOfChildren: A gyerekek száma.  
- _totalWeight: Az óriáskerék fülkéinek maximális súlykapacitása.  
- _arrWeightOfChildren: Egy lista, amely minden gyerek súlyát tartalmazza.

**Konstruktor (`__init__`):**   

A konstruktor inicializálja az adattagokat a bemeneti paraméterekkel: a gyerekek számával, az összsúlykapacitással, valamint a gyerekek súlyát tartalmazó listával.

**checkParameters() metódus:**

Ez a metódus a bemeneti paraméterek érvényességét ellenőrzi:

- Ellenőrzi, hogy a gyerekek száma és az összsúly a megadott tartományon belül van-e.
- Biztosítja, hogy a gyerekek súlyértékei érvényes tartományon belül legyenek.
- Ha minden paraméter megfelel, True-val tér vissza, különben False-szal.

**Calculate() metódus**

A Calculate() függvény célja, hogy a gyerekek számához viszonyítva a lehető legkevesebb fordulót használja az óriáskeréken. Ehhez rendezést és egy "oszd meg és uralkodj" alapú keresési algoritmust alkalmaz, hogy optimálisan párosítsa a gyerekeket.

**Működési elv:**  
1. Rendezés: 

   - A gyerekek súlyát tartalmazó listát növekvő sorrendbe rendezi, így a legnehezebb gyerekek a lista végén lesznek, megkönnyítve az optimális párosítást.

2. Iteratív feldolgozás és párosítás:
   - Minden iterációban a legnehezebb gyereket (nWeightOfActualChild) leválasztja a listáról.
   - Ezután a fennmaradó gyerekek listájában rekurzív keresést végez (findBestFitRecursive függvény), hogy megtalálja azt a legnehezebb gyereket, aki még belefér az adott kapacitásba az aktuálisan kiválasztott gyerek mellé.
   - Ha van ilyen gyerek, a program eltávolítja őt a listából, optimalizálva ezzel a párosítást.
3. Fordulószámláló frissítése:
   - Minden fülke indításával növeli a nCounter változót, ami a szükséges fordulók számát jelöli.
   - A folyamat addig ismétlődik, amíg minden gyerek sorra nem kerül.

4. Végső eredmény:  
A Calculate() függvény visszaadja a nCounter értékét, amely a minimális fordulók számát jelenti az adott beállítások mellett.

**findBestFitRecursive() függvény**  

Ez a rekurzív függvény egy bináris keresési algoritmus megvalósítása, amely az optimális párosítás érdekében hatékonyan találja meg azt a gyereket, aki a súlyhatáron belül van:

- A függvény a gyerekek súlyának listáját folyamatosan kettébontja, hogy meghatározza a legjobb illeszkedést a célértékhez.
- Ha megtalál egy megfelelő súlyú gyereket (akinek súlya kisebb vagy egyenlő a fennmaradó kapacitással), visszatér az indexével; ellenkező esetben folytatja a keresést az egyik oldalra szűkítve.

**Összefoglalás**  

A Calculate() metódus a gyorsabb keresés érdekében rendezi a gyerekek súlyát, majd egy rekurzív "oszd meg és uralkodj" algoritmussal találja meg az optimális párosításokat. Ez az eljárás biztosítja a lehető legkevesebb fordulót, miközben minimalizálja az óriáskerék fülkéinek kihasználatlanságát.

## Tesztelés: ##

- Tesztrendszer: Source/File_test.py  
- Tesztfájlok: Tests/input és Tests/output

A tesztelés célja a FerrisWheel osztály Calculate() metódusának helyes működésének ellenőrzése különböző bemeneti adatokkal. A tesztelés fájlalapú bemenetet és kimenetet használ, és az eredmények automatikus összehasonlítását végzi.

**Tesztelési folyamat:**  

1. Bemeneti fájlok feldolgozása:

- A tesztelés az input mappában található fájlok alapján történik. Minden fájl egy külön tesztesetet képvisel, ahol az első sor a gyerekek számát és az összkapacitást tartalmazza, a második sor a gyerekek súlyait.

3. Objektum létrehozása és paraméterellenőrzés:

- Az input adatokat a FerrisWheel osztály konstruktorába adja, és a checkParameters() metódus segítségével érvényesíti azokat.
Ha a bemeneti adatok érvénytelenek, a program tovább lép a következő tesztre.

4. Eredmény kiszámítása:

- A Calculate() metódus segítségével kiszámítja, hogy hány fordulóra van szükség a gyerekek optimális párosításához.

5. Kimeneti fájlok ellenőrzése:

- A számított eredményt (result_by_calc) összeveti az elvárt kimenettel, amely az output mappa megfelelő fájljából származik.
- A program jelzi, ha az eredmények nem egyeznek, így gyorsan kiszűrhetők az eltérések.
6. Összehasonlítás és kiértékelés:

- A számított eredményt (res_by_calc) és az elvárt kimenetet (res_by_outPut) hasonlítja össze.
- A teszt eredményét a program kiírja a képernyőre, jelezve, hogy az értékek egyeznek-e.

Ez a tesztelési megközelítés biztosítja, hogy a FerrisWheel osztály helyesen működjön, és az algoritmus a várt eredményeket adja különböző bemeneti adatokat figyelembe véve.