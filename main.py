import math, queue
from collections import Counter


class TreeNode(object):
    # we assume data is a tuple (frequency, character)
    def __init__(self, left=None, right=None, data=None, char = None):
        self.left = left
        self.right = right
        self.data = data
        self.char = char
    def __lt__(self, other):
        return(self.data < other.data)
    def children(self):
        return((self.left, self.right))
    
def get_frequencies(fname):
    ## This function is done.
    ## Given any file name, this function reads line by line to count the frequency per character. 
    #f=open(fname, 'r')
    #C = Counter()
    #for l in f.readlines():
    #  C.update(Counter(l))
    #return(dict(C.most_common()))
    f = open(fname, 'r')
    C = Counter()
    for l in f.readlines():
        C.update(Counter(l.strip()))
    C.update(Counter('\n'))  # add new line count to the counter
    return(dict(C.most_common()))

# given a dictionary f mapping characters to frequencies, 
# create a prefix code tree using Huffman's algorithm
def make_huffman_tree(f):
    p = queue.PriorityQueue()
    # construct heap from frequencies, the initial items should be
    # the leaves of the final tree
    for c in f.keys():
      p.put(TreeNode(None,None,(f[c], c)))

    # greedily remove the two nodes x and y with lowest frequency,
    # create a new node z with x and y as children,
    # insert z into the priority queue (using an empty character "")
    while (p.qsize() > 1):
        # TODO
      # remove the two nodes x and y with lowest frequency
        x = p.get()
        y = p.get()
        # create a new node z with x and y as children
        z = TreeNode(x, y, (x.data[0] + y.data[0], ''))
        # insert z into the priority queue
        p.put(z)
        
    # return root of the tree
    return p.get()

# perform a traversal on the prefix code tree to collect all encodings
def get_code(node, prefix="", code={}):
    # TODO - perform a tree traversal and collect encodings for leaves in code
    if node.left is None and node.right is None:
        code[node.char] = prefix
    else:
        if node.left:
            get_code(node.left, prefix + "0", code)
        if node.right:
            get_code(node.right, prefix + "1", code)
    return code

    pass

# given an alphabet and frequencies, compute the cost of a fixed length encoding
def fixed_length_cost(f):
    # TODO
    # Find the length of the encoding of each character
    # Multiply the frequency of each character with its encoding length
    total_cost = sum([f[c] * 8 for c in f])
    return total_cost

    pass

# given a Huffman encoding and character frequencies, compute cost of a Huffman encoding
def huffman_cost(C, f):
    # TODO
    cost = 0
    for code, freq in zip(C.values(), f.values()):
      cost += len(code) * freq
    return cost


f = get_frequencies('fields.c')
#print(f)
print("Fixed-length cost:  %d" % fixed_length_cost(f))
T = make_huffman_tree(f)
C = get_code(T)
print("Huffman cost:  %d" % huffman_cost(C, f))
print((huffman_cost(C, f)) / (fixed_length_cost(f)))
