import unittest
from os import path

from sequencer.sequencers import build_chromosome

class TestSequencers(unittest.TestCase):
    def test_build_chromosome(self):
        fixture = path.join(path.dirname(__file__), './fixtures/example.fasta')
        with open(fixture) as file:
            chromosome = build_chromosome(file)
        self.assertEqual(chromosome, "ATTAGACCTGCCGGAATAC")

