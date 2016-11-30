import unittest
from networkx import DiGraph
from sequencer.paths import hamiltonians, find_hamiltonian, zip_path_with_overlaps

class TestPaths(unittest.TestCase):
    def test_hamiltonians(self):
        graph = DiGraph()
        nodes = list(range(3))
        graph.add_cycle(nodes)
        rotations = {tuple(nodes[i:] + nodes[:i]) for i in nodes}

        self.assertEqual(set(map(tuple, hamiltonians(graph))), rotations)
        self.assertTrue(tuple(find_hamiltonian(graph)) in rotations)

    def test_zip_nodes_with_overlaps(self):
        graph = DiGraph()
        path = 'hop and a scotch'.split()
        overlaps = (2, 4, 6)
        for i in range(len(path)-1):
            graph.add_edge(path[i], path[i+1], overlap=overlaps[i])

        self.assertEqual(zip_path_with_overlaps(path, graph), [
            ('hop',    0),
            ('and',    2),
            ('a',      4),
            ('scotch', 6),
        ])






        
