from state import State
from igraph import *
class Map:
    def __init__(self, states:list[State]):
        self.states = states.copy()
    def draw(self, layout=None):
        g=Graph()
        g.add_vertices(len(self.states))
        i =0
        edge = []
        weights = []
        setStates = {state.name:i for i,state in zip(range(len(self.states)),self.states)}
        print('>>',setStates)
        get = lambda name: setStates.get(name)
        for state in self.states:
            g.vs[i]["id"]= get(state.name)
            g.vs[i]["label"]= state.name
            for e in state.edges:
                edge.append((get(state.name),get(e.target)))
                weights.append(e.cost)
            i +=1
        print(edge)
        g.add_edges(edge)
        g.es['weight'] = weights
        g.es['label'] = weights
        visual_style = {}
        visual_style["vertex_size"] = 12
        visual_style["vertex_color"] = 'yellow'
        visual_style["vertex_shape"] = 'square'
        visual_style["vertex_label_dist"] = 2
        visual_style["margin"] = 50
        visual_style["bbox"] = (400,400)
        if(layout):
            layout = g.layout(layout)
            plot(g, **visual_style,target='map.png', layout=layout)

        else:
            plot(g, **visual_style,target='map.png')



