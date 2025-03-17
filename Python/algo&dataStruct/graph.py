class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graph_dict: dict[str, list[str]] = {}

        for start, end in self.edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]

    def get_paths(self, start, end, path=[]):
        if start not in self.graph_dict:
            return []
        path = path + [start]

        if start == end:
            return [path]

        paths = []
        for node in self.graph_dict[start]:
            new_paths = self.get_paths(node, end, path)
            for p in new_paths:
                paths.append(p)
        return paths

    def get_shortest_path(self, start, end):
        paths = self.get_paths(start, end)

        if not len(paths):
            return None

        if len(paths) == 1:
            return paths[0]

        min = paths[0]
        for idx in range(1, len(paths)):
            if len(path[idx]) < len(min):
                min = path[idx]
        return min


if __name__ == "__main__":
    routes = [
        ("Mumbai", "Paris"),
        ("Mumbai", "Dubai"),
        ("Texas", "Washington"),
        ("Paris", "Dubai"),
        ("Paris", "New York"),
        ("Dubai", "New York"),
        ("Washington", "New Jersey"),
        ("New York", "Toronto"),
    ]

    route_graph = Graph(routes)
    path = route_graph.get_paths("Mumbai", "New York")
    shortest = route_graph.get_shortest_path("New York", "New York")
    print(path)
    print(shortest)
