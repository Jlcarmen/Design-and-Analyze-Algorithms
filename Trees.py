class Node:
    def __init__ (self,data):
        self.data = data
        self.left = None
        self.right = None

def inorder(node):
    if node:
        inorder(node.left)
        print (node.data, end= " ")
        inorder(node.right)

root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.left.left = Node(2)
root.right.right = Node(20)

print("Inorder Traversal (Left -> Root -> Right):")
inorder(root)