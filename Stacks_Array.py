class Stack:
    def __init__(self):
        self.data = []
    
    def push(self, data):
        self.data.append(data)
    
    def pop(self):
        return self.data.pop() if self.data else None
    
#Example Usage
Sample_stack = Stack()

Sample_stack.push(5)
Sample_stack.push(6)
Sample_stack.push(7)

print("Push",Sample_stack.data)



