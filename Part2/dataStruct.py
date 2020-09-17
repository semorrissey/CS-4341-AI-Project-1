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

    def toString(self, qType):
        if qType == SearchEnum.GREEDY_SEARCH or qType == SearchEnum.HILL_CLIMBING or qType == SearchEnum.BEAM_SEARCH:
            result = []
            for k in self.data:
                result.append((k.heuristic, k.path))
            return result
        elif qType == SearchEnum.UNIFORM_COST_SEARCH:
            result = []
            for k in self.data:
                result.append((k.cost, k.path))
            return result
        elif qType == SearchEnum.A_STAR:
            result = []
            for k in self.data:
                result.append((k.cost + k.heuristic, k.path))
            return result
        else:    
            result = []
            for k in self.data:
                result.append(k.path)
            return result

    def addNode(self, p):
        self.data.append(p)

    def removeFront(self):
        node = self.data.pop(0)
        if(node.name not in self.visited):
            self.visited.append(node.name)
        return node

    def getQueueNames(self):
        temp = []
        for i in self.data:
            temp.append(i.name)
        return temp

    def sortInformed(self,qType):
        if qType == SearchEnum.GREEDY_SEARCH or qType == SearchEnum.HILL_CLIMBING:
            for i,j in enumerate(self.data[:-1]):
                if(j.heuristic != self.data[i+1].heuristic):
                    if(j.heuristic > self.data[i+1].heuristic):
                        index1 = self.data.index(j)
                        index2 = self.data.index(self.data[i+1])
                        self.data[index1],self.data[index2] = self.data[index2],self.data[index1]
                else:
                    if(j.path[0] != self.data[i+1].path[0]):
                        temp = [j,self.data[i+1]]
                        temp.sort(key=lambda x: x.path, reverse = False)
                        index = self.data.index(j)
                        if(self.data[index] is not temp[0]):
                            index1 = self.data.index(j)
                            index2 = self.data[i+1]
                            self.data[index1],self.data[index2] = self.data[index2],self.data[index1]
                    else:
                        if(len(j.path) != len(self.data[i+1].path)):
                            if(len(j.path) > len(self.data[i+1].path)):
                                index1 = self.data.index(j)
                                index2 = self.data.index(self.data[i+1])
                                self.data[index1],self.data[index2] = self.data[index2],self.data[index1]
        elif qType == SearchEnum.A_STAR:
            for i,j in enumerate(self.data[:-1]):
                if((j.heuristic+j.cost) != (self.data[i+1].heuristic + self.data[i+1].cost)):
                    if((j.heuristic+j.cost)> (self.data[i+1].heuristic + self.data[i+1].cost)):
                        index1 = self.data.index(j)
                        index2 = self.data.index(self.data[i+1])
                        self.data[index1],self.data[index2] = self.data[index2],self.data[index1]
                else:
                    if(j.path[0] != self.data[i+1].path[0]):
                        temp = [j,self.data[i+1]]
                        temp.sort(key=lambda x: x.path, reverse = False)
                        index = self.data.index(j)
                        if(self.data[index] is not temp[0]):
                            index1 = self.data.index(j)
                            index2 = self.data[i+1]
                            self.data[index1],self.data[index2] = self.data[index2],self.data[index1]
                    else:
                        if(len(j.path) != len(self.data[i+1].path)):
                            if(len(j.path) > len(self.data[i+1].path)):
                                index1 = self.data.index(j)
                                index2 = self.data.index(self.data[i+1])
                                self.data[index1],self.data[index2] = self.data[index2],self.data[index1]
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
            self.data.sort(key=lambda x: x.path, reverse = False)
            self.data.sort(key=lambda x: len(x.path), reverse = True)
            return
        elif qType == SearchEnum.BREADTH_FIRST_SEARCH:
            self.data.sort(key=lambda x: len(x.path), reverse = False)
            return
        elif qType == SearchEnum.DEPTH_LIMITED_SEARCH:
            self.data.sort(key=lambda x: x.name, reverse = False)
            self.data.sort(key=lambda x: x.path, reverse = False)
            self.data.sort(key=lambda x: len(x.path), reverse = True)
            return
        elif qType == SearchEnum.ITERATIVE_DEEPENING_SEARCH:
            self.data.sort(key=lambda x: x.name, reverse = False)
            self.data.sort(key=lambda x: x.path, reverse = False)
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
            self.sortInformed(qType)
            return
        elif qType == SearchEnum.GREEDY_SEARCH:
            self.data.sort(key=lambda x: x.name, reverse = False)
            self.data.sort(key=lambda x: len(x.path), reverse = True)
            self.data.sort(key=lambda x: (x.heuristic,x.name), reverse = False)
            self.sortInformed(qType)
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
            return
        elif qType == SearchEnum.HILL_CLIMBING:
            self.data.sort(key=lambda x: x.name, reverse = False)
            self.data.sort(key=lambda x: len(x.path), reverse = True)
            self.sortInformed(qType)
            return




    
    
