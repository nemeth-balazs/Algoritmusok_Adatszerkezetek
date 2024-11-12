from GraphNode import GraphNode
import queue

class BuildingRoads:
    _numberOfCities = 0
    _numberOfRoads = 0
    _arrCityToCity = [[]]
    def __init__(self, numberOfCities, numberOfRoads, arrCityToCity):
        self._numberOfCities = numberOfCities
        self._numberOfRoads = numberOfRoads
        self._arrCityToCity = arrCityToCity

    def checkParameters(self) -> bool:

        if self._numberOfCities < 1 or self._numberOfCities > 10e5:
            return False

        if self._numberOfRoads < 1 or self._numberOfRoads > 2*10e5:
            return False

        if len(self._arrCityToCity) != self._numberOfRoads:
            return False

        if any(nCities == 2 for nCities in self._arrCityToCity):
            return False

        if any(nCity < 1 or nCity > 10e5 for inner_list in self._arrCityToCity for nCity in inner_list):
            return False

        return True

    def Calculate(self):
        arrDifferentTrees = []
        setNodes = self.GetGraphNodes(self._arrCityToCity)
        if len(setNodes) == 0:
            return arrDifferentTrees

        for node in setNodes:
            if node.Discovered:
                continue

            arrDifferentTrees.append([node.cityIndex])
            queueNode = queue.Queue()
            queueNode.put(node)
            while not queueNode.empty():
                actualNode = queueNode.get()
                actualNode.Discovered = True

                for child in actualNode.Children:
                    if not child.Discovered:
                        child.Parent = actualNode
                        arrDifferentTrees[-1].append(child.cityIndex)
                        child.Discovered = True
                        queueNode.put(child)

        arrNewRoads = self.GetNewRoads(arrDifferentTrees)
        return [ len(arrNewRoads), arrNewRoads ]

    def GetGraphNodes(self, arrCityToCity: '[[]]'):

        dictCityIndexToGraphNode = dict()
        for arrCities in arrCityToCity:

            firstCity = GraphNode(arrCities[0]) if not arrCities[0] in dictCityIndexToGraphNode else dictCityIndexToGraphNode[arrCities[0]]
            secondCity = GraphNode(arrCities[1]) if not arrCities[1] in dictCityIndexToGraphNode else dictCityIndexToGraphNode[arrCities[1]]

            firstCity.AppendChildren(secondCity)
            secondCity.AppendChildren(firstCity)
            dictCityIndexToGraphNode[arrCities[0]] = firstCity
            dictCityIndexToGraphNode[arrCities[1]] = secondCity

        for nCityIndex in range(1, self._numberOfCities+1):
            if not nCityIndex in dictCityIndexToGraphNode:
                dictCityIndexToGraphNode[nCityIndex] = GraphNode(nCityIndex)

        return dictCityIndexToGraphNode.values()

    def GetNewRoads(self, arrDifferentTrees):
        arrNewRoads = []
        for i in range(0, len(arrDifferentTrees)):
            if i + 1 < len(arrDifferentTrees):
                combined = [arrDifferentTrees[i][0], arrDifferentTrees[i + 1][0]]
                arrNewRoads.append(combined)

        return arrNewRoads




