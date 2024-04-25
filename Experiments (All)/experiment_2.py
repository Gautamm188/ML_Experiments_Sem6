class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, node, neighbors):
        self.graph[node] = neighbors

    def dfs(self, start_node, goal_node):
        visited = set()
        stack = [start_node]

        while stack:
            current_node = stack.pop()

            if current_node == goal_node:
                print(f"Goal node {goal_node} found!")
                return True

            if current_node not in visited:
                visited.add(current_node)
                print(f"Visiting node {current_node}")

                neighbors = self.graph.get(current_node, [])
                stack.extend(neighbors[::-1])  # Reverse the neighbors and add to stack

        print(f"Goal node {goal_node} not found!")
        return False

# Example Usage:
if __name__ == "__main__":
    my_graph = Graph()
    my_graph.add_edge('A', ['B', 'C'])
    my_graph.add_edge('B', ['D', 'E'])
    my_graph.add_edge('C', ['F', 'G'])
    my_graph.add_edge('D', [])
    my_graph.add_edge('E', [])
    my_graph.add_edge('F', [])
    my_graph.add_edge('G', [])

    start_node = 'A'
    goal_node = 'G'    # change the goal node to change the outcomes f the output

    my_graph.dfs(start_node, goal_node)



