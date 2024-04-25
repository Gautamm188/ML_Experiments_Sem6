# class Graph:
#     def __init__(self):
#         self.graph = {}

#     def add_edge(self, node, neighbor, weight):
#         if node not in self.graph:
#             self.graph[node] = []
#         self.graph[node].append((neighbor, weight))

#     def greedy_search(self, start, goal):
#         if start not in self.graph or goal not in self.graph:
#             return None  # If start or goal nodes are not in the graph

#         visited = set()
#         path = [start]
#         current_node = start

#         while current_node != goal:
#             if current_node not in self.graph:
#                 return None  # If current_node is not in the graph

#             neighbors = self.graph[current_node]
#             neighbors.sort(key=lambda x: x[1])  # Sort by heuristic or cost
#             next_node = None

#             for neighbor, _ in neighbors:
#                 if neighbor not in visited:
#                     next_node = neighbor
#                     break

#             if next_node is None:
#                 # If no unvisited neighbors, backtrack
#                 path.pop()
#             else:
#                 # Move to the next node
#                 visited.add(next_node)
#                 path.append(next_node)
#                 current_node = next_node

#         return path

# # Example Usage:
# if __name__ == "__main__":
#     # Create a graph
#     my_graph = Graph()
#     my_graph.add_edge('A', 'B', 3)
#     my_graph.add_edge('A', 'C', 5)
#     my_graph.add_edge('B', 'D', 2)
#     my_graph.add_edge('B', 'E', 4)
#     my_graph.add_edge('C', 'F', 1)

#     # Perform Greedy Search
#     start_node = 'A'
#     goal_node = 'B'
#     result_path = my_graph.greedy_search(start_node, goal_node)

#     # Display the result
#     if result_path:
#         print(f"Greedy Search path from {start_node} to {goal_node}: {result_path}")
#     else:
#         print(f"No path found from {start_node} to {goal_node}")



import heapq

 

class Node:

    def __init__(self, state, cost, heuristic):

        self.state = state

        self.cost = cost

        self.heuristic = heuristic

 

    def __lt__(self, other):

        # Comparison method for priority queue

        return (self.cost + self.heuristic) < (other.cost + other.heuristic)

 

def best_first_search(initial_state, goal_state, heuristic_function, successors_function):

    priority_queue = []

    heapq.heappush(priority_queue, Node(initial_state, 0, heuristic_function(initial_state)))

 

    while priority_queue:

        current_node = heapq.heappop(priority_queue)

 

        if current_node.state == goal_state:

            print("Goal reached!")

            return current_node.state

 

        for successor_state, cost in successors_function(current_node.state):

            successor_node = Node(successor_state, current_node.cost + cost, heuristic_function(successor_state))

            heapq.heappush(priority_queue, successor_node)

 

    print("Goal not reached.")

    return None

 

# Example usage:

 

# Heuristic function (manhattan distance for illustrative purposes)

def heuristic(state):

    return abs(state[0] - goal_state[0]) + abs(state[1] - goal_state[1])

 

# Successors function (possible moves in this example)

def successors(state):

    x, y = state

    possible_moves = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]

    return [(move, 1) for move in possible_moves if 0 <= move[0] < 5 and 0 <= move[1] < 5]

 

# Initial and goal states

initial_state = (0, 0)

goal_state = (4, 4)

 

# Run the Best-First Search

best_first_search(initial_state, goal_state, heuristic, successors)

