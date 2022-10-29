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
        stack: list[Node] = []
        while(node != None):
            stack.append(node)
            node = node.father
        while(stack):
            node = stack.pop()
            print(f"{node.state.name} - {node.cost}",end=' -> ')
            
        print()
        
    def __lt__(self, __o: "Node") -> bool:
        return self.cost < __o.cost
    
    def __eq__(self, __o: "Node") -> bool:
        if(__o == None):
            return False
        return self.state == __o.state

    def __str__(self) -> str:
        return str(f'{self.state.name} - {self.cost}')