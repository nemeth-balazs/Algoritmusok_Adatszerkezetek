from GraphNode import GraphNode
import queue

class DistanceQuery:
    _numberOfCities = 0
    _arrCityToCity = [[]]
    _arrRoadLength = []
    def __init__(self, numberOfCities, arrCityToCity, arrRoadLength):
        self._numberOfCities = numberOfCities
        self._arrCityToCity = arrCityToCity
        self._arrRoadLength = arrRoadLength

    def checkParameters(self) -> bool:

        if self._numberOfCities < 1 or self._numberOfCities > 10e4:
            return False

        if len(self._arrCityToCity) != self._numberOfCities-1:
            return False

        if len(self._arrCityToCity) != len(self._arrRoadLength):
            return False

        if any(nRoadLength < 1 or nRoadLength > 10e5 for nRoadLength in self._arrRoadLength):
            return False

        return True

    def Calculate(self, nFromCity, nToCity):

        setNodes = self.GetGraphNodes(self._arrCityToCity)
        self.FindParentAndChildrenForGrapNodes(setNodes, nFromCity)
        mapRoadLengths = self.GetRoadLengths(self._arrCityToCity, self._arrRoadLength)
        minRoadLength = self.FindMinOrMaxRoadLength(setNodes, mapRoadLengths, nFromCity, nToCity, False)
        maxRoadLength = self.FindMinOrMaxRoadLength(setNodes, mapRoadLengths, nFromCity, nToCity, True)

        return [minRoadLength,maxRoadLength ]

    def FindParentAndChildrenForGrapNodes(self, setNodes, nFromCity):
        if len(setNodes) == 0:
            return

        nCounter = 0
        node_iterator = iter(setNodes)
        while nCounter != len(setNodes):
            node = next(node_iterator)
            if nCounter == 0 and node.cityIndex != nFromCity:
                continue

            if node.Discovered:
                continue

            queueNode = queue.Queue()
            queueNode.put(node)
            while not queueNode.empty():
                actualNode = queueNode.get()
                nCounter += 1 if not actualNode.Discovered else 0
                actualNode.Discovered = True

                for child in actualNode.Children:
                    if not child.Discovered:
                        child.Parent = actualNode
                        child.Discovered = True
                        nCounter += 1
                        queueNode.put(child)

        return

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

    def GetRoadLengths(self, arrCityToCity, arrRoadLength):
        mapRoadLengths = dict()
        for (city1, city2), road_length in zip(arrCityToCity, arrRoadLength):
            mapRoadLengths[(city1, city2)] = road_length
            mapRoadLengths[(city2, city1)] = road_length

        return mapRoadLengths

    def FindMinOrMaxRoadLength(self, setNodes, mapRoadLengths, nFromCity, nToCity, bFindMaxRoadLength):

        roadLength = 0 if bFindMaxRoadLength else 10e5
        for node in setNodes:
            if node.cityIndex == nToCity:
                roadLength = self.GetMinMaxRoadRecursive(node, mapRoadLengths, nFromCity, bFindMaxRoadLength, roadLength)
                break

        return roadLength

    def GetMinMaxRoadRecursive(self, node, mapRoadLengths, nTargetCityIndex, bFindMaxRoadLength, roadLength):

        if node.cityIndex == nTargetCityIndex:
            return roadLength

        if node.Parent is None:
            return None

        roadLength = max(roadLength, mapRoadLengths[node.cityIndex, node.Parent.cityIndex]) if bFindMaxRoadLength else min(roadLength, mapRoadLengths[node.cityIndex, node.Parent.cityIndex])
        return self.GetMinMaxRoadRecursive(node.Parent, mapRoadLengths, nTargetCityIndex, bFindMaxRoadLength, roadLength)