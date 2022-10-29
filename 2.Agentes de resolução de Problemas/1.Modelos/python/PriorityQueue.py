from typing import Callable
from node import Node
from state import State


class PriorityQueue(list):
    def __init__(self, fn : Callable[[Node,Node],bool] = lambda x,y: x < y):
        self.queue: list[Node] = []
        self.fn = fn
 
    def __len__(self) -> int:
        return self.queue.__len__()

    def __str__(self):
        return ' '.join([str(i) for i in self.queue])
 
    # for checking if the queue is empty
    def isEmpty(self):
        return len(self.queue) == 0
 
    # for inserting an element in the queue
    def insert(self, data):
        self.queue.append(data)
 
    # for popping an element based on Priority
    def delete(self):
        try:
            max_val = 0
            for i in range(len(self.queue)):
                if(self.fn(self.queue[i], self.queue[max_val])):
                    max_val = i
            item = self.queue[max_val]
            del self.queue[max_val]
            return item
        except IndexError:
            print()
            exit()
 
if __name__ == '__main__':
    myQueue = PriorityQueue()
    myQueue.insert(Node(State("aaa"), 10, None))
    myQueue.insert(Node(State("bv"), 5, None))
    myQueue.insert(Node(State("bv"), 7, None))
    
    print(myQueue.delete())
