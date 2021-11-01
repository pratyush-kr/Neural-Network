class Neuron:
    def __init__(self, id:int):
        self.id = id
        self.adj = []
        self.bias = 1
    def addConnection(self, previous:int):
        self.adj.append(previous)

if __name__ == '__main__':
    l1 = []
    l2 = Neuron(3)
    l1.append(Neuron(1))
    l1.append(Neuron(2))