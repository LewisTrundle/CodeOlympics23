import sys

tree = []
# Creating node class
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
# Function to insert in BST
    def insert(self, data):
        # if value is lesser than the value of the parent node
        if data < self.data:
            if self.left:
                # if we still need to move towards the left subtree
                self.left.insert(data)
            else:
                self.left = Node(data)
        # if value is greater than the value of the parent node        
        else:
            if self.right:
                # if we still need to move towards the right subtree
                self.right.insert(data)
            else:
                self.right = Node(data)

    def tolist(self):
        tree.append(self)
        if self.left:
            self.left.tolist()
        if self.right:
            self.right.tolist()

    # function to print a BST
    def PrintTree(self):
        print(self.data)
        if self.left:
            self.left.PrintTree()
        if self.right:
            self.right.PrintTree()
    
    def get_left(self):
        if self.left:
            return self.left.data
    
    def get_right(self):
        if self.right:
            return self.right.data

    # Function to search in BST
    def search(self, val):
        for node in tree:
            if node.data == val:
                return node

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.left.left.left = Node(8)
root.left.left.right = Node(9)
root.left.right.left = Node(10)
root.left.right.right = Node(11)
root.right.left.left = Node(12)
root.right.left.right = Node(13)
root.right.right.left = Node(14)
root.right.right.right = Node(15)
root.tolist()

def two_edge_checker(a, b):
    if a > b or a < 1 or b < 1 or a > 15 or b > 15:
        return

    a = root.search(a)
    if a is not None and (a.get_left() == b or a.get_right() == b):
        print("Yes")
    else:
        print("No")

# print(two_edge_checker(3, 6))

# for i in range(1, 16):
#     for j in range(1, 16):
#         if i != j:
#             print(f"({i}, {j}): {two_edge_checker(i, j)}")

for line in sys.stdin:
    two_edge_checker(int(line.split()[0]), int(line.split()[1]))