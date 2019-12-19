import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def pop(self):
        #first check it empty
        if self.size > 0: #syntax needs :
            self.size -= 1
            return self.storage.remove_from_head()
            # return self.storage.remove_from_tail()
            # why not when pop removes from end
        else:
            return None

    def push(self, value):
        self.size += 1
        self.storage.add_to_head(value)

    def len(self):
        return self.size
