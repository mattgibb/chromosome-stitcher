from networkx import DiGraph

def brute_force_matcher(seqs):
    graph = DiGraph()
    
    for i in range(len(seqs)):
        for j in range(len(seqs)):
            if i is j: continue # don't overlap string with itself
            
            bases_i, bases_j = seqs[i].bases, seqs[j].bases
            len_i, len_j = len(bases_i), len(bases_j)
            
            min_i_overlap = len_i//2 + 1
            min_j_overlap = len_j//2 + 1
            min_overlap = max(min_i_overlap, min_j_overlap)
            
            # check each string is long enough for the other
            if len_i < min_overlap or len_j < min_overlap: continue
            
            for overlap in range(min_overlap, min(len_i, len_j)+1):
                if bases_i[-overlap:] == bases_j[:overlap]:
                    graph.add_edge(seqs[i].name, seqs[j].name, overlap=overlap)
                    break #winning, ignore possible larger overlaps

    return graph

