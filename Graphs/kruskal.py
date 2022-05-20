import sys

class WeightBranch:
    def __init__(self, originNode, targetNode, weight):
        self.originNode = originNode
        self.targetNode = targetNode
        self.weight = weight
    
    def __repr__(self):
        return "(%s, %s: %s)" % (self.originNode, self.targetNode, self.weight)


class OrderedWeightBranches:
    def __init__(self):
        self.set = []

    def addBranch(self, branch):
        self.set.append(branch)
        for index in range(len(self.set) - 1, 0, -1):
            if(self.set[index].weight < self.set[index - 1].weight):
                self.set[index], self.set[index - 1] = self.set[index - 1], self.set[index]


class Node:
    def __init__(self, value):
        self.value = value
        self.setRoot = value
    
    def __repr__(self):
        return "%s" % self.value

class NodeSet:
    def __init__(self):
        self.set = []
    
    def add(self, node):
        if(len(self.set) > 0):
            node.setRoot = self.set[0].value
        self.set.append(node)
    
    def __repr__(self):
        return "[" + ", ".join(str(node.value) for node in self.set) + "]"

class MinimumSpanningTree:
    numberOfNodes = 0
    def __init__(self, filename):
        self.sets = []
        self.weightBranches = OrderedWeightBranches()
        self.buildDataFromFile(filename)
        self.populateSets()
        self.run()

    def findSet(self, value):
        for nodeSet in self.sets:
            for node in nodeSet.set:
                if(node.value == value):
                    return nodeSet
        return -1
    
    def mergeSets(self, firstSet, secondSet):
        largerSet, smallerSet = firstSet, secondSet
        if(len(secondSet.set) > len(firstSet.set)):
            largerSet, smallerSet = secondSet, firstSet
        for node in smallerSet.set:
            largerSet.add(node)
        self.sets.remove(smallerSet)

    def buildDataFromFile(self, filename):
        file = open(filename, 'r')
        self.numberOfNodes = int(file.readline().replace('\n', ''))
        originNode = 0
        for line in file:
            originNode += 1
            targetNode = originNode + 1
            weights = line.split(' ')
            for weight in weights:
                if(int(weight) > 0):
                    self.weightBranches.addBranch(WeightBranch(originNode, targetNode, weight.replace('\n', '')))
                targetNode += 1

    def populateSets(self):
        for value in range(1, self.numberOfNodes + 1):
            nodeSet = NodeSet()
            nodeSet.add(Node(value))
            self.sets.append(nodeSet)

    def run(self):
        path = []
        for branch in self.weightBranches.set:
            originSet = self.findSet(branch.originNode)
            targetSet = self.findSet(branch.targetNode)
            if(originSet != targetSet):
                path.append(branch)
                self.mergeSets(originSet, targetSet)
        print(path)
        print(self.sets)


if __name__ == "__main__":
    MinimumSpanningTree(sys.argv[1])
