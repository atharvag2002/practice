
class Queue:
    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return None
    
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)
    
    def peek(self):
        if not self.is_empty():
            return self.items[0]
        return None


def main():
    q = Queue()
    for item in [1, 2, 3, 4, 5]:
        q.enqueue(item)
    
    print(f"Queue size: {q.size()}")
    print(f"Front element: {q.peek()}")
    
    while not q.is_empty():
        print(f"Dequeued: {q.dequeue()}")


if __name__ == "__main__":
    main()
