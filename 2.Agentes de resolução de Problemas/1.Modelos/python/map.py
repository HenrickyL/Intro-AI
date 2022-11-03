from PriorityQueue import PriorityQueue
from node import Node
from state import State
from igraph import *
from transition import Transition
import json

class Map:
    def __init__(self, states):
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
        return None
    #Breadth First Search
    @staticmethod
    def bfs(map, ini:str, fin: str, isPrint=False):
        initialState = map.states[ini]
        node = Node(initialState)
        edge  = [node] #queue
        read = set()
        while(edge):
            if(isPrint):
                print([e.state.name for e in edge])
            node = edge.pop(0)
            read.add(node.state.name)
            for e in node.state.edges:
                child = Node(map.states[e.target] , e.cost+node.cost, node)
                if(child.state.name not in [key for key in read] and child.state.name not in [e.state.name for e in edge]):
                    if(child.state.name == fin):
                        return child
                    edge.append(child)
        return None
    #Depth-first search
    @staticmethod
    def dfs(map, ini:str, fin: str, isPrint=False)-> Node:
        initialState = map.states[ini]
        node = Node(initialState)
        edge  = [node] #stack
        read = set()
        while(edge):
            if(isPrint):
                print([e.state.name for e in edge])
            node = edge.pop()
            read.add(node.state.name)
            for e in node.state.edges:
                child = Node(map.states[e.target] , e.cost+node.cost, node)
                if(child.state.name not in [key for key in read] and child.state.name not in [e.state.name for e in edge]):
                    if(child.state.name == fin):
                        return child
                    edge.append(child)
        return None
                
    def compare(x, y, method)-> bool:
        return  method(x,y)

    #------------------------------------------------    
    @classmethod
    def _search(cls, map, ini:str, fin: str, compare, isPrint:bool = True ):
        initialState = map.states[ini]
        node = Node(initialState)
        f = compare
        edge : PriorityQueue[Node] = PriorityQueue(fn=f)
        edge.insert(node)
        read = []
        while(edge):
            if(isPrint):
                print([f'{e.state.name}-{e.cost}' for e in edge.queue])
            node: Node = edge.delete()
            if node.state.name == fin:
                return node
            read.append(node)
            for e in node.state.edges:
                child = Node(map.states[e.target], e.cost + node.cost, node)
                if(child.state.name not in [e.state.name for e in [*edge.queue, *read]]):
                    edge.insert(child)
                elif child.state.name in [x.state.name for x in edge.queue]:
                    another : Node= edge.remove(child)
                    if(f(child, another)):
                        edge.insert(child)
                    else:
                        edge.insert(another)
        return None
    #------------------------------------------------    
    @classmethod
    def ucs(cls,map, ini:str, fin: str, isPrint=False):
        f  = lambda x,y : x.cost < y.cost
        return cls._search(map, ini, fin, f, isPrint=isPrint)

    ####################################################################
    @staticmethod
    def readDistanceMap(path : str)  :
        with open(path,'r') as file:
            return json.load(file)

    def _makeHeuristic(distanceMap ):
        return lambda x: distanceMap[x.state.name]

    @classmethod
    def gcs(cls, map, ini:str, fin: str, distanceMap , isPrint=False):
        h =  cls._makeHeuristic(distanceMap)
        f = lambda x,y: h(x) < h(y)
        return cls._search(map,ini,fin,f, isPrint=isPrint)

    @classmethod
    def aStar(cls, map, ini:str, fin: str, distanceMap, isPrint=False):
        h = cls._makeHeuristic(distanceMap)
        fn = lambda node:  h(node) + node.cost
        f = lambda x,y: fn(x)< fn(y)
        return cls._search(map,ini,fin,f, isPrint=isPrint)

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