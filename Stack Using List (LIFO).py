class Stack:
    def __init__(self):
        self.stack = []
    # push operation
    def push(self,value):
        self.stack.append(value)
        print(f"{value} pushed to stack")
    # pop operation
    def pop(self):
        if self.is_empty():
            print("stack is empty")
            return None
        return self.stack.pop()
    # peek operation
    def peek(self):
        if self.is_empty():
            print("stack is empty")
            return None
        return self.stack[-1]
    def is_empty(self):
        return len(self.stack) == 0
    def __str__(self):
        return str(self.stack)
if __name__ == "__main__":
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.peek()
    print("peek:",stack.peek())
    print("pop:",stack.pop())
    print("pop:",stack.pop())
    print("pop:",stack.pop())
    print("pop:",stack.pop())