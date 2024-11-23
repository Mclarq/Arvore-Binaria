class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root

def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.val, end=' ')
        inorder_traversal(root.right)

# Exemplo de uso:
root = Node(10)
root = insert(root, 20)
root = insert(root, 5)
root = insert(root, 8)
root = insert(root, 15)

print("Traversal Inorder da árvore binária:")
inorder_traversal(root)
