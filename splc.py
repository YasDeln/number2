Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # RNA Splicing
... 
... from functools import reduce
... from .helpers import Parser, Dna
... 
... 
... def main(file):
...     def trim(gene, intron):
...         s = gene.find(intron)
...         return gene[:s] + gene[s + len(intron) :]
... 
...     seqs = Parser(file).seqs()
