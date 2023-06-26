"""
Python Data Structures - A Game-Based Approach
Queue class
Robin Andrews - https://compucademy.net/
"""

from collections import deque


class Queue:
    def __init__(self):
        self.items = deque()

    def is_empty(self):
        return not self.items  # Empty deck returns zero

    def enqueue(self, item):  # End of stack
        self.items.append(item)

    def dequeue(self):  # Front of stack
        return self.items.popleft()

    def size(self):
        return len(self.items)

    def peek(self):
        return self.items[0]

    def __str__(self):
        return str(self.items)


if __name__ == "__main__":
    q = Queue()
    q.enqueue("learning")
    q.enqueue("with")
    q.dequeue()
    print(q)



    # print(q)
    # print(q.is_empty())
    # q.enqueue("A")
    # q.enqueue("D")
    # q.enqueue("F")
    # print(q)
    # print(q.dequeue())
    # print(q.dequeue())
    # print(q)
    # print(q.size())
    # print(q.peek())
    # print(q)
