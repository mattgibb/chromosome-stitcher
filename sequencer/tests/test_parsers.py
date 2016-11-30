import unittest, io
from sequencer.parsers import Sequence, parse_fasta 

class TestParsers(unittest.TestCase):
    def test_sequence(self):
        name = "some_fragment"
        bases = "ACC\nGGTT\n"
        sequence_string = "%s\n%s" % (name, bases)
        sequence = Sequence.parse(sequence_string)

        self.assertEqual(name, sequence.name)
        self.assertEqual(bases.replace("\n", ''), sequence.bases)

    def test_parse_fasta(self):
        file = io.StringIO(
""">Frag_56
ATTAGACCTG
>Frag_57
CCTGCCGGAA
>Frag_58
AGACCTGCCG
>Frag_59
GCCGGAATAC
""")

        sequences = [
            ("Frag_56", "ATTAGACCTG"),
            ("Frag_57", "CCTGCCGGAA"),
            ("Frag_58", "AGACCTGCCG"),
            ("Frag_59", "GCCGGAATAC")
        ]

        self.assertEqual(sequences, parse_fasta(file))
