#create nary tree
import random as rand

def find_len_child(child):
    return len(child)

class NaryTree:
    def __init__(self, key):
        self.key = key
        self.child = []


if __name__ == "__main__":
    root = NaryTree(10)
    root.child.append(NaryTree(2))
    root.child.append(NaryTree(100))
    root.child.append(NaryTree(125))
    leng = find_len_child(root.child)
    for i in range(leng):
        root.child[i].child.append(NaryTree(rand.randrange(9)))
        root.child[i].child.append(NaryTree(rand.randrange(9)))
    
    print("Done")
