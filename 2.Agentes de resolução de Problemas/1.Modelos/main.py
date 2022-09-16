from state import State
from map import Map
from transition import Transition
with open('data.txt','r') as file:
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
        state.show()
        states.append(state)
map = Map(states)
print(map)
map.draw(layout='rt')

    