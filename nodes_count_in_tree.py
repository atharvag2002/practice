
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def nodes_count_in_tree(node):
    if not node:
        return 0
    return 1 + nodes_count_in_tree(node.left) + nodes_count_in_tree(node.right)


def main():
    root = Node(1, Node(2), Node(3))
    print(nodes_count_in_tree(root))

if __name__ == "__main__":
    main()
