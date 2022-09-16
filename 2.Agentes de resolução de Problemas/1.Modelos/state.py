from transition import Transition
class State:
    def __init__(self, name: str, edges:list[Transition] = []):
        self.name = name
        self.edges = edges
    def getEdges(self):
        return [ [e.target,e.cost] for e in self.edges]
    def show(self):
        s = 'name: {0}\n'.format(self.name)
        s+= 'edge:\n'
        for e in self.edges:
            s+="\t({0},{1})\n".format(e.target,e.cost)
        print(s)
    # def _add_edges(self, edges: list[Transition]):
    #     for edge in edges:
    #         if self not in edge.target.edges:
    #             edge.target.edges.append(self)
    #     return edges.copy()

