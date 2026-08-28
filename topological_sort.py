
from collections import defaultdict, deque

def topological_sort(vertices, edges):
    graph = defaultdict(list)
    in_degree = {v: 0 for v in vertices}
    
    for u, v in edges:
        graph[u].append(v)
        in_degree[v] += 1
    
    queue = deque([v for v in vertices if in_degree[v] == 0])
    result = []
    
    while queue:
        vertex = queue.popleft()
        result.append(vertex)
        
        for neighbor in graph[vertex]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    if len(result) != len(vertices):
        return None  # Cycle detected
    
    return result


def main():
    vertices = ['A', 'B', 'C', 'D', 'E', 'F']
    edges = [('A', 'D'), ('B', 'D'), ('D', 'E'), ('C', 'E'), ('E', 'F')]
    result = topological_sort(vertices, edges)
    print(f"Topological sort: {result}")


if __name__ == "__main__":
    main()
