class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


def get_height(node):
    return node.height if node else 0


def get_balance(node):
    return get_height(node.left) - get_height(node.right) if node else 0


def rotate_right(y):
    x = y.left
    T2 = x.right
    x.right = y
    y.left = T2
    y.height = max(get_height(y.left), get_height(y.right)) + 1
    x.height = max(get_height(x.left), get_height(x.right)) + 1
    return x


def rotate_left(x):
    y = x.right
    T2 = y.left
    y.left = x
    x.right = T2
    x.height = max(get_height(x.left), get_height(x.right)) + 1
    y.height = max(get_height(y.left), get_height(y.right)) + 1
    return y


def insert_avl(root, key):
    if not root:
        return AVLNode(key)
    if key < root.key:
        root.left = insert_avl(root.left, key)
    else:
        root.right = insert_avl(root.right, key)

    root.height = max(get_height(root.left), get_height(root.right)) + 1
    balance = get_balance(root)

    # Left Left
    if balance > 1 and key < root.left.key:
        return rotate_right(root)

    # Right Right
    if balance < -1 and key > root.right.key:
        return rotate_left(root)

    # Left Right
    if balance > 1 and key > root.left.key:
        root.left = rotate_left(root.left)
        return rotate_right(root)

    # Right Left
    if balance < -1 and key < root.right.key:
        root.right = rotate_right(root.right)
        return rotate_left(root)

    return root


def preorder_avl(root):
    if root:
        print(root.key, end=" ")
        preorder_avl(root.left)
        preorder_avl(root.right)


# Example Usage
root_avl = None
orders_avl = ["Order 5", "Order 2", "Order 8", "Order 1", "Order 3"]
for order in orders_avl:
    root_avl = insert_avl(root_avl, order)

print("Preorder Traversal of AVL Tree:")
preorder_avl(root_avl)
