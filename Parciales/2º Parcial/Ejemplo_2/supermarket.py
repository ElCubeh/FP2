from containerbase import ContainerBase


class Client:

    def __init__(self, name, total_cost):
        self.name = name
        self.total_cost = total_cost

    def __str__(self):
        return f"{self.name}: {self.total_cost}"


class CheckoutQueue:
    class Node:
        __slots__ = ('client', 'next')
        def __init__(self, client, next_node=None):
            self.client = client
            self.next = next_node
            
    def __init__(self):
        self.first = None
        self.last = None
        self._daily_sales = 0.0
        
    def enqueue(self, client):
        new_node = CheckoutQueue.Node(client)
        if self.first is None:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node

    def dequeue(self):
        if self.first is None:
            return None
            
        client = self.first.client
        self.first = self.first.next
        if self.first is None:
            self.last = None
            
        self._daily_sales += client.total_cost
        return client

    @property
    def daily_sales(self):
        return self._daily_sales

    def split(self):
        par_first = None
        par_last = None
        impar_first = None
        impar_last = None
        
        current = self.first
        index = 0
        
        while current:
            next_node = current.next
            current.next = None
            
            if index % 2 == 0:
                if par_first is None:
                    par_first = current
                    par_last = current
                else:
                    par_last.next = current
                    par_last = current
            else:
                if impar_first is None:
                    impar_first = current
                    impar_last = current
                else:
                    impar_last.next = current
                    impar_last = current
            
            current = next_node
            index += 1
        
        self.first = par_first
        self.last = par_last
        
        new_queue = CheckoutQueue()
        new_queue.first = impar_first
        new_queue.last = impar_last
        return new_queue