class QueueList:
    def __init__(self):
        self.hang_doi = []
    
    def enqueue(self, val):
        self.hang_doi.append(val)
        
    def dequeue_cham(self):
        if self.hang_doi:
            return self.hang_doi.pop(0)
        return None

class QueueToiUu:
    def __init__(self):
        self.hang_doi = []
        self.front = 0
        
    def enqueue(self, val):
        self.hang_doi.append(val)
        
    def dequeue_nhanh(self):
        if self.front < len(self.hang_doi):
            val = self.hang_doi[self.front]
            self.front += 1
            return val
        return None

q = QueueToiUu()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print("pop ->", q.dequeue_nhanh())
print("con lai bat dau tu index", q.front)
