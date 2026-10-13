
def iterative_deepening_dfs(graph, start, goal):
    def dls(node, depth, visited):
        if depth == 0:
            return node == goal
        if node == goal:
            return True
        visited.add(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                if dls(neighbor, depth - 1, visited.copy()):
                    return True
        return False
    
    depth = 0
    while True:
        visited = set()
        if dls(start, depth, visited):
            return depth
        depth += 1


def main():
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }
    start, goal = 'A', 'F'
    depth = iterative_deepening_dfs(graph, start, goal)
    print(f"Goal '{goal}' found at depth {depth}")


if __name__ == "__main__":
    main()
