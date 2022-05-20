import sys

class Prim():
    INFINITE = 99999999999
    def __init__(self, graph, weights, start = 1):
        self.graph = graph
        self.weights = weights
        self.position = start
        self.distanceMap = {}
        self.path = {}
        self.buildDistanceMap()
        self.run()
    
    def buildDistanceMap(self):
        for node in self.graph:
            self.distanceMap[node] = self.INFINITE
        self.distanceMap[self.position] = 0
        self.path[self.position] = -1

    def run(self):
        while(len(self.graph) > 1):
            origin = self.graph.pop(0)
            for index in range(len(self.weights[origin])):
                target = origin + 1 + index
                if (target in self.graph and self.weights[origin][index] > 0 and self.weights[origin][index] < self.distanceMap[target]):
                    self.path[target] = origin
                    self.distanceMap[target] = self.weights[origin][index]
        

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
    
    print(Prim(graph, weights).path)
