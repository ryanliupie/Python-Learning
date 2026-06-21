class Node: 
    def __init__(self, data): # we are keeping track of data here
        self.data = data # node with data 
        self.next = None # no data yet
        self.prev = None # no data yet 


class LinkedList: 
    def __init__(self):
        self.head = None # list starts with no object, so the head pointer points to null

    def search(self, target): # O(n)
        current = self.head # we set a current node equal to the head 
        while current: # means while current is not null
            if current.data == target: 
                return current 
            current = current.next
        return None
    
    def insert(self, node): # O(1)
        node.next = self.head # if we wanted to insert 5, it would be like "5 → 10 ⇄ 20 ⇄ 30", so node.next = node10
        if self.head: # if the list is not empty, we update the old head's prev, before: "None ← 10 ⇄ 20 ⇄ 30", after: "5 ⇄ 10 ⇄ 20 ⇄ 30", so 10.prev = 5
            self.head.prev = node 

        self.head = node # update the head to the new node 
        node.prev = None # since the new node is becoming the first node, it has no previous node "None ← 5 ⇄ 10 ⇄ 20 ⇄ 30"
    
    def delete(self, node):
        if node.prev is not None: # so lets say we have 10, 20, 30, and currently we specify node 20. If the node before it not empty, then the next node is the node after the current: 10 → 30
            node.prev.next = node.next
        else: 
            self.head = node.next # now if the head is 10 and we want to delete it, it moves forward, so 20 ⇄ 30 





