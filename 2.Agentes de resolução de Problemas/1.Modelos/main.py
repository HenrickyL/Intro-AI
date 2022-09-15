from map import Map
from state import State
from transition import Transition

with open('data.txt','r') as file:
    line = file.readline()
    city, city_targets = line.split(':')
    
    edges = []
    for transiction in city_targets.split(','):
        target, cost = transiction.split()
        edges.append(Transition(target=State(target), cost=cost))

    state = State(city, edges)

    