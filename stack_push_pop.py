
class Stack:
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop() if self.items else None


def main():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    print(stack.pop())
    print(stack.pop())

if __name__ == "__main__":
    main()
