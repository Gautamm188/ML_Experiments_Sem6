from collections import deque
import time

def dfs(graph, start, end):
    start_time = time.time()

    visited = set()
    paths = []
    stack = [(start, [start])]

    while stack:
        current, path = stack.pop()
        if current == end:
            print("Path found:", ' -> '.join(map(str, path)))
            paths.append(path)

        visited.add(current)
        stack.extend((neighbor, path + [neighbor]) for neighbor in graph[current] if neighbor not in visited)

    elapsed_time = time.time() - start_time
    print(f"Time taken for DFS: {elapsed_time:.6f} seconds")

if __name__ == "__main__":
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F', 'G', 'H'],
        'D': ['B'],
        'E': ['B'],
        'F': ['C'],
        'G': ['C'],
        'H': ['C']
    }

    start_node = 'A'
    end_node = 'G'
    print("DFS output:")
    dfs(graph, start_node, end_node)
