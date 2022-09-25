from state import State
from igraph import *
from transition import Transition
class Map:
    def __init__(self, states:list[State]):
        self.states = states.copy()
    def showStates(self):
        for state in self.states:
            state.show()
    def showCitys(self):
        setStates = {state.name:i for i,state in zip(range(len(self.states)),self.states)}
        print(setStates)
    def readData(data:str):
        with open(data,'r') as file:
            states = []
            for line in file.readlines():
                city, city_targets = line.split(':')
                city = city.strip()
                city_targets = city_targets.strip()

                edges = []
                if(city_targets):
                    for transiction in city_targets.split(','):
                        target, cost = transiction.strip().split('-')
                        edges.append(Transition(target=target, cost=cost))
                state = State(city, edges)
                
                states.append(state)
        return Map(states)
    def draw(self, layout=None):
        g=Graph()
        g.add_vertices(len(self.states))
        i =0
        edge = []
        weights = []
        setStates = {state.name:i for i,state in zip(range(len(self.states)),self.states)}
        get = lambda name: setStates.get(name)
        for state in self.states:
            g.vs[i]["id"]= get(state.name)
            g.vs[i]["label"]= state.name
            for e in state.edges:
                edge.append((get(state.name),get(e.target)))
                weights.append(e.cost)
            i +=1
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



