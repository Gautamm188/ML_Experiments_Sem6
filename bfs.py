from collections import deque
import time

def bfs(graph, start, end):
    start_time = time.time()

    visited = set()
    paths = []
    queue = deque([(start, [start])])

    while queue:
        current, path = queue.popleft()
        if current == end:
            print("Path found:", ' -> '.join(map(str, path)))
            paths.append(path)

        visited.add(current)
        queue.extend((neighbor, path + [neighbor]) for neighbor in graph[current] if neighbor not in visited)

    elapsed_time = time.time() - start_time
    print(f"Time taken for BFS: {elapsed_time:.6f} seconds")

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
    print("BFS output:")
    bfs(graph, start_node, end_node)