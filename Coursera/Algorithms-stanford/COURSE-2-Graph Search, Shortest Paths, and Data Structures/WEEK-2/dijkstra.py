from ast import literal_eval

class Dijkstra:
    def __init__(self, filename):
        self.graph = {}
        with open(filename) as file:
            for line in file:
                inf = line.split()
                self.graph[int(inf[0])] = [literal_eval(x) for x in inf[1:]]
        self.source = 1

    
    def shortest_path(self, source=None):
        if source is None:
            source = self.source
        shortest_paths = {}
        visited = set()
        for vertex in self.graph.keys():
            shortest_paths[vertex] = (float('inf'), [])
        shortest_paths[source] = (0, [])
        visited.add(source)
        while set(self.graph.keys() - visited):
            source, min_edge = -1, ()
            for vertex in visited:
                for edge in self.graph[vertex]:
                    if edge[0] in visited:
                        continue
                    if not min_edge or shortest_paths[vertex][0] + edge[1] < min_edge[1]:
                        min_edge = (edge[0], shortest_paths[vertex][0] + edge[1])
                        source = vertex
            shortest_paths[min_edge[0]] = (min_edge[1], shortest_paths[source][1] + [min_edge[0]])
            visited.add(min_edge[0])
        return shortest_paths
if __name__ == '__main__':
    path_finder = Dijkstra('dijkstraData.txt')
    paths = path_finder.shortest_path()
    actual = {vertex: distance[0] for (vertex, distance) in paths.items()}
    # for i in range(1, 15):
    #     print(paths[i])
    print(actual[7])
    print(actual[37])
    print(actual[59])
    print(actual[82])
    print(actual[99])
    print(actual[115])
    print(actual[133])
    print(actual[165])
    print(actual[188])
    print(actual[197])


            