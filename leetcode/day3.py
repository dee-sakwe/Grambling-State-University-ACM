from typing import List, Tuple, Optional


class ListNode:
    def __init__(self, key=-1, val=-1, next=None):
        self.key = key
        self.val = val
        self.next = next


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class MyHashMap:
    """
    Design a HashMap without using any built-in hash table libraries.

    Implement the `MyHashMap` class:

    - `MyHashMap()` initializes the object with an empty map.
    - `void put(int key, int value)` inserts a `(key, value)` pair into the HashMap. If the `key` already exists in the map, update the corresponding `value`.
    - `int get(int key)` returns the `value` to which the specified `key` is mapped, or `-1` if this map contains no mapping for the `key`.
    - `void remove(key)` removes the `key` and its corresponding `value` if the map contains the mapping for the `key`.


    Example 1:

        Input
        ["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
        [[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
        Output
        [null, null, null, 1, -1, null, 1, null, -1]

    Explanation
        MyHashMap myHashMap = new MyHashMap();
        myHashMap.put(1, 1); // The map is now [[1,1]]
        myHashMap.put(2, 2); // The map is now [[1,1], [2,2]]
        myHashMap.get(1);    // return 1, The map is now [[1,1], [2,2]]
        myHashMap.get(3);    // return -1 (i.e., not found), The map is now [[1,1], [2,2]]
        myHashMap.put(2, 1); // The map is now [[1,1], [2,1]] (i.e., update the existing value)
        myHashMap.get(2);    // return 1, The map is now [[1,1], [2,1]]
        myHashMap.remove(2); // remove the mapping for 2, The map is now [[1,1]]
        myHashMap.get(2);    // return -1 (i.e., not found), The map is now [[1,1]]
    """

    def __init__(self):
        self.map = [ListNode() for i in range(1000)]

    def __repr__(self):
        valid = []

        for i, ll in enumerate(self.map):
            if not ll.next:
                continue

            valid.append(ll.next)

        for i, ll in enumerate(valid):
            if ll.next:
                others = []

                curr = ll

                while curr:
                    others.append((f"{curr.key} : {curr.val}"))
                    curr = curr.next

                valid[i] = others

        for i, ll in enumerate(valid):
            if isinstance(ll, list):
                continue

            valid[i] = f"{ll.key} : {ll.val}"

        return f"Hashmap: {valid}"

    def print_list(self, listNode: ListNode):
        curr = listNode
        array = []

        while curr:
            array.append(str(curr.val))
            curr = curr.next

        print(" -> ".join(array))

    def hash(self, key):
        return key % len(self.map)

    def put(self, key, value):
        hashed_key = self.hash(key)

        # If the dummy node doesn't point to anything yet
        if not self.map[hashed_key].next:
            self.map[hashed_key].next = ListNode(key, value)

        else:
            curr = self.map[hashed_key].next  # Dummy node

            while curr:
                if curr.key == key:
                    curr.val = value
                    return

                if not curr.next:
                    curr.next = ListNode(key, value)

                curr = curr.next

    def get(self, key: int) -> int:
        hashed_key = self.hash(key)

        # If the dummy node points to None
        if not self.map[hashed_key].next:
            return -1

        curr = self.map[hashed_key].next

        while curr:
            if curr.key == key:
                return curr.val

            curr = curr.next

        return -1

    def remove(self, key: int) -> None:
        hashed_key = self.hash(key)

        if self.map[hashed_key].next:
            # Start with the dummy node so we can point to null if the key to remove is the first one
            curr = self.map[hashed_key]

            while curr.next:
                if curr.next.key == key:
                    curr.next = curr.next.next
                    return

                curr = curr.next

    def tests(self):
        myHashMap = MyHashMap()
        myHashMap.put(1, 1)  # // The map is now [[1,1]]
        myHashMap.put(2, 2)  # // The map is now [[1,1], [2,2]]
        myHashMap.get(1)  # // return 1, The map is now [[1,1], [2,2]]
        myHashMap.get(
            3
        )  # // return -1 (i.e., not found), The map is now [[1,1], [2,2]]
        myHashMap.put(
            2, 1
        )  # // The map is now [[1,1], [2,1]] (i.e., update the existing value)
        myHashMap.put(2002, 5)  # [[1,1], [[2, 1] -> [2002, 5]]]
        myHashMap.put(1002, 1)  # [[1,1], [[2, 1] -> [2002, 5] ->[1002, 1] ]]
        print(myHashMap.get(2))
        print(myHashMap.get(1002))

        print(myHashMap)

        myHashMap.remove(2)
        myHashMap.get(2)

        print(myHashMap)


def maxDepth(root: Optional[TreeNode]) -> int:
    """
    Given the `root` of a binary tree, return its maximum depth.

    A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

    Example 1:

        Input: root = [3,9,20,null,null,15,7]
        Output: 3

    Example 2:

        Input: root = [1,null,2]
        Output: 2

    Constraints:

        The number of nodes in the tree is in the range `[0, 10⁴]`.
        `-100 <= Node.val <= 100`
    """
    # Recursive solution
    # if not root:
    #     return 0

    # return 1 + max(maxDepth(root.left), maxDepth(root.right))

    # BFS solution

    # from collections import deque

    # if not root:
    #     return 0

    # q = deque([root])

    # level = 0

    # while q:
    #     for i in range(len(q)):
    #         node = q.popleft()

    #         if node.left:
    #             q.append(node.left)

    #         if node.right:
    #             q.append(node.right)

    #     level += 1

    # return level

    # Iterative DFS

    stack: List[Tuple[TreeNode | None, int]] = [(root, 1)]

    depth = 0

    while stack:
        node, level = stack.pop()

        if node:
            depth = max(depth, level)
            stack.append((node.left, level + 1))
            stack.append((node.right, level + 1))

    return depth

