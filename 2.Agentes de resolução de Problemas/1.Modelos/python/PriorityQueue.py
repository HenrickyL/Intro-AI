from heapq import heapify
from node import Node
from state import State


class PriorityQueue(list):
    def __init__(self, fn  = lambda x,y: x.cost < y.cost):
        self.queue = []
        self.fn = fn
 
    def __len__(self) :
        return self.queue.__len__()

    def __str__(self):
        return ' '.join([str(i) for i in self.queue])
 
    # for checking if the queue is empty
    def isEmpty(self):
        return len(self.queue) == 0
 
    # for inserting an element in the queue
    def insert(self, data):
        self.queue.append(data)
 
    def remove(self,data):
        index = self.queue.index(data)
        res = self.queue[index]
        del self.queue[index]
        heapify(self.queue)
        return res
    # for popping an element based on Priority
    def delete(self):
        try:
            max_val = 0
            for i in range(len(self.queue)):
                if ( self.fn(self.queue[i], self.queue[max_val])):
                    max_val = i
            item = self.queue[max_val]
            del self.queue[max_val]
            return item
        except IndexError:
            print()
            exit()
 
if __name__ == '__main__':
    myQueue = PriorityQueue()
    myQueue.insert(Node(State("1"), 8, None))
    myQueue.insert(Node(State("2"), 7, None))
    myQueue.insert(Node(State("3"), 6, None))
    myQueue.insert(Node(State("4"), 10, None))
    myQueue.insert(Node(State("5"), 1, None))
    
    while(myQueue.queue):
        print(myQueue.delete())
