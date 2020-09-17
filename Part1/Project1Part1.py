from SearchEnum import SearchEnum
import Graph
import sys
from dataStruct import node
from dataStruct import queue
from collections import OrderedDict
# Template for Project 1 of CS 4341 - A2020
def General_Search(problem, searchMethod):
    """
    Return the solution path or failure to reach state G from state S. 
    
    Parameters
    ----------
    problem : Graph.Graph
        The graph to search from S to G.
    searchMethod : SearchEnum
        The search method to use to search the graph.
    """
    initialState = 'S' # name of the initial state
    finalState = 'G' # Name of the final state

    # Make_Queue, Make_Queue_Node, Remove_Front, Terminal_State, Expand, and expand_queue are to be implemented by the student. 
    # Implementation of the below pseudocode may vary slightly depending on the data structures used.

    queue = Make_Queue(Make_Queue_Node(problem.getState(initialState)))
    # Initialize the data structures to start the search at initialState
    while len(queue.data) > 0:
         print(queue.data[0].name + "          " + str(queue.toString(searchMethod)))
         node = Remove_Front(queue) # Remove and return the node to expand from the queue
         if Terminal_State(node) is finalState: # solution is not a defined variable, but this statement represents checking whether you have expanded the goal node.
             return node # If this is a solution, return the node containing the path to reach it.
         opened_nodes = Expand(node,problem) # Get new nodes to add to the queue based on the expanded node.
         expand_queue(queue,opened_nodes,problem,searchMethod)
    return False
def expand_queue(queue, nodesToAddToQueue, problem, searchMethod):
    """
    Add the new nodes created from the opened nodes to the queue based on the search strategy.

    Parameters
    ----------
    queue 
        The queue containing the possible nodes to expand upon for the search.
    newNodesToAddToQueue : list
        The list of nodes to add to the queue.
    problem : Graph.Graph
        The graph to search from S to G.
    searchMethod : SearchEnum
        The search method to use to search the graph.
    """
 #Fill in the below if and elif bodies to implement how the respective searches add new nodes to the queue.
    if searchMethod == SearchEnum.DEPTH_FIRST_SEARCH:
        for i in nodesToAddToQueue:
            if(queue.checkValid(i,searchMethod)):
                queue.addNode(i)
        queue.sortQueue(searchMethod)
    elif searchMethod == SearchEnum.BREADTH_FIRST_SEARCH:
         for i in nodesToAddToQueue:
             if(queue.checkValid(i,searchMethod)):
                queue.addNode(i)
         queue.sortQueue(searchMethod)
    elif searchMethod == SearchEnum.DEPTH_LIMITED_SEARCH:
             for i in nodesToAddToQueue:
                    if(queue.checkValid(i,searchMethod)):
                        if(len(i.path) <= 3):
                            queue.addNode(i)
             queue.sortQueue(searchMethod)
    elif searchMethod == SearchEnum.ITERATIVE_DEEPENING_SEARCH:
             for i in nodesToAddToQueue:
                    if(queue.checkValid(i,searchMethod)):
                        if(len(i.path) <= queue.limit +1):
                            queue.addNode(i)
             if(not queue.data):
                print("L=" + str(queue.limit))
                queue.limit += 1
                queue.addNode(queue.startNode)
             queue.sortQueue(searchMethod)
    elif searchMethod == SearchEnum.UNIFORM_COST_SEARCH:
        for i in nodesToAddToQueue:
            if(queue.checkValid(i,searchMethod)):
                queue.addNode(i)
        queue.sortQueue(searchMethod)
    elif searchMethod == SearchEnum.GREEDY_SEARCH:
        for i in nodesToAddToQueue:
            if(queue.checkValid(i,searchMethod)):
                queue.addNode(i)
        queue.sortQueue(searchMethod)
    elif searchMethod == SearchEnum.A_STAR:
        for i in nodesToAddToQueue:
            if(queue.checkValid(i,searchMethod)):
                queue.addNode(i)
        queue.sortQueue(searchMethod)
    elif searchMethod == SearchEnum.HILL_CLIMBING:
        nodesToAddToQueue.sort(key=lambda x: x.name, reverse = False)
        nodesToAddToQueue.sort(key=lambda x: len(x.path), reverse = True)
        nodesToAddToQueue.sort(key=lambda x: (x.heuristic,x.name), reverse = False)
        queue.addNode(nodesToAddToQueue[0])
        if(nodesToAddToQueue[0].name in queue.visited):
            queue.data = [];
        queue.sortQueue(searchMethod)
    elif searchMethod == SearchEnum.BEAM_SEARCH:
        for i in nodesToAddToQueue:
             if(queue.checkValid(i,searchMethod)):
                queue.addNode(i)
        queue.sortQueue(searchMethod)
def Make_Queue_Node(state):
    newNode = node(state.name, state.edges,state.heuristic)
    return newNode

def Make_Queue(initialNode):
    newQueue = queue(initialNode)
    return newQueue
def Remove_Front(givenQueue):
    return givenQueue.removeFront()
def Terminal_State(node):
    return node.path[0]
def Expand(givenNode,problem):
    result = []
    for name in givenNode.children:
        newNode = Make_Queue_Node(problem.getState(name))
        newNode.cost = givenNode.cost + givenNode.children.get(name)
        for x in givenNode.path:
            newNode.addNode(x)
        result.append(newNode)
    return result
def main(filename):
    """
    Entry point for this program. Parses the input and then runs each search on the parsed graph.

    Parameters
    ----------
    filename : str
        The name of the file with graph input to search
    """ 

    graph = readInput(filename)
    for search in SearchEnum:
        print(search.value)
        print("Expanded   Queue")
        solution = General_Search(graph, search)
        if (not solution):
            print("failure to find path between S and G")
        else:
            print("\tgoal reached!")
            solutionStr =""
            for i in reversed(solution.path):
                if(i is solution.path[len(solution.path)-1]):
                    solutionStr = i
                else:
                    solutionStr = solutionStr + "-" + i  
            print("solution found: " + solutionStr)
        print()
def readInput(filename):
    """
    Build the graph from the given input file.

    Parameters
    ----------
    filename : str
        The name of the file with input to parse into a graph.
    """

    parsedGraph = Graph.Graph()
    isHeuristicSection = False # True if processing the heuristic values for the graph. False otherwise.
    sectionDivider = "#####"
    minCharsInLine = 3 # Each line with data must have at least 3 characters
    with open(filename, 'r') as input:
        for line in input.readlines():
            if (len(line) > minCharsInLine):
                line = line.strip()
                if(sectionDivider in line):
                    isHeuristicSection = True
                elif(isHeuristicSection):
                    state, heurStr = line.split(' ')
                    heuristic = float(heurStr)
                    parsedGraph.setHeuristic(state, heuristic)
                else:
                    state1, state2, costStr = line.split(' ')
                    cost = float(costStr)
                    parsedGraph.addStatesAndEdge(state1,state2, cost)
    for state_key in parsedGraph.states:
        state = parsedGraph.states[state_key]
        state.edges = OrderedDict(sorted(state.edges.items()))
    return parsedGraph   
if __name__ == "__main__": 
    if len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        print("Must input the filename with the graph input to search.")
