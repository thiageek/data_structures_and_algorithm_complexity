import sys

class Dijkstra:
    INFINITE = 99999999999
    def __init__(self, graph, weights, start = 1):
        self.graph = graph
        self.weights = weights
        self.start = start
        self.distanceMap = {}
        self.path = {}
        self.initialize()
        self.run()
    
    def initialize(self):
        for node in self.graph:
            self.distanceMap[node] = self.INFINITE
            self.path[node] = -1
        self.distanceMap[self.start] = 0
        
    def relax(self, origin, target, weight):
        localPath = self.distanceMap[origin] + weight
        if(self.distanceMap[target] > localPath and weight > 0):
            self.distanceMap[target] = localPath
            self.path[target] = origin
    
    def run(self):
        while(len(self.graph) > 1):
            origin = self.graph.pop(0)
            for index in range(len(self.weights[origin])):
                target = origin + 1 + index
                self.relax(origin, target, self.weights[origin][index])


if __name__ == "__main__":
    file = open(sys.argv[1], 'r')

    numberOfNodes = int(file.readline().replace('\n', ''))
    graph = list(range(1, numberOfNodes + 1))
    
    weights = {}
    key = 1
    for line in file:
        weights[key] = []
        weightsForKey = line.split(' ')
        for pathFromKey in range(len(weightsForKey)):
            weights[key].append(int(weightsForKey[pathFromKey].replace('\n', '')))
        key += 1
    
    file.close()
    
    print(Dijkstra(graph, weights).path)
