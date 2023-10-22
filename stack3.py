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
    def decode_string(s):
        stack = [] 
        curr_num = 0
        curr_str = ''  
        for char in s:
            if char.isdigit():
                curr_num = curr_num * 10 + int(char)
            elif char == '[':
                stack.append(curr_str) 
                stack.append(curr_num)
                curr_num = 0 
                curr_str = '' 
            elif char == ']':
                num = stack.pop()
                prev_str = stack.pop()
                curr_str = prev_str + curr_str * num 
            else:
                curr_str += char
        return curr_str