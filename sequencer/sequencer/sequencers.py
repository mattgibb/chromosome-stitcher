from sequencer.parsers import parse_fasta
from sequencer.matchers import brute_force_matcher
from sequencer.paths import find_hamiltonian
from sequencer.assemblers import assemble

def build_chromosome(file):
    seqs = parse_fasta(file)
    graph = brute_force_matcher(seqs)
    hamiltonian = find_hamiltonian(graph)
    whole_sequence = assemble(seqs, graph, hamiltonian)
    return whole_sequence
