from SearchEnum import SearchEnum
class node():
    path=[]
    children = dict
    name = ""
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
    visited = []
    def __init__(self, startNode):
        self.data = []
        self.visited = []
        self.startNode = startNode
        self.addNode(startNode)

    def addNode(self, p):
        self.data.append(p)

    def removeFront(self):
        node = self.data.pop(0)
        if(node.name not in self.visited):
            print(node.name)
            self.visited.append(node.name)
        return node

    def checkValid(self,node):
        if (node.path[0] in self.visited):
            return False
        else:
            return True
    def sortQueue(self,qType):
        if qType == SearchEnum.DEPTH_FIRST_SEARCH:
            self.data.sort(key=lambda x: x.name, reverse = False)
            self.data.sort(key=lambda x: len(x.path), reverse = True)
        elif qType == SearchEnum.BREADTH_FIRST_SEARCH:
            return
        elif qType == SearchEnum.DEPTH_LIMITED_SEARCH:
            return
        elif qType == SearchEnum.ITERATIVE_DEEPENING_SEARCH:
            return
        elif qType == SearchEnum.UNIFORM_COST_SEARCH:
            return
        elif qType == SearchEnum.A_STAR:
            return
        elif qType == SearchEnum.GREEDY_SEARCH:
            return
        elif qType == SearchEnum.BEAM_SEARCH:
            return
        elif qType == SearchEnum.HILL_CLIMBING:
            return




    
    
