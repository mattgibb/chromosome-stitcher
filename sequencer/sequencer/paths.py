def zip_path_with_overlaps(path, digraph):
    overlaps = [0] # first node doesn't have previous overlap
    for i in range(len(path)-1):
        a, b = path[i], path[i+1]
        overlap = digraph.edge[a][b]['overlap']
        overlaps.append(overlap)

    return list(zip(path, overlaps))

def __without_node(graph, node):
    return graph.subgraph(n for n in graph if n != node)

def find_hamiltonian(digraph):
    return hamiltonians(digraph, first=True)

def hamiltonians(digraph, first=False):
    n = len(digraph)
    partial_hamiltonians = [([node], digraph) for node in digraph]
    hamiltonians = []
    
    while partial_hamiltonians:
        base_path, graph = partial_hamiltonians.pop()
        tip = base_path[-1]
        for successor in graph.successors(tip):
            path = base_path + [successor]
            if len(path) == n:
                if first: return path #winning, bail once we find one
                hamiltonians.append(path)
            subgraph = __without_node(graph, tip)
            partial_hamiltonians.append((path, subgraph))
    
    if first: # we never found one
        return None
    else:
        return hamiltonians
