from state import State


class Transition:
    def __init__(self,target: State, cost: int ):
        self.target = target
        self.cost = cost
