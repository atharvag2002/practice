
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def depth_first_search(root):
    if not root:
        return []
    return [root.value] + depth_first_search(root.left) + depth_first_search(root.right)


def main():
    root = Node(1, Node(2), Node(3))
    print(depth_first_search(root))

if __name__ == "__main__":
    main()
