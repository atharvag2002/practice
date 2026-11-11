
class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None
    
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None


def main():
    s = Stack()
    for item in [1, 2, 3, 4, 5]:
        s.push(item)
    
    print(f"Stack size: {s.size()}")
    print(f"Top element: {s.peek()}")
    
    while not s.is_empty():
        print(f"Popped: {s.pop()}")


if __name__ == "__main__":
    main()
