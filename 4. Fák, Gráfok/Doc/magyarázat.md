# Fák, Gráfok feladat
## Feladat megnevezése: [Building Roads](https://cses.fi/problemset/task/1666/)

- Az algoritmus implementálása: Source/Building Roads.py

**Osztály áttekintése: Building Roads** 

Ez az osztály egy olyan probléma megoldására készült, amelyben több városból álló hálózatot reprezentálunk, ahol a városokat utak kötik össze. Az algoritmus célja, hogy feltárja a különböző városcsoportokat (fák vagy komponensek), amelyeket közvetlen vagy közvetett utak kapcsolnak össze, és meghatározza, milyen további utak szükségesek a teljes hálózat összekapcsolásához. Az algoritmus alapja a szélességi keresés (BFS), amellyel végigjárhatók a gráf különálló részei. A cél a minimális számú új útvonal hozzáadása a városok teljes összekötéséhez.

**Osztály adattagjai:**
- _numberOfCities (int) – Az összes város száma.
- _numberOfRoads (int) – A meglévő utak száma a városok között.
- _arrCityToCity (list of lists) – Az egyes városok közötti kapcsolatok listája. Minden belső lista két elemet tartalmaz, amelyek a kapcsolatban lévő városokat azonosítják.

**Konstruktor (`__init__`):** 

A konstruktor inicializálja a városok és utak számát, valamint a városok közötti kapcsolatokat tároló listát.

**checkParameters() metódus:**  

A checkParameters() függvény végzi a bemeneti adatok validálását, ellenőrzi például, hogy a városok és utak száma érvényes tartományon belül van-e, valamint hogy a kapcsolatok száma helyes-e.

**Calculate() metódus:**  

A Calculate() függvény a hálózat elemzésének fő algoritmusát tartalmazza. A következő lépésekből áll:

1. Gráf csomópontok előállítása – A GetGraphNodes() függvény segítségével létrehozza a városok gráfját, ahol minden város egy-egy csomópontot képvisel.
2. Szélességi keresés (BFS) – Az algoritmus BFS-t alkalmaz minden városcsoportban, hogy feltárja az összes kapcsolt várost (komponenst), amelyek egy különálló hálózatot alkotnak. Minden újonnan felfedezett komponenst a arrDifferentTrees listához ad.
3. Új utak meghatározása – A GetNewRoads() függvénnyel az algoritmus meghatározza, hogy a különböző komponensek között milyen minimális számú új utat kell hozzáadni a hálózat összekapcsolásához. Az új utak két város azonosítóját tartalmazzák, ahol egy-egy új út megépítésére van szükség.

A Calculate() függvény eredményeként visszaadja az új utak számát, valamint a szükséges új utak listáját.

**További függvények** 

1. GetGraphNodes() – Létrehozza a városok csomópontjait tartalmazó gráfot a GraphNode osztály alapján. A megadott város-párokat összeköti, és minden városhoz hozzáad egy csomópontot, még akkor is, ha egy város nem szerepel kapcsolatokban.

2. GetNewRoads() – Elemzi az egymástól különálló városcsoportokat, és meghatározza az összekötésükhöz szükséges minimális számú utat.

**Összefoglalás**   

Az BuildingRoads osztály segít elemezni és kiegészíteni egy városhálózatot úgy, hogy a teljes hálózat összekapcsolt legyen. Az algoritmus BFS segítségével azonosítja a különálló városcsoportokat, majd meghatározza az ezek összekapcsolásához szükséges minimális számú új utat.

## Tesztelés: ##

- Tesztrendszer: Source/File_test.py  
- Tesztfájlok: Tests/input és Tests/output

A tesztelés célja a BookShop osztály Calculate() függvényének helyes működésének ellenőrzése különböző bemeneti adatokkal. A tesztelés egy bemeneti és egy elvárt kimeneti fájlstruktúrára épül, amely az eredmények automatikus összehasonlítását teszi lehetővé.

**Tesztelési folyamat:**  

1. Fájlbeolvasás:

- Az input mappában lévő fájlok mindegyike egy tesztesetet képvisel, ahol az első sorban a városok és utak száma, a többi sorban pedig az egyes városkapcsolatok szerepelnek.

2. Objektum Létrehozása és Ellenőrzése:

- A bemeneti adatokat a BuildingRoads osztály konstruktora fogadja. A checkParameters() függvény segítségével előzetesen ellenőrzi a paraméterek érvényességét, hogy csak megfelelő adatok alapján számítson.

3. Eredmények Összehasonlítása:

- A számított eredményt (result_by_calc) az output mappa megfelelő fájljából vett elvárt eredménnyel (result_by_output) veti össze. Ha az értékek eltérnek, azt a program jelzi.

Ez a fájlalapú tesztelési módszer biztosítja, hogy a Calculate() algoritmus különféle esetekben is helyesen működjön.
