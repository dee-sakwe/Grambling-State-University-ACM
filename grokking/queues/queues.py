from linked_lists.linkedLists import DLL

class queue:
    def __init__(self):
        self.data = DLL()

    def is_empty(self):
        return self.data.is_empty()
    
    def enqueue(self, value):
        self.data.insert_to_back(value)

    def dequeue(self):
        if self.is_empty():
            raise ValueError("Cannot dequeue from an empty queue")
        
        return self._data.delete_from_front()