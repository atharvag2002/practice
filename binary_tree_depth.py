
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def tree_depth(node):
    if not node:
        return 0
    return 1 + max(tree_depth(node.left), tree_depth(node.right))


def main():
    root = Node(1, Node(2), Node(3, Node(4), None))
    print(tree_depth(root))

if __name__ == "__main__":
    main()
