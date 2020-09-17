from SearchEnum import SearchEnum
class node():
    path=[]
    children = dict
    name = ""
    heuristic = 0.0
    def __init__(self, name,children,h):
        self.path = []
        self.name = name
        self.cost = 0
        self.heuristic = h
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
        elif qType == SearchEnum.GREEDY_SEARCH:
            for i in self.visited:
                if(node.path.count(i) > 1 and node.path[0] in self.visited):
                    return False
            return True
        elif qType == SearchEnum.A_STAR:
            for i in self.visited:
                if(node.path.count(i) > 1 and node.path[0] in self.visited):
                    return False
            return True
        elif qType == SearchEnum.HILL_CLIMBING:
            for i in self.visited:
                if(node.path.count(i) > 1 and node.path[0] in self.visited):
                    return False
            return True
        elif qType == SearchEnum.BEAM_SEARCH:
            for i in self.visited:
                if(node.path.count(i) > 1):
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
            return
        elif qType == SearchEnum.A_STAR:
            self.data.sort(key=lambda x: x.name, reverse = False)
            self.data.sort(key=lambda x: len(x.path), reverse = True)
            self.data.sort(key=lambda x: ((x.heuristic + x.cost),x.name), reverse = False)
            return
        elif qType == SearchEnum.GREEDY_SEARCH:
            self.data.sort(key=lambda x: x.name, reverse = False)
            self.data.sort(key=lambda x: len(x.path), reverse = True)
            self.data.sort(key=lambda x: (x.heuristic,x.name), reverse = False)
            return
        elif qType == SearchEnum.BEAM_SEARCH:
            self.data.sort(key=lambda x: len(x.path), reverse = False)
            lenfirstElement = len(self.data[0].path) if self.data else None
            ifSame = all(len(i.path) == lenfirstElement for i in self.data)
            if(ifSame):
                while(len(self.data) > 2):
                    champion = self.data[0]
                    for i in self.data:
                        if(champion.heuristic < i.heuristic):
                            champion = i
                        elif(champion.heuristic == i.heuristic):
                            if(len(champion.path) < len(i.path)):
                                champion = i
                    self.data.remove(champion)
            thing = []
            for k in self.data:
                thing.append(k.path)
            print(thing)
            return
        elif qType == SearchEnum.HILL_CLIMBING:
            self.data.sort(key=lambda x: x.name, reverse = False)
            self.data.sort(key=lambda x: len(x.path), reverse = True)
            return




    
    
