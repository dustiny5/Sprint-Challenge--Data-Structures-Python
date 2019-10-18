import sys
#sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        # Add element to the end of the queue
        self.size += 1
        return self.storage.add_to_head(value)

    def dequeue(self):
        # Remove element at the front of the queue
        if self.size is not 0:
            self.size -= 1
            return self.storage.remove_from_tail()

    def len(self):
        # Get the length of the queue list
        return self.size
