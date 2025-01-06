class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def insert(root, key):
    if root is None:
        return TreeNode(key)
    if key < root.val:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root


def inorder(root):
    if root:
        inorder(root.left)
        print(root.val, end=" ")
        inorder(root.right)


# Example Usage
root = None
medicines = ["Paracetamol", "Ibuprofen", "Aspirin"]
for med in medicines:
    root = insert(root, med)

print("Inorder Traversal of Medicines:")
inorder(root)
