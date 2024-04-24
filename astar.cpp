#include <iostream>
#include <fstream>
#include <unordered_map>
#include <vector>
#include <queue>
#include <cmath>

using namespace std;

struct City {
    int x, y;
    City(int x, int y) : x(x), y(y) {}
};

struct Edge {
    string destination;
    int distance;
    Edge(string dest, int dist) : destination(dest), distance(dist) {}
};

unordered_map<string, vector<Edge>> createGraph() {
    ifstream file("citiesGraph.txt");
    unordered_map<string, vector<Edge>> graph;

    string source, destination;
    int distance;
    while (file >> source >> destination >> distance) {
        graph[source].push_back(Edge(destination, distance));
        graph[destination].push_back(Edge(source, distance));
    }
    return graph;
}

unordered_map<string, City> getCity() {
    ifstream file("cities.txt");
    unordered_map<string, City> cities;
    string name;
    int x, y;
    while (file >> name >> x >> y) {
        cities[name] = City(x, y);
    }
    return cities;
}

int heuristic(const City& a, const City& b) {
    return sqrt(pow(a.x - b.x, 2) + pow(a.y - b.y, 2));
}

vector<string> Astar(const string& startNode, const string& goalNode, const unordered_map<string, vector<Edge>>& graph,
                     const unordered_map<string, City>& cities) {
    priority_queue<pair<int, string>, vector<pair<int, string>>, greater<pair<int, string>>> priorityQueue;
    unordered_map<string, int> distance;
    unordered_map<string, string> parent;
    vector<string> path;

    priorityQueue.push(make_pair(0, startNode));
    distance[startNode] = 0;

    while (!priorityQueue.empty()) {
        string current = priorityQueue.top().second;
        priorityQueue.pop();

        if (current == goalNode) {
            string node = current;
            while (node != startNode) {
                path.push_back(node);
                node = parent[node];
            }
            path.push_back(startNode);
            reverse(path.begin(), path.end());
            return path;
        }

        for (const Edge& edge : graph.at(current)) {
            int cost = distance[current] + edge.distance;
            if (!distance.count(edge.destination) || cost < distance[edge.destination]) {
                distance[edge.destination] = cost;
                int priority = cost + heuristic(cities.at(edge.destination), cities.at(goalNode));
                priorityQueue.push(make_pair(priority, edge.destination));
                parent[edge.destination] = current;
            }
        }
    }

    return path;
}

int main() {
    auto graph = createGraph();
    auto cities = getCity();

    string startNode = "Arad";
    string goalNode = "Bucharest";

    vector<string> path = Astar(startNode, goalNode, graph, cities);

    cout << "Shortest path from " << startNode << " to " << goalNode << ":" << endl;
    for (const string& city : path) {
        cout << city << " ";
    }
    cout << endl;

    return 0;
}
