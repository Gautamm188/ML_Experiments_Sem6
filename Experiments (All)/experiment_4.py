import heapq

class Node:
    def __init__(self, state, parent=None, g=0, h=0):
        self.state = state
        self.parent = parent
        self.g = g  # Cost from start node to current node
        self.h = h  # Heuristic estimate from current node to goal

    def __lt__(self, other):
        # Comparison function for priority queue based on total cost (f = g + h)
        return (self.g + self.h) < (other.g + other.h)

def astar_search(start, goal, heuristic):
    open_set = []
    closed_set = set()

    start_node = Node(state=start, g=0, h=heuristic(start))
    heapq.heappush(open_set, start_node)

    while open_set:
        current_node = heapq.heappop(open_set)

        if current_node.state == goal:
            return reconstruct_path(current_node)

        closed_set.add(current_node.state)

        for neighbor in get_neighbors(current_node.state):
            if neighbor in closed_set:
                continue

            g_score = current_node.g + 1  # Assuming uniform edge cost

            # Check if the neighbor is not in the open set or has a lower cost
            neighbor_node = Node(state=neighbor, parent=current_node, g=g_score, h=heuristic(neighbor))
            if neighbor_node not in open_set or g_score < neighbor_node.g:
                heapq.heappush(open_set, neighbor_node)

    return None  # No path found

def reconstruct_path(node):
    path = []
    while node:
        path.append(node.state)
        node = node.parent
    return path[::-1]

def get_neighbors(state):
    x, y = state
    # Define possible movements (up, down, left, right)
    movements = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
    # Filter out movements that go out of bounds or are invalid
    valid_neighbors = [(nx, ny) for nx, ny in movements if 0 <= nx < 5 and 0 <= ny < 5]  # Adjust bounds according to your problem
    return valid_neighbors


# Example usage:
start_state = (0, 0)
goal_state = (4, 4)

# Example heuristic function (Euclidean distance in this case)
def euclidean_distance_heuristic(state):
    return ((state[0] - goal_state[0]) ** 2 + (state[1] - goal_state[1]) ** 2) ** 0.5

path = astar_search(start_state, goal_state, heuristic=euclidean_distance_heuristic)
print("A* Search Path:", path)
