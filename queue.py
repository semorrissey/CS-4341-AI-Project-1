from SearchEnum import SearchEnum
class node:
    
    def __init__(self, name, adjNode, costA, costE):
        self.name = name
        self.adjNode = adjNode
        self.costA = costA
        self.costE = costE

class path:
    path = []
    def __init__(self,startNode):
        self.startNode = startNode
        path.append(startNode)
    def addNode(self, node):
        path.append(node)
    def removeFront(self):
        path.pop(0)

class queue:
    queue = []
    
    def __init__(self, startPath, qType):
        self.startPath = startPath
        self.qType = qType
        self.addPath(startPath)

    def addPath(self, p):
        queue.append((p[0].name, p))

    def removeFront(self):
        queue.pop(0)

    def sortQueue(self):
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




    
    
