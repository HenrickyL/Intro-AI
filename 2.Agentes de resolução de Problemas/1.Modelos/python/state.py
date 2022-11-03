from transition import Transition
class State:
    def __init__(self, name: str, edges = []):
        self.name = name
        self.edges = edges

    def __eq__(self, __o) :
        return self.name == __o.name

    def copy(self):
        res = State(self.name)
        res.edges = self.edges.copy()
        return res
    
    def getEdges(self):
        return [ [e.target,e.cost] for e in self.edges]
    def show(self):
        s = 'name: {0}\n'.format(self.name)
        s+= 'edge:\n'
        for e in self.edges:
            s+="\t({0},{1})\n".format(e.target,e.cost)
        print(s)