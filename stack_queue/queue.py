class Queue:
    
    def __init__(self):
        self.queue = []
    
        
    def is_empty(self):
        return self.queue == []
    
    
    def enqueue(self, data):
        self.queue.append(data)
        
    
    def dequeue(self):
        if self.is_empty():
            return -1
        data = self.queue[0]
        del self.queue[0]
        return data
    
    
    def peek(self):
        return self.queue[0]
    
    
    def size(self):
        return len(self.queue)
    
    