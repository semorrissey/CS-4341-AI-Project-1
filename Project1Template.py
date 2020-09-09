from SearchEnum import SearchEnum
import Graph
import sys
from collections import OrderedDict
# Template for Project 1 of CS 4341 -A2020
def General_Search(problem : Graph.Graph, search : SearchEnum):
    """ Return the solution path or failure to reach node G from node S.
    Also outputs the expanded nodes and the queues before each expansion.
        
        Parameters
        ----------
        problem : Graph.Graph
            The graph to search from S to G.
        search : SearchEnum.SearchEnum
        The search method to use to search the graph.  """
    initialState = 'S' # name of the initial state
    finalState = 'G' # Name of the final state
    solution = finalState
    State =[]
    # Make_Queue, Make_Node, Remove_Front, State[node], Expand, and expand_queue are to be implemented by the student. Implementation may vary depending on the data structures used.
    queue = Make_Queue(Make_Node(problem.getState(initialState)))
    while len(queue) > 0:
        node = Remove_Front(queue)
        # state[node] is the current path so far that has been expanded
        #checks to see if the front of the queue is in that path and is at the final state
        #solution is the finalstate
        if State[node] is solution:
            return State[node]
        # expand creates a list of all the possible paths from opened or possible nodes,
        # expand_queue adds them to the queue given the rules for each search algorithm
        opened_nodes = Expand(node)
        expand_queue(queue,opened_nodes,problem,search)
    print("failure to find path between S and G")
    return False
def expand_queue(queue, pathsToAddToQueue, problem, search):
    """
    Add the new paths created from the opened nodes to the queue based on the search strategy.

    Parameters
    ----------
    queue 
        The queue containing the possible paths to expand upon for the search.
    newPathsToAddToQueue : list
        The list of paths to add to the queue.
    problem : Graph.Graph
        The graph to search from S to G.
    search : SearchEnum.SearchEnum
        The search method to use to search the graph.
    """
    #Fill in the below if and elif bodies to implement how the respective searches add new paths to the queue.
    if search == SearchEnum.DEPTH_FIRST_SEARCH:
        return "yo"

    elif search == SearchEnum.BREADTH_FIRST_SEARCH:
        return "yo"

    elif search == SearchEnum.DEPTH_LIMITED_SEARCH:
        return "yo"

    elif search == SearchEnum.ITERATIVE_DEEPENING_SEARCH:
        return "yo"

    elif search == SearchEnum.UNIFORM_COST_SEARCH:
        return "yo"

    elif search == SearchEnum.GREEDY_SEARCH:
        return "yo"

    elif search == SearchEnum.A_STAR:
        return "yo"

    elif search == SearchEnum.HILL_CLIMBING:
        return "yo"

    elif search == SearchEnum.BEAM_SEARCH:
        return "yo"

def main(filename : str):
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
        if (not General_Search(graph, search)):
            print("failure to find path between S and G")
        else:
            print("\tgoal reached!")
        print()
def readInput(filename : str) -> Graph.Graph:
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
                    node, heurStr = line.split(' ')
                    heuristic = float(heurStr)
                    parsedGraph.setHeuristic(node, heuristic)
                else:
                    node1, node2, costStr = line.split(' ')
                    cost = float(costStr)
                    parsedGraph.addNodesAndEdge(node1,node2, cost)
    for node_key in parsedGraph.nodes:
        node = parsedGraph.nodes[node_key]
        node.edges = OrderedDict(sorted(node.edges.items()))
    return parsedGraph   
if __name__ == "__main__": 
    if len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        print("Must input the filename with the graph input to search.")


def Make_Queue(node):
    return

def Make_Node(state):
    return

def Remove_Front(queue):
    return

def Expand(node):
    return