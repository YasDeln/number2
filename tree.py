Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Completing a Tree
... 
... from .helpers import Parser
... 
... 
... # Nb. A connected tree of n nodes will always contain n-1 edges
... def main(file):
...     data = Parser(file).lines()
...     n_nodes = int(data[0])
