# CMPS 2200 Recitation 6
## Answers

**Name:** Griffin Olimpio and Devin Gutierrez


Place all written answers from `recitation-06.md` here for easier grading.



- **d.**

File | Fixed-Length Coding | Huffman Coding | Huffman vs. Fixed-Length
----------------------------------------------------------------------
f1.txt    |        2144  |     436       |  .2034
alice29.txt    |   1125520       |    74148   | 0.0659
asyoulik.txt    |       952176       |     77436   | 0.0813
grammar.lsp    |       26424        |    3339   | 0.1264
fields.c    |       75208         |       5336  |0.0709




- **e.**

If every character in the alphabet has the same frequency, then the Huffman tree for the document will be a perfectly balanced binary tree, with all leaves at the same depth. To see this, note that if the frequencies are the same, then at each step of the Huffman algorithm, we will be merging two subtrees of the same size.

Suppose that there are $n$ characters in the alphabet. Then the Huffman encoding for each character will be a binary code of length $\log_2 n$, since each character will be assigned a leaf at depth $\log_2 n$ in the perfectly balanced binary tree. The expected cost of a Huffman encoding for the document is therefore:

1/n sigma length of encoding for c= 1/n  sigma logn = logn

This expected cost is consistent across documents, since it only depends on the size of the alphabet and not on the specific frequencies of the characters in the document.
