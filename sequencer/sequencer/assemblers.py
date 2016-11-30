def assemble(seqs, graph, path):
    seq_lookup = {seq.name: seq.bases for seq in seqs}
    assembled = [seq_lookup[path[0]]]

    for i in range(len(path)-1):
        a, b = path[i], path[i+1]
        overlap = graph.edge[a][b]['overlap']
        bases = seq_lookup[b]
        tail = bases[overlap:]
        assembled.append(tail)

    return ''.join(assembled)
