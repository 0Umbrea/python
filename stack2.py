class stack:
    def __init__(self,size=100):
        self.size=size
        self.stack=[]
        self.top=-1
    def is_empty(self):
        return self.top==-1
    def is_full(self):
        return self.top+1==self.size
    def push(self,val):
        if self.is_full():
            return Exception('Stack is full')
        self.stack.append(val)
        self.top+=1
    def pop(self):
        if self.is_empty():
            return Exception('Stack is empty')
        self.stack.pop()
        self.top-=1
    def peek(self):
        if self.is_empty():
            return Exception('Stack is empty')
        else:
            return self.stack[self.top]
    def evaluate_reverse_polish(expression):
        stack = []  
        operators = ['+', '-', '*', '/']  
        for token in expression:
            if token not in operators:
                stack.append(int(token))
            else:
                operand2 = stack.pop()
                operand1 = stack.pop()
                if token == '+':
                    result = operand1 + operand2
                elif token == '-':
                    result = operand1 - operand2
                elif token == '*':
                    result = operand1 * operand2
                elif token == '/':
                    result = operand1 / operand2
                stack.append(result) 
        return stack[0] 