class LL:
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

        

            
