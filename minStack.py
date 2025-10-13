#Problem Statement: Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.



class minStack:		
    # Constructor
    def __init__(self):
        # Write your code here.
        self.a = []
        self.b = []

    # Function to add another element equal to num at the top of stack.
    def push(self, num: int) -> None:
        # Write your code here
        self.a.append(num)
        if len(self.b) < 1:
            self.b.append(num)
        else:
            if self.b[-1] >= num:
                self.b.append(num)



    # Function to remove the top element of the stack.
    def pop(self) -> int:
        # Write your code here.
        if self.a[-1] == self.b[-1]:
            self.b.pop()
        self.a.pop()


    # Function to return the top element of stack if it is present. Otherwise return -1.
    def top(self) -> int:
        # Write your code here.
        return self.a[-1]


    # Function to return minimum element of stack if it is present. Otherwise return -1.
    def getMin(self) -> int:
        return self.b[-1]
