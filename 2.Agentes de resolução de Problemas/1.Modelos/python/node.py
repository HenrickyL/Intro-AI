from dataclasses import dataclass
from typing import List
from state import State

@dataclass
class Node:
    state: "State"
    cost: int
    father: "Node"

    def __init__(self, state:State, cost:int = 0 , father: 'Node' = None):
        self.state = state
        self.cost = cost
        self.father = father

    def fatherPath(self):
        node = self
        while(node != None):
            print(node.state.name,end=' -> ')
            node = node.father
        print()
        
    def __lt__(self, __o: "Node") -> bool:
        return self.cost <= __o.cost
    
    def __eq__(self, __o: "Node") -> bool:
        if(__o == None):
            return False
        return self.state == __o.state

    def __str__(self) -> str:
        return str(f'{self.state.name} - {self.cost}')