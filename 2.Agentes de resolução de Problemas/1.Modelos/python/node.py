from dataclasses import dataclass

@dataclass
class Node:
    def __init__(self, state, cost:int = 0 , father: 'Node' = None):
        self.state = state
        self.cost = cost
        self.father = father

    def fatherPath(self):
        node = self
        stack = []
        sol = ''
        while(node != None):
            stack.append(node)
            node = node.father
        while(stack):
            node = stack.pop()
            sol += node.state.name+", "
        return sol
        
    def __lt__(self, __o) :
        return self.cost < __o.cost
    
    def __eq__(self, __o) :
        if(__o == None):
            return False
        return self.state == __o.state

    def __str__(self) :
        return str(f'{self.state.name} - {self.cost}')