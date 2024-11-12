class GraphNode:
    def __init__(self, cityIndex):
        self._Discovered = False
        self._FullyChecked = False
        self._Parent = None
        self._Children = []
        self._cityIndex = cityIndex

    @property
    def cityIndex(self):
        return self._cityIndex

    @property
    def Discovered(self):
        return self._Discovered

    @Discovered.setter
    def Discovered(self, Discovered):
        self._Discovered = Discovered

    @property
    def Parent(self):
        return self._Parent

    @Parent.setter
    def Parent(self, Parent):
        self._Parent = Parent

    @property
    def Children(self):
        return self._Children

    @Children.setter
    def Children(self, Children):
        self._Children = Children

    def AppendChildren(self, Children):
        self._Children.append(Children)



