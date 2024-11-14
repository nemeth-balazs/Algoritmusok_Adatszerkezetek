# SPOJ feladat
## Feladat megnevezése: [DISQUERY - Distance Query](https://www.spoj.com/problems/DISQUERY/)

- Az algoritmus implementálása: Source/DistanceQuery.py

**Osztály áttekintése: DistanceQuery** 

A DistanceQuery osztály célja, hogy egy városhálózatban két megadott város között megtalálja az úthossz minimális és maximális értékeit. Az algoritmus felépít egy gráfot, amelyben a városokat utak kapcsolják össze, és szélességi kereséssel (BFS) tárja fel a városok közötti kapcsolatokat.

**Osztály adattagjai:**

- _numberOfCities (int) – A városok száma a hálózatban.
- _arrCityToCity (list of lists) – A városok közötti utak listája, ahol minden belső lista két város azonosítóját tartalmazza.
- _arrRoadLength (list) – Az utak hossza a városok között.  

**Konstruktor (`__init__`):** 

A konstruktor inicializálja a városok számát, a városok közötti kapcsolatokat és az utak hosszát.

**checkParameters() metódus:**  

A checkParameters() metódus ellenőrzi, hogy a városok száma és az utak hossza az előírt tartományon belül van-e, valamint hogy a kapcsolatok száma helyes-e.

**Calculate() metódus:**  

A Calculate() metódus a két megadott város közötti minimális és maximális úthossz kiszámításáért felel. Főbb lépései:

1. Gráf csomópontok létrehozása – A GetGraphNodes() függvény létrehozza a városok gráfját, ahol minden város egy-egy csomópont.
2. Szélességi keresés alkalmazása (BFS) – A FindParentAndChildrenForGraphNodes() függvény beállítja a csomópontok szülő és gyermek kapcsolatait, segítve az útvonalak feltérképezését.
3. Úthosszak kiszámítása – A GetRoadLengths() páronként eltárolja az utak hosszát, amelyet a minimális és maximális úthossz kiszámításához használ.
4. Minimális és maximális út meghatározása – A FindMinOrMaxRoadLength() megkeresi a megadott két város közötti minimális és maximális úthosszakat.

A Calculate() függvény egy listában adja vissza a minimális és maximális úthosszakat.

**További függvények** 

1. GetGraphNodes() – A megadott várospárokat csomópontként összeköti, és minden városhoz hozzáad egy csomópontot.
2. GetRoadLengths() – Az utak hosszát tárolja az összeköttetések alapján.
3. FindMinOrMaxRoadLength() – Rekurzív módon meghatározza a legrövidebb vagy leghosszabb útvonalat a két város között.

**Összefoglalás**   

A DistanceQuery osztály segítségével a városok hálózatában egy adott várospár között megtalálható a minimális és maximális úthossz. Az algoritmus szélességi kereséssel azonosítja a városkapcsolatokat, majd rekurzívan kiszámítja a lehetséges legkisebb és legnagyobb útvonalhosszakat.

## Tesztelés: ##

- Tesztrendszer: Source/File_test.py  
- Tesztfájlok: Tests/input és Tests/output

A tesztelés célja a DistanceQuery osztály Calculate() függvényének helyes működésének ellenőrzése különböző bemeneti adatokkal. A tesztelés egy bemeneti és egy elvárt kimeneti fájlstruktúrára épül, amely az eredmények automatikus összehasonlítását teszi lehetővé.

**Tesztelési folyamat:**  

1. Fájlbeolvasás:

- Az input mappában lévő fájlok egy-egy tesztesetet tartalmaznak, az első sorban a városok, majd az egyes városkapcsolatok és azok hosszával.

2. Objektum Létrehozása és Ellenőrzése:

- A DistanceQuery osztály konstruktora feldolgozza a bemenetet. A checkParameters() metódus biztosítja, hogy a bemeneti adatok érvényesek legyenek.

3. Eredmények Összehasonlítása:

- A kiszámított eredményeket az output mappában található elvárt értékekkel hasonlítja össze, eltérés esetén figyelmeztetve a felhasználót.

Ez a tesztelési módszer biztosítja, hogy a Calculate() algoritmus különféle helyzetekben helyesen működjön.
