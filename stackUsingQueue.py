# Implement a stack using a queue.
# use 2 lists to implement the stack.
# use one list as the main stack and the other list as the auxiliary stack.
# Time Complexity: O(n) for push and pop operations.
# Space Complexity: O(n) for the auxiliary stack.


from typing import List

class Stack:
    def __init__(self):
        # Define the data members.
        self.q1 = []
        self.q2 = []
        

    def getSize(self) -> int:
        # Implement the getSize() function.
        return len(self.q1)
        

    def isEmpty(self) -> bool:
        # Implement the isEmpty() function.
        return len(self.q1) == 0
        

    def push(self, element: int) -> None:
        # Implement the push() function.
        self.q1.append(element)
        

    def pop(self) -> int:
        # Implement the pop() function.
        if self.isEmpty():
            return -1
        while len(self.q1) > 1:
            self.q2.append(self.q1[0])
            self.q1.pop(0)

        topele = self.q1.pop(0)
        self.q1, self.q2 = self.q2, self.q1
        return topele
        

    def top(self) -> int:
        # Implement the top() function.
        if self.isEmpty():
            return -1
        while len(self.q1) > 1:
            self.q2.append(self.q1[0])
            self.q1.pop(0)

        topele = self.q1.pop(0)
        self.q2.append(topele)
        self.q1, self.q2 = self.q2, self.q1
        return topele


