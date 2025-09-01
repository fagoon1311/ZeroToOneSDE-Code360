class Queue :

    def __init__(self):
        self.items = []

#Define data members and __init__()




'''----------------- Public Functions of Queue -----------------'''


def isEmpty(self) :
    #Implement the isEmpty() function
    if len(self.items) == 0:
        return True
    else:
        return False



def enqueue(self, data) :
    self.items.append(data)
    #Implement the enqueue(element) function



def dequeue(self) :
    #Implement the dequeue() function
    if self.isEmpty():
        return -1
    else:
        return self.items.pop(0)



def front(self) :
    if self.isEmpty():
        return -1
    else:
        return self.items[0]
    #Implement the front() function
