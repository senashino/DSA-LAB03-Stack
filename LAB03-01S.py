class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            print("Stack is empty")
            return None
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            print("Stack is empty")
            return None
    
    def is_empty(self):
        return len(self.items) == 0
    
    def show(self):
        print("Remaining Stack:", self.items)


stack = Stack()

stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
stack.push(50)

print("Top item is:", stack.peek())

stack.pop()
stack.pop()
stack.pop()

stack.show()
