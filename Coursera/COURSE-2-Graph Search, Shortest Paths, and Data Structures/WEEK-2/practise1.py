from ast import literal_eval
from collections import defaultdict
class Dijkstra:
    def __init__(self, filename):
        self.graph = {}
        with open(filename) as file:
            for line in file:
                inf = line.split()
                self.graph[int(inf[0])] = [literal_eval(x) for x in inf[1:]]

    def find_lowest_cost_node(self, costs):
        lowest_cost = float('inf')
        lowest_cost_node = None
        for node in costs: 
            cost = costs[node]
            if cost < lowest_cost and node not in processed: 
                lowest_cost = cost 
                lowest_cost_node = node
        return lowest_cost_node

    def shortest_paths(self):
        costs = defaultdict()
        processed = []
        source = 1
        node = self.find_lowest_cost_node(self.graph[source]) 
        while node is not None: 
            cost = costs[node]
            neighbors = self.graph[node]
            for n in neighbors.keys(): 
                new_cost = cost + neighbors[n] 
                if costs[n] > new_cost:
                    costs[n] = new_cost
                    parents[n] = node 
            processed.append(node) 
            node = self.find_lowest_cost_node(costs) 

    
if __name__ == '__main__':
    path_finder = Dijkstra('dijkstraData.txt')
    paths = path_finder.shortest_paths()
    actual = {vertex: distance[0] for (vertex, distance) in paths.items()}
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