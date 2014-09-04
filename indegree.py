"""
Graph Degree 
"""

EX_GRAPH0 = {0: set([1, 2]), 1: set([]), 2: set([])}
EX_GRAPH1 = {0 : set([1,4,5]) , 1 : set([2,6]) , 2 : set([3]) ,
             3 : set([0]) , 4 : set([1]) , 5 : set([2]) , 6 : set([])}
EX_GRAPH2 = {0 : set([1,4,5]) , 1 : set([2,6]) , 2 : set([3,7]) , 
             3 : set([7]) , 4 : set([1]) , 5 : set([2]) , 6 : set([])
             , 7 : set([3]) , 8 : set([1,2]) , 9 : set([0,3,4,5,6,7])}


def make_complete_graph(num_nodes):
    """
    Takes the number of nodes num_nodes and 
    returns a dictionary corresponding to a complete
    directed graph with the specified number of nodes. 
    """
    
    graph = {}
    if(num_nodes>0):
        for index in range(0,num_nodes):
            items = set([])
            for item in range(0,num_nodes):
                if item != index :
                    items.update(set([item]))
            graph[index] = items
            
    return graph


def compute_in_degrees(digraph):
    """
    Takes a directed graph and computes the
    in-degrees for the nodes in the graph.
    """
    
    graph = {}
    for key in digraph.keys():
        counter = 0
        for value in digraph.values():
            if key in value :
                counter = counter + 1
                
        graph[key] = counter
        
    return graph


def in_degree_distribution(digraph):
    """
    Takes a directed graph and computes the
    unnormalized distribution of the in-degrees
    of the graph.
    """
    
    indegree_graph = compute_in_degrees(digraph)
    
    graph = {}
    for value in indegree_graph.values():
        if value not in graph:
            graph[value] = 1
        else:
            graph[value] += 1
        
    return graph
                   