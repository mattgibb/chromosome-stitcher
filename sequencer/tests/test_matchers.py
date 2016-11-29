import unittest
from sequencer.parsers import Sequence
from sequencer.matchers import brute_force_matcher 

class TestMatchers(unittest.TestCase):
    def setUp(self):
        self.sequences = [Sequence._make(s) for s in [
            ("Frag_56", "ATTAGACCTG"),
            ("Frag_57", "CCTGCCGGAA"),
            ("Frag_58", "AGACCTGCCG"),
            ("Frag_59", "GCCGGAATAC")
        ]]
        self.target = "ATTAGACCTGCCGGAATAC"

    def test_brute_force_matcher(self):
        match_graph = brute_force_matcher(self.sequences)
        self.assertEqual(set(match_graph.edges()), set((
            ("Frag_56", "Frag_58"),
            ("Frag_58", "Frag_57"),
            ("Frag_57", "Frag_59")
        )))

        for edge in match_graph.edges(data=True):
            self.assertEqual(edge[2]['overlap'], 7)

