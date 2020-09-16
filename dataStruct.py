from SearchEnum import SearchEnum
class node():
    path=[]
    children = dict
    def __init__(self, name,children):
        self.path = []
        self.name = name
        self.cost = 0
        self.children = children
        self.path.append(name)

    def addNode(self,node):
        self.path.append(node)
    def removeFront(self):
        self.path.pop(0)

class queue():
    data = []
    
    def __init__(self, startNode):
        self.data = []
        self.startNode = startNode
        self.addNode(startNode)

    def addNode(self, p):
        self.data.append(p)

    def removeFront(self):
        return self.data.pop()

    def sortQueue(self,qType):
        if self.qType == SearchEnum.DEPTH_FIRST_SEARCH:
            return
        elif self.qType == SearchEnum.BREADTH_FIRST_SEARCH:
            return
        elif self.qType == SearchEnum.DEPTH_LIMITED_SEARCH:
            return
        elif self.qType == SearchEnum.ITERATIVE_DEEPENING_SEARCH:
            return
        elif self.qType == SearchEnum.UNIFORM_COST_SEARCH:
            return
        elif self.qType == SearchEnum.A_STAR:
            return
        elif self.qType == SearchEnum.GREEDY_SEARCH:
            return
        elif self.qType == SearchEnum.BEAM_SEARCH:
            return
        elif self.qType == SearchEnum.HILL_CLIMBING:
            return




    
    
