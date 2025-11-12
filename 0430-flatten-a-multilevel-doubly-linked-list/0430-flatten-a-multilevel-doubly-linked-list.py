"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        def insert(node):
            curr = node
            last = curr
            while curr:
                target = curr.next
                if curr.child:
                    left, right = insert(curr.child)
                    curr.next = left
                    left.prev = curr
                    right.next = target
                    if target:
                        target.prev = right
                    curr.child = None
                    last = right
                else:
                    last = curr
                curr = target
            return node, last
        insert(head)
        return head