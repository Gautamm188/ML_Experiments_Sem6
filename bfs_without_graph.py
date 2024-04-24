from collections import deque
import time

def bfs_without_graph(start):
    neighbors = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F', 'G'],
        'D': ['B'],
        'E': ['B'],
        'F': ['C'],
        'G': ['C']
    }

    visited = set()
    queue = deque([start])

    start_time = time.time()  # Start the timer

    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            print(vertex, end=' ')
            visited.add(vertex)
            queue.extend(neighbor for neighbor in neighbors.get(vertex, []) if neighbor not in visited)

    end_time = time.time()  # Stop the timer
    elapsed_time = end_time - start_time
    print("\nTime taken:", elapsed_time, "seconds")

# Example usage:
start_vertex = 'A'
print("BFS starting from vertex", start_vertex, ":")
bfs_without_graph(start_vertex)
