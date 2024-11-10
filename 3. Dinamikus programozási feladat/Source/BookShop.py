import math

class BookShop:
    _numberOfBook = 0
    _totalMoney = 0
    _arrPricesOfBooks = []
    _arrPagesOfBooks = []
    def __init__(self, numberOfBook, totalMoney, arrPricesOfBooks, arrPagesOfBooks):
        self._numberOfBook = numberOfBook
        self._totalMoney = totalMoney
        self._arrPricesOfBooks = arrPricesOfBooks
        self._arrPagesOfBooks = arrPagesOfBooks

    def checkParameters(self) -> bool:

        if self._numberOfBook < 1 or self._numberOfBook > 1000:
            return False

        if self._totalMoney < 1 or self._totalMoney > 10e5:
            return False

        if self._numberOfBook == 0:
            return False

        if self._numberOfBook!= len(self._arrPagesOfBooks) or self._numberOfBook!= len(self._arrPagesOfBooks):
            return False

        if any(nPriceOfBook < 1 or nPriceOfBook > 1000 for nPriceOfBook in self._arrPricesOfBooks):
            return False

        if any(nPageOfBook < 1 or nPageOfBook > 1000 for nPageOfBook in self._arrPagesOfBooks):
            return False

        return True

    def Calculate(self):
        pages = [[0] * (self._totalMoney+1) for _ in range(self._numberOfBook+1)]

        for numberOfBookToChoice in range(1, self._numberOfBook+1):
            for priceIndex in range(1, self._totalMoney+1):
                pages[numberOfBookToChoice][priceIndex] = pages[numberOfBookToChoice-1][priceIndex]
                if priceIndex >= self._arrPricesOfBooks[numberOfBookToChoice-1]:
                        pages[numberOfBookToChoice][priceIndex] = max(pages[ numberOfBookToChoice-1][priceIndex],
                                                                      pages[ numberOfBookToChoice-1][priceIndex-self._arrPricesOfBooks[numberOfBookToChoice-1] ] + self._arrPagesOfBooks[numberOfBookToChoice-1])

        return pages[-1][-1]