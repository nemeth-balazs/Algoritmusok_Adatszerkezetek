class ConcertTickets:

    _numberOfTickets = 0
    _numberOfCustomer = 0
    _arrCustomerOffers = []
    _arrTicketPrices = []
    def __init__(self, numberOfTickets: 'int', numberOfCustomer: 'int',  arrTicketPrices: '[]', arrCustomerOffers: '[]',):
        self._numberOfTickets = numberOfTickets
        self._numberOfCustomer = numberOfCustomer
        self._arrTicketPrices = arrTicketPrices
        self._arrCustomerOffers = arrCustomerOffers

    def checkParameters(self) -> bool:

        if self._numberOfTickets < 1 or self._numberOfTickets > 2*10e5:
            return False

        if self._numberOfCustomer < 1 or self._numberOfCustomer > 2*10e5:
            return False

        if len(self._arrCustomerOffers) == 0 or len(self._arrTicketPrices) == 0:
            return False

        if self._numberOfTickets != len(self._arrTicketPrices):
            return False

        if self._numberOfCustomer != len(self._arrCustomerOffers):
            return False

        if any(nCustomerOffer < 1 or nCustomerOffer > 10e9 for nCustomerOffer in self._arrCustomerOffers):
            return False

        if any(nTicketPrices < 1 or nTicketPrices > 10e9 for nTicketPrices in self._arrTicketPrices):
            return False

        return True

    def Calculate(self):
        self._arrTicketPrices.sort()
        arrTicketPriceForCustomer = []
        for nCustomerOffer in self._arrCustomerOffers:
            bestFitIndex = self.findBestFitRecursive(self._arrTicketPrices, 0, len(self._arrTicketPrices), nCustomerOffer)
            arrTicketPriceForCustomer.append(self._arrTicketPrices.pop(bestFitIndex)) if bestFitIndex >= 0 else arrTicketPriceForCustomer.append(-1)

        return arrTicketPriceForCustomer

    def findBestFitRecursive(self, arrTicketPrices, fromIndex, toIndex, targetValue):
        index = int((fromIndex + toIndex) / 2)
        if len(arrTicketPrices) == 0:
            return -1
        elif arrTicketPrices[index] <= targetValue and toIndex - fromIndex == 1:
            return index
        elif arrTicketPrices[index] > targetValue and toIndex - fromIndex == 1:
            return -1
        elif arrTicketPrices[index] > targetValue:
            return self.findBestFitRecursive(arrTicketPrices, fromIndex, index, targetValue)
        else:
            return self.findBestFitRecursive(arrTicketPrices, index, toIndex, targetValue)
