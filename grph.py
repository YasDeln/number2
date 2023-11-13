Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Overlap Graphs
... 
... from .helpers import Parser
... from itertools import permutations
... 
... 
... def overlap_graph(seqs, n=3):
...     for pair in permutations(seqs, 2):
...         if pair[0].seq.endswith(pair[1].seq[:n]):
...             yield (pair[0].id, pair[1].id)
... 
... 
... def main(file):
...     fa = Parser(file).fastas()
...     for i in overlap_graph(fa):
