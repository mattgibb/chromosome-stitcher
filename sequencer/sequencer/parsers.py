import re
from collections import namedtuple

class Sequence(namedtuple('Sequence', 'name bases')):
    __format = re.compile(r'(?P<name>[^\r\n]+)\r?\n(?P<bases>[ACGT\r\n]+)')

    @classmethod
    def parse(cls, seq_string):
        seq = cls.__format.fullmatch(seq_string)
        if not seq: raise NameError("sequence isn't the right format:\n%s" % log_string)
        name = seq.group('name')
        bases = seq.group('bases').replace('\r', '').replace('\n', '')
        return cls(name, bases)

    def __repr__(self, n=10):
        ellipsis = '...' if len(self.bases) > n else ''
        return self.name + ': ' + self.bases[:n] + ellipsis

def parse_fasta(io):
    paragraphs = io.read().split('>')[1:]
    return [Sequence.parse(p) for p in paragraphs]
    
