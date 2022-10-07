from asyncio.windows_events import NULL
from state import State
from igraph import *
from transition import Transition
class Map:
    def __init__(self, states:dict[State]):
        self.states = states.copy()
        self.listStates = []
    def showStates(self):
        for name in self.states:
            self.states[name].show()
    def showCitys(self):
        setStates = {state.name:i for i,state in zip(range(len(self.states)),self.states)}
        print(setStates)
    def getByName(self, name:str):
        for s in self.states:
            if(s.name == name):
                return s
        return NULL
    #Breadth First Search
    @staticmethod
    def bds(map:'Map', ini:str, fin: str):
        edge  = [ini]
        read = set()
        while(edge):
            print(edge)
            name = edge.pop(0)
            node = State(name)
            read.add(name)
            for e in map.states[name].edges:
                child = State(e.target)
                child.father = name
                node.edges.append(e.target)
                if(child.name not in read or child.name not in edge):
                    if(child.name == fin):
                        return child
                    edge.append(child.name)  
                
                
    def readData(data:str):
        with open(data,'r') as file:
            states = {}
            lState = []
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
                lState.append(state)
                states[city]=state
        res = Map(states)
        res.listStates = lState
        return res
    def draw(self, layout=None):
        g=Graph()
        g.add_vertices(len(self.listStates))
        i =0
        edge = []
        weights = []
        setStates = {state.name:i for i,state in zip(range(len(self.listStates)),self.listStates)}
        get = lambda name: setStates.get(name)
        for state in self.listStates:
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



