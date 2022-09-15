from state import State
from transition import Transition
class Map:
    def __init__(self, states:set[State]):
        self.states = states.copy()