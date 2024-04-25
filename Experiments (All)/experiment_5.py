from sys import maxsize
from itertools import permutations

V = 4

def travellingSalesmanProblem(graph, s):
    # Store all vertices apart from the source vertex
    vertex = [i for i in range(V) if i != s]

    # Store minimum weight
    min_path = maxsize

    # Generate all possible permutations of remaining vertices
    next_permutation = permutations(vertex)
    
    # Iterate over each permutation
    for perm in next_permutation:
        # Store current path weight (cost)
        current_pathweight = 0
        k = s

        # Compute current path weight
        for j in perm:
            current_pathweight += graph[k][j]
            k = j

        # Add weight to return to the source vertex
        current_pathweight += graph[k][s]

        # Update minimum path weight
        min_path = min(min_path, current_pathweight)

    return min_path

if __name__ == "__main__":
    # Matrix representation of graph
    graph = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]
    s = 0
    print("ANS:")
    print(travellingSalesmanProblem(graph, s))
