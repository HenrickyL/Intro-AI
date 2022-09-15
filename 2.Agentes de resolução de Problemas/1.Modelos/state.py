from transition import Transition



class State:
    def __init__(self, name: str, edges:list[Transition] = []):
        self.name = name
        self.edges = self._add_edges(edges)

    def _add_edges(self, edges: list[Transition]):
        for edge in edges:
            if self not in edge.target.edges:
                edge.target.edges.append(self)
        return edges.copy()

