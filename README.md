# Sequence All the Genomes!
My first investigation of the data and the problem is found in the
'DNA Sequence Stetch' notebook, and tested production code is found in
'sequencer'.

## Getting Started
### Install dependencies
```
pip install networkx
```

### Run program
list the FASTA file as an argument:

```
cd sequencer
bin/build tests/fixtures/example.fasta
```

or pipe it to stdin:

```
cd sequencer
bin/build < ../data/coding_challenge_data_set.txt > genome.txt
```

### Run tests
```
cd sequencer
python -munittest
```

## Future Work
### Sequence Matching
I spent a bunch of time getting familiar with tries, suffix trees, Ukkonen's
algorithm, KMP etc. I should probably have known all this stuff already, but
Tushar Roy has become my new favourite person on YouTube. What a legend!

The current implementation is just brute force and takes O(m^2*n^2) time where
m is the average sequence length and n is the number of sequences. I would 
have loved to build a solution in Go that combined each suffix greater than
half the length of its sequence into a single trie for all sequences. Each
sequence could then be used to traverse the trie, collecting prefix matches
as it went.

Both trie construction and traversal would be linear in m and n. Because every
full sequence would be included in the trie (as the largest suffix), every
traversal will end up performing a match on the whole string. A small
optimization at trie construction time might store a flag at each intermediate
node, marking whether more than one path remains, allowing much earlier exits
in most cases.

Given that there are only 4 bases, each of which can be represented by 2 bits,
it might have been interesting to explore compressed binary representations
and algorithms.

### Matching with Errors/Local Matching
Indels and substitutions make sequencing trickier when working with real data,
and I would love to get more familiar with several approaches to this problem.

### String Overlaps
The current implementation simply finds the shortest overlap, and doesn't
continue to check for all overlaps.

### Finding Hamiltonian Paths
A closer look at possible optimizations for the brute force algorithm is found
in the 'Failed proof of divide and conquer technique for graphs with unique
Hamiltonians' notebook.

Late in the day, I found a great paper 'Rubin_Hamiltonian_Search.pdf', which I
would have loved to implement with a bit more time.
