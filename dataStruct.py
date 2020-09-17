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
    limit = 0
    def __init__(self, startNode):
        self.data = []
        self.visited = []
        self.limit = 0
        self.startNode = startNode
        self.addNode(startNode)

    def addNode(self, p):
        self.data.append(p)

    def removeFront(self):
        node = self.data.pop(0)
        print(node.name)
        if(node.name not in self.visited):
            self.visited.append(node.name)
        return node

    def checkValid(self,node,qType):
        if qType == SearchEnum.DEPTH_FIRST_SEARCH:
            if (node.path[0] in self.visited):
                return False
            else:
                return True
        elif qType == SearchEnum.BREADTH_FIRST_SEARCH:
            for i in self.visited:
                if(node.path.count(i) > 1):
                    return False
            return True
        elif qType == SearchEnum.DEPTH_LIMITED_SEARCH:
             for i in self.visited:
                if(node.path.count(i) > 1 and node.path[0] in self.visited):
                    return False
             return True
        elif qType == SearchEnum.ITERATIVE_DEEPENING_SEARCH:
             for i in self.visited:
                if(node.path.count(i) > 1 and node.path[0] in self.visited):
                    return False
             return True
        elif qType == SearchEnum.UNIFORM_COST_SEARCH:
            for i in self.visited:
                if(node.path.count(i) > 1 and node.path[0] in self.visited):
                    return False
            return True
    def sortQueue(self,qType):
        if qType == SearchEnum.DEPTH_FIRST_SEARCH:
            self.data.sort(key=lambda x: x.name, reverse = False)
            self.data.sort(key=lambda x: len(x.path), reverse = True)
            return
        elif qType == SearchEnum.BREADTH_FIRST_SEARCH:
            self.data.sort(key=lambda x: len(x.path), reverse = False)
            return
        elif qType == SearchEnum.DEPTH_LIMITED_SEARCH:
            self.data.sort(key=lambda x: x.name, reverse = False)
            self.data.sort(key=lambda x: len(x.path), reverse = True)
            return
        elif qType == SearchEnum.ITERATIVE_DEEPENING_SEARCH:
            self.data.sort(key=lambda x: x.name, reverse = False)
            self.data.sort(key=lambda x: len(x.path), reverse = True)
            return
        elif qType == SearchEnum.UNIFORM_COST_SEARCH:
            self.data.sort(key=lambda x: x.name, reverse = False)
            self.data.sort(key=lambda x: len(x.path), reverse = True)
            self.data.sort(key=lambda x: (x.cost,x.name), reverse = False)
            
            thing = []
            for k in self.data:
                thing.append(k.cost)
                thing.append(k.path)
            print(thing)
            return
        elif qType == SearchEnum.A_STAR:
            return
        elif qType == SearchEnum.GREEDY_SEARCH:
            return
        elif qType == SearchEnum.BEAM_SEARCH:
            return
        elif qType == SearchEnum.HILL_CLIMBING:
            return




    
    
