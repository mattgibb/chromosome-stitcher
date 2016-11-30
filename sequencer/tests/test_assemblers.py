import unittest
from networkx import DiGraph

from sequencer.parsers import Sequence
from sequencer.assemblers import assemble

class TestAssemblers(unittest.TestCase):
    def test_assemble(self):
        seqs = [
            Sequence("a", "DriverSaves"),
            Sequence("b", "EachDay"),
            Sequence("c", "LivesEach"),
            Sequence("d", "SavesLives")
        ]

        path = list('adcb')

        graph = DiGraph()
        graph.add_edge('a', 'd', overlap=5)
        graph.add_edge('d', 'c', overlap=5)
        graph.add_edge('c', 'b', overlap=4)

        self.assertEqual(assemble(seqs, graph, path), "DriverSavesLivesEachDay")
