# File: Topic6/tree_hierarchical_data.py

class TreeNode:
    def __init__(self, name):
        self.name = name
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def display(self, level=0):
        print(" " * level * 4 + self.name)
        for child in self.children:
            child.display(level + 1)

# Example: Representing medicine categories and subcategories
root = TreeNode("Medicine")

pain_relievers = TreeNode("Pain Relievers")
pain_relievers.add_child(TreeNode("Paracetamol"))
pain_relievers.add_child(TreeNode("Ibuprofen"))

antibiotics = TreeNode("Antibiotics")
antibiotics.add_child(TreeNode("Amoxicillin"))
antibiotics.add_child(TreeNode("Ciprofloxacin"))

antihistamines = TreeNode("Antihistamines")
antihistamines.add_child(TreeNode("Cetirizine"))
antihistamines.add_child(TreeNode("Loratadine"))

root.add_child(pain_relievers)
root.add_child(antibiotics)
root.add_child(antihistamines)

# Display the hierarchical structure
root.display()
