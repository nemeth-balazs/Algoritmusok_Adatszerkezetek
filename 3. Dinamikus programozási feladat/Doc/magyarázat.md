# Dinamikus programozási feladat
## Feladat megnevezése: [Book Shop](https://cses.fi/problemset/task/1158/)

- Az algoritmus implementálása: Source/Bookshop.py

**Osztály áttekintése: BookShop** 

A BookShop osztály egy olyan rendszert modellez, amelynek célja, hogy egy adott költségvetésen belül a lehető legtöbb oldalszámú könyvet vásárolhassuk meg. Az osztály olyan adattagokat és metódusokat tartalmaz, amelyek a könyvek árait, oldalszámait és a teljes költségvetést kezelik.

**Osztály adattagjai:**
- _numberOfBook: A rendelkezésre álló könyvek száma.
- _totalMoney: Az összes könyvvásárlásra szánt költségvetés.  
- _arrPricesOfBooks: Egy lista, amely minden könyv árát tartalmazza.  
- _arrPagesOfBooks: Egy lista, amely minden könyv oldalszámát tartalmazza.  

**Konstruktor (`__init__`):** 

A konstruktor inicializálja a fenti adattagokat a bemeneti paraméterek alapján: a könyvek számával, az összköltségvetéssel, valamint a könyvek árával és oldalszámával.

**checkParameters() metódus:**  

Ez a metódus ellenőrzi a bemeneti paramétereket, hogy biztosan az elvárt tartományban legyenek:

Ellenőrzi, hogy a könyvek száma és a teljes költségvetés az érvényes határok között van-e.
Biztosítja, hogy a könyvek árai és oldalszámai valós értékeket képviselnek; ha minden ellenőrzés megfelel, True értékkel tér vissza, különben False-szal.

**Calculate() metódus:**  

A Calculate() függvény dinamikus programozást alkalmaz annak érdekében, hogy maximalizálja az adott költségvetésen belül megvásárolható oldalszámot. A metódus iterál a könyveken és a költségvetési szinteken, frissítve egy 2D-s pages táblázatot, amely az egyes könyv- és költségkombinációk esetében elérhető maximális oldalszámot tárolja.

**Működési elv:**  
1. 2D tömb inicializálása:   
A pages egy olyan táblázat, amely mérete [numberOfBook + 1][totalMoney + 1], ahol pages[i][j] az elérhető maximális oldalszámot jelöli az első i könyv felhasználásával és j költségvetéssel.
2. Iteratív számítás:  
   - Minden könyv esetében (numberOfBookToChoice) ellenőrzi az összes lehetséges költségvetési értéket (priceIndex).
   - Aktuális könyv nélküli eset: Kezdetben pages[numberOfBookToChoice][priceIndex] az előző maximális oldalszámot örökli az aktuális könyv nélkül (pages[numberOfBookToChoice-1][priceIndex]).
   - Aktuális könyvvel rendelkező eset: Ha az aktuális költségvetés megengedi a könyv megvásárlását (azaz priceIndex nagyobb vagy egyenlő, mint a könyv ára), akkor a függvény összehasonlítja:
   - A könyv kihagyása: Az előző maximális oldalszám megtartása.
   - A könyv bevonása: A könyv oldalszámának hozzáadása az eredményhez, ha belefér a költségvetésbe.
   - Az optimális értéket (lehető legnagyobb oldalszámot) a pages tömb tárolja.
3. Végső eredmény:  
A végső válasz a pages[-1][-1] pozícióban található, amely az összes könyv és a teljes költségvetés mellett elérhető maximális oldalszámot jelenti.


**Összefoglalás**   

A Calculate() metódus dinamikus programozást alkalmaz, hatékonyan kiszámítva a költségvetésen belül elérhető maximális oldalszámot az előzőleg kiszámított eredmények felhasználásával. Ez az eljárás biztosítja, hogy a megoldás optimális és hatékony legyen, különösen akkor, ha sok könyv és nagy költségvetés áll rendelkezésre.

## Tesztelés: ##

- Tesztrendszer: Source/File_test.py  
- Tesztfájlok: Tests/input és Tests/output

A tesztelés célja a BookShop osztály Calculate() függvényének helyes működésének ellenőrzése különböző bemeneti adatokkal. A tesztelés egy bemeneti és egy elvárt kimeneti fájlstruktúrára épül, amely az eredmények automatikus összehasonlítását teszi lehetővé.

**Tesztelési folyamat:**  

1. Fájlbeolvasás:

- Az input mappa fájljait egyenként feldolgozza. Minden fájl egy tesztesetet képvisel, ahol az első sor a könyvek számát és a teljes költségvetést, a második sor a könyvek árait, a harmadik pedig az oldalszámokat tartalmazza.  

3. Objektum Létrehozása és Ellenőrzése:

- A bemeneti adatokat a BookShop osztály konstruktorának adja át.
- A checkParameters() függvény segítségével előzetes validálást végez, hogy csak érvényes bemeneti adatok alapján történjen számítás.

4. Eredmények Összehasonlítása:

- A számított eredményt (result_by_calc) összeveti az elvárt kimenettel, amely az output mappa megfelelő fájljából származik.
- A program jelzi, ha az eredmények nem egyeznek, így gyorsan kiszűrhetők az eltérések.

Ez a fájlalapú megközelítés biztosítja, hogy a Calculate() algoritmus különböző helyzetekben is megfelelően működjön, és az esetleges hibák gyorsan felfedezhetők legyenek.


