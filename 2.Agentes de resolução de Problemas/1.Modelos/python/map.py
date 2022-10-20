from asyncio.windows_events import NULL
from PriorityQueue import PriorityQueue
from node import Node
from state import State
from igraph import *
from transition import Transition

class Map:
    def __init__(self, states:dict[str, State]):
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
    def bfs(map:'Map', ini:str, fin: str):
        initialState = map.states[ini]
        node = Node(initialState)
        edge  = [node] #queue
        read = set()
        while(edge):
            print([e.state.name for e in edge])
            node = edge.pop(0)
            read.add(node.state.name)
            for e in node.state.edges:
                child = Node(map.states[e.target] , e.cost, node)
                if(child.state.name not in [key for key in read] and child.state.name not in [e.state.name for e in edge]):
                    if(child.state.name == fin):
                        return child
                    edge.append(child)
        return None
    #Depth-first search
    @staticmethod
    def dfs(map:'Map', ini:str, fin: str)-> Node:
        initialState = map.states[ini]
        node = Node(initialState)
        edge  = [node] #stack
        read = set()
        while(edge):
            print([e.state.name for e in edge])
            node = edge.pop()
            read.add(node.state.name)
            for e in node.state.edges:
                child = Node(map.states[e.target] , e.cost, node)
                if(child.state.name not in [key for key in read] and child.state.name not in [e.state.name for e in edge]):
                    if(child.state.name == fin):
                        return child
                    edge.append(child)
        return None
                
                

    @staticmethod
    def ucs(map:'Map', ini:str, fin: str):
        initialState = map.states[ini]
        node = Node(initialState)
        edge = PriorityQueue()
        edge.insert(node)
        read = []
        while(edge):
            print([e.state.name for e in edge.queue])
            node: Node = edge.delete()
            if node.state.name == fin:
                return node
            read.append(node)
            for e in node.state.edges:
                child = Node(map.states[e.target], e.cost + node.cost, node)
                if(child.state.name not in [e.state.name for e in [*edge.queue, *read]]):
                    edge.insert(child)
                elif child in edge:
                    another = edge.remove(child)
                    edge.insert(min(child, another))
        return None

    ####################################################################    
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
                        edges.append(Transition(target=target, cost=int(cost)))
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