class CircularQueue:
    def __init__(self, kich_thuoc):
        self.kich_thuoc = kich_thuoc
        self.mang = [None] * kich_thuoc
        self.front = -1
        self.rear = -1
        
    def is_empty(self):
        return self.front == -1
        
    def is_full(self):
        return (self.rear + 1) % self.kich_thuoc == self.front
        
    def enqueue(self, val):
        if self.is_full():
            print("Hang doi day!")
            return False
            
        if self.is_empty():
            self.front = 0
            
        self.rear = (self.rear + 1) % self.kich_thuoc
        self.mang[self.rear] = val
        return True
        
    def dequeue(self):
        if self.is_empty():
            print("Hang doi rong!")
            return None
            
        val = self.mang[self.front]
        
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.kich_thuoc
            
        return val

cq = CircularQueue(3)
cq.enqueue(1)
cq.enqueue(2)
cq.enqueue(3)
cq.dequeue()
cq.enqueue(4)
print("Da enqueue vao slot cuoi -> vong len index 0")
