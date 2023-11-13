Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Error Correction in Reads
... 
... from .helpers import Parser, Dna
... from .hamm import hamm
... 
... 
... def find_errors(seqs):
...     rseqs = [Dna(x).revc().seq for x in seqs]
...     unique = [x for x in seqs if seqs.count(x) + rseqs.count(x) == 1]
...     correct = set(seqs + rseqs).difference(set(unique))
... 
...     for x in unique:
...         for y in correct:
...             if hamm(x, y) == 1:
...                 yield x + "->" + y
... 
... 
... def main(file):
...     seqs = Parser(file).fastas()
...     seqs = [x.seq for x in seqs]
