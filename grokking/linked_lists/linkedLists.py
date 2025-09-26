class SLL:
    def __init__(self, head=None):
        self._head = head

    class Node:
        def __init__(self, value=0, next=None):
            self.value = value
            self.next = next

    def delete(self, target):
        curr = self._head
        prev = None

        while curr and curr.next:
            if curr.value == target:
                if not prev:
                    self._head = curr.next

                else:
                    prev.next = curr.next

                return

            prev = curr
            curr = curr.next

    def insert_in_sorted_list(self, new_data):
        curr = self._head
        prev = None

        while curr:
            if new_data.value <= curr.value and prev is None:
                new_data.next = curr
                self._head = new_data

            elif curr.next and (curr.value <= new_data.value <= curr.next.value):
                new_data.next = curr.next
                curr.next = new_data

            else:
                curr.next = new_data


class DLL:
    def __init__(self):
        self._head = None
        self._tail = None

    class Node:
        def __init__(self, value, next=None, prev=None):
            self._value = value
            self._next = next
            self._prev = prev

        def has_next(self):
            return self._next is not None

        def append(self, next_node):
            self._next = next_node

            if next_node:
                next_node._prev = self

        def prepend(self, prev_node):
            if self._prev:
                self._prev._next = prev_node

            self._prev = prev_node

    
    def is_empty(self) -> bool:
        return self._head is None
    
    
    def insert_to_back(self, data):

        if self._tail is None:
            self._tail = self._head = DLL.Node(data)

        else:
            old_tail = self._tail
            self._tail = DLL.Node(data)
            self._tail.prepend(old_tail)


    def delete_from_front(self):

        if self.is_empty():
            raise ValueError('Delete on an empty list.')
        
        data = self._head._value
        self._head = self._head._next

        if self._head is None:
            self._tail = None
        else:
            self._head.prepend(None)
            
        return data
                
            
def reverse_ssl(ssl):
    """
    Three pointers:
    prev, curr, and next.

    Course of action:

    while next is not none:
    - point curr at prev
    - set prev to curr
    - set curr to next
    - set next to next.next 
    """

    curr = ssl._head
    prev = None
    next_node = curr.next

    while curr:
        curr.next = prev
        prev = curr
        curr = next_node
        next_node = next_node.next

    return prev