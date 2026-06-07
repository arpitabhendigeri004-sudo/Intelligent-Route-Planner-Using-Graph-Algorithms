class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, source, destination, weight):
        if source not in self.graph:
            self.graph[source] = []

        if destination not in self.graph:
            self.graph[destination] = []

        self.graph[source].append((destination, weight))
        self.graph[destination].append((source, weight))

    def display_graph(self):
        print("\nCity Road Network:\n")

        for node in self.graph:
            print(f"{node} -> {self.graph[node]}")